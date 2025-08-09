import os
inp="1.mp4"
to="zundamon.mp4"
si=99
os.system("cp "+inp+" "+to)
for i in range(si):
    os.system("ffmpeg -f concat -i 1.mp4 -i "+to+"-c copy "+to)
