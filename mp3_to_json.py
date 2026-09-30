import json
import os
import whisper
import torch

device = "cuda" if torch.cuda.is_available() else "cpu"
model = whisper.load_model('large-v2').to(device)

audios = os.listdir('audios')

for audio in audios:
    if '_' in audio:
        #result = model.transcribe(audio=f'audios/sample.mp3',language='hi',task='translate',word_timestamps=False) //for testing 
        result = model.transcribe(audio=f'audios/{audio}',language='hi',task='translate',word_timestamps=False)
        video_no=audio.split('_')[0]
        title=audio.split('_')[1][:-4]
        chunk =[]
        for segment in result['segments']:                                   
            chunk.append({'vid_no': video_no, 'vid_title':title,'start':segment['start'],'end':segment['end'],'text':segment['text']})
        

        chunk_with_metadata={'chunks':chunk,'text':result['text']}
        with open(f'jsons/{video_no}_{title}.json','w') as f:
            json.dump(chunk_with_metadata,f)
        

