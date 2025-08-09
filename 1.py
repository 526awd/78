import os
inp="1.mp4"
to="zundamon.mp4"
si=99
os.system("cp "+inp+" "+to)
for i in range(si):
    os.system("ffmpeg -f concat -safe 0 -i  "+inp+" -i "+to+"-c copy "+to)
