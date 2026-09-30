import requests
import os
import json
import numpy as np
import pandas as pd
import joblib



def create_embbeding(text_list):
    r = requests.post('http://localhost:11434/api/embed',json={'model':'bge-m3','input':text_list})
    
    embedding= r.json()['embeddings']
    return embedding



jsons = os.listdir('jsons')

my_dict=[]
chunk_id=0

for jason in jsons:
    if jason.endswith('json'):
        with open(f'jsons/{jason}') as f:
            content = json.load(f)
        print(f'creating embedding for {jason}')
        embedding = create_embbeding([c['text'] for c in content['chunks']] )
    

    for i,chunk in enumerate(content['chunks']):
        chunk['chunk_id']= chunk_id
        chunk['embedding']=embedding[i]
        chunk_id+=1
        my_dict.append(chunk)
    

df = pd.DataFrame.from_records(my_dict)

joblib.dump(df,'embedding.joblib')
