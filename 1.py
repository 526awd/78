import os
inp="1.mp4"
to="zundamon1.mp4"
si=99
os.system("cp "+inp+" "+to)
for i in range(si):
    os.system("ffmpeg -f concat -safe 0 -i input.txt -c copy "+to)
    os.system("rm zundamon.mp4"+)
    os.system("cp zundamon1.mp4 zundamon.mp4")
    os.system("rm zundamon1.mp4")
