import os
import subprocess

files=os.listdir('rag_videos')
for file in files:
    tutorial_number=file.split(' #')[1].split('[')[0]
    mp3_name=file.split(' ｜')[0]
    print(f'{tutorial_number}_{mp3_name}.mp3')
    subprocess.run(['ffmpeg','-i',f'rag_videos/{file}',f'audios/{tutorial_number}_{mp3_name}.mp3'])