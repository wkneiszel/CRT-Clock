from PIL import Image, ImageDraw, ImageFilter, ImageFont
from datetime import datetime
import subprocess
import time
import os
import random

while True:
    currentTime = datetime.now()
    hour = currentTime.strftime('%I')
    minute = currentTime.strftime('%M')
    minuteTens = minute[:1]
    minuteOnes = minute[1:]

    bgImages = os.listdir("images")
    bgImage = bgImages[random.randint(0,len(bgImages)-1)]
    bgImagePath = "images/"+bgImage

    hourImages = os.listdir("hours/"+hour)
    hourImagePath = "hours/"+hour+"/"+hourImages[random.randint(0,len(hourImages)-1)]

    img = Image.open(bgImagePath)
    hourImage = Image.open(hourImagePath)
    img.paste(hourImage, (0,0), hourImage)
    img.save("time.png")

    #subprocess.run(["sudo", "fbi", "-a", "-T", "1", "time.png"])

    time.sleep(5)