import os
inp="studio_video_1754743955890.mp4"
to="zundamon.mp4"
si=99
os.system("cp "+inp+" "+to)
for i in range(si):
    os.system("ffmpeg -f concat -i "+inp+" -i "+to+"-c copy "+to)
