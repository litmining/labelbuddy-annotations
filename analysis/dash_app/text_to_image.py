from pathlib import Path

from PIL import Image, ImageFont, ImageDraw
import pandas as pd


def text_to_image(text, figpath):
    fontsize = 18
    height = fontsize * text.count("\n") + fontsize * 2
    width = 1000
    img = Image.new("RGB", (width, height), color=(255, 255, 255))
    fnt = ImageFont.truetype("Pillow/Tests/fonts/FreeMono.ttf", fontsize)
    ImageDraw.Draw(img).text((3, 3), text, font=fnt, fill=(0, 0, 0))
    print("fig saved at \n", figpath)
    img.save(figpath)


# load the data. Each row is an annotation. There may be several annotations per paper
data_path = Path(__file__).resolve().parent / "all_annotations.csv"
df = pd.read_csv(data_path, index_col=False)
df.pmcid = df.pmcid.astype(int)

text_all = ""
for project_name, project_df in df.groupby(["annotation_project"]):
    project_name_upper = project_name.replace("_", " ").upper()
    labels_list = list(set(project_df["annotation_label_name"]))
    labels_list.sort()
    labels_list = [""] + labels_list
    labels_str = "\n        ".join(labels_list)
    n_papers_annotated = len(set(project_df["pmcid"]))
    title = f"{project_name_upper} project"
    underline = "-" * len(title)
    text_list = [
        title,
        underline,
        f"    {n_papers_annotated} papers annotated\n",
        f"    Labels used:",
        labels_str,
        "\n\n",
    ]
    text_str = "\n".join(text_list)
    text_all = text_all + text_str


figpath = Path(__file__).resolve().parent / "figures" / "projects_summary.png"
text_to_image(text_all, figpath)


cols = ["annotation_label_name", "document_from_project"]
for col in cols:
    items = list(set(df[col]))
    text = "\n".join(items)
    filename = col + "s.png"
    figpath = Path(__file__).resolve().parent / "figures" / filename
    text_to_image(text, figpath)
