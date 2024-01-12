from pathlib import Path

import pandas as pd

folder = Path(__file__).resolve().parent 
files = sorted(folder.glob('documents*.jsonl'))


for file in files:
    df = pd.read_json(file, lines=True)
    for ind, row in df.iterrows():
        print(ind, end='\r')
        title = row["list_title"].lower()
        if 'meta-analy' in title:
            continue
        elif 'meta analy' in title:
            continue
        else:
            df.drop(ind, inplace=True)
        
    df.to_json(file.parent / f'{file.stem}-ma-in-title.jsonl', orient='records', lines=True)
    
d = 1
