import os
import subprocess

files=os.listdir("videos")
for file in files:
    tutorial_no=file.split(" #")[1].split(".")[0]
    file_name=file.split(" | ")[0]
    print(tutorial_no)
    subprocess.run(["ffmpeg","-i",f"videos/{file}",f"audios/{tutorial_no}_{file_name}.mp3"])