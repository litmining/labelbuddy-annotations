import json
import os

import openai
import backoff

OUTPUT_DIR = "llm_extract_task_info/"

SYSTEM_MESSAGE_1 = """
you are an expert cognitive neuroscientist.
You will be provided with a text sample from a scientific journal.
Your function is to identify details related to the cognitive task(s) that were performed during an MRI.
Use the provided text to extract the task information.
Reason through your answers and provide as much detail as possible that
will help in understanding the cognitive task(s) performed during the MRI.


Please extract the following information for each of the tasks used in the MRI study:
- The name of the psychological task. A task is **NOT** a model or an analysis method, but IS a specific cognitive/psychological task that participants performed during the MRI.
- The definition of the task. Provide descriptions of the conditions here if available. This is likely in a Methods section.
- The list of conditions within the task. These can be different categories of stimuli and/or some other manipulation of the stimuli. Conditions are not differences between groups of participants.
- The list of contrasts of conditions within the task, (e.g., 'faces > houses'). Report interactions between conditions if available. The tables at the end of the paper may be useful for this information.

If *any* of the information is missing and you are not confident, return null for that specific field.
ONLY report information for tasks used in MRI, fMRI or neuroimaging.


"""

TASK_SCHEMA = {
    "type": "object",
    "properties": {
        "tasks": {
            "name": "tasks_schema",
            "description": "list of psychological tasks used in text",
            "type": "array",
            "items": {
                "name": "task_schema",
                "description": "schema for psychological task description",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "name": {
                            "type": "string",
                            "description": "The name of the psychological task."
                        },
                        "definition": {
                            "type": "string",
                            "description": "Definition of the psychological task."
                        },
                        "conditions": {
                            "type": "array",
                            "items": {
                                "type": "string"
                            },
                            "description": "The conditions within the task."
                        },
                        "contrasts": {
                            "type": "array",
                            "items": {
                                "type": "string"
                            },
                            "description": "The comparisons of conditions within the task, (e.g., 'faces > houses')."
                        }
                    }
                }
            }
        }
    }
}


def load_json_files():
    # Define the input directory and file names
    input_dir = "documents"
    with open(f"{input_dir}/documents_00001.jsonl", 'r') as json_file:
        json_list = list(json_file)

    for i, json_str in enumerate(json_list):
        json_list[i] = json.loads(json_str)

    return json_list


@backoff.on_exception(backoff.expo, openai.RateLimitError)
def query_openai(prompt, schema, model):
    # Set your OpenAI API key
    openai.api_key = os.environ.get("OPENAI_API_KEY")

    # Send the query to the OpenAI API
    try:
        response = openai.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": SYSTEM_MESSAGE_1},
                {"role": "user", "content": prompt},
            ],
            temperature=0.0,
            tools=[
                {
                    "type": "function",
                    "function": {
                        "name": "extractData",
                        "description": "Extract data from scientific text",
                        "parameters": TASK_SCHEMA,
                    }
                }
            ]
        )
    except openai.BadRequestError as e:
        return {'error': f'OpenAI BadRequestError: {e}'}
    # Convert the response to JSON
    try:
        response_json = json.loads(
            response.choices[0].message.tool_calls[0].function.arguments
        )
    except json.JSONDecodeError:
        response_json = {'error': 'Failed to parse JSON response from OpenAI.'}
    except AttributeError:
        response_json = {'error': 'Failed to extract JSON response from OpenAI.'}
    except TypeError:
        response_json = {'error': 'Failed to extract JSON response from OpenAI.'}

    return response_json


# model = "gpt-3.5-turbo-0125"	
# model = "gpt-3.5-turbo-16k-0613"
model = "gpt-4o"

OUTPUT_DIR = f"llm_extract_task_info/{model}"
os.makedirs(OUTPUT_DIR, exist_ok=True)
json_list = load_json_files()
for paper in json_list:
    # prompt = paper['text']
    text = paper['text']
    prompt = SYSTEM_MESSAGE_1 + '\n\n' + text
    output_file = f"{OUTPUT_DIR}/{paper['metadata']['pmid']}.json"
    if os.path.exists(output_file):
        print(f"Skipping {paper['metadata']['pmid']}, already exists.")
        continue
    resp = query_openai(prompt, TASK_SCHEMA, model=model)

    with open(f"{OUTPUT_DIR}/{paper['metadata']['pmid']}.json", 'w') as json_file:
        json.dump(resp, json_file, indent=4)
