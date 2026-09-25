# convert videos to mp3 files

import os
import subprocess

files = os.listdir("videos")

for file in files:
        tut_number = file.split(" - ")[0].split("#")[1]
        file_name = file.split("  Python Tutorial  ")[0]
        print(tut_number, file_name)  
        subprocess.run(["ffmpeg", "-i", f"videos/{file}", f"audios/{tut_number}_{file_name}.mp3"])  
