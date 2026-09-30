import os
import math
import json

n=5

for file in os.listdir('jsons'):
    if file.endswith('json'):
        file_path=os.path.join('jsons',file)
        with open(file_path,'r',encoding='utf-8') as f:
            data=json.load(f)
            new_chunks=[]
            num_chunks=len(data['chunks'])
            num_group=math.ceil(num_chunks/n)
            
            for i in range(num_group):
                start_idx=i*n
                end_idx=min((i+1)*n,num_chunks)
                chunk_grp=data['chunks'][start_idx:end_idx]
            
                new_chunks.append({
                    'number':data['chunks'][0]['number'],
                    'title':chunk_grp[0]['title'],
                    'start':chunk_grp[0]['start'],
                    'end':chunk_grp[-1]['end'],
                    'text':' '.join(c['text'] for c in chunk_grp)
                })
                
    
            os.makedirs('newjsons',exist_ok=True)
            with open(f'newjsons/{file}', 'w',encoding='utf-8') as json_file:
                json.dump({'chunks':new_chunks,'text':data['text']},json_file,indent=4)  

                #after doing this i renamed the newjsons folder to jsons folder and deleted jsons folder & run json_preprocessing