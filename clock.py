from PIL import Image, ImageDraw, ImageFilter, ImageFont
from datetime import datetime
import subprocess
import time
import os
import random
import sys

while True:
    currentTime = datetime.now()
    hour = currentTime.strftime('%I')
    minute = currentTime.strftime('%M')
    minuteTens = minute[:1]
    minuteOnes = minute[1:]
    ampm = currentTime.strftime('%p').lower()
    x = random.randint(0, 128)
    y = random.randint(0, 176)

    bgImages = os.listdir("images")
    bgImage = bgImages[random.randint(0,len(bgImages)-1)]
    bgImagePath = "images/"+bgImage

    hourImages = os.listdir("hours/"+hour)
    hourImagePath = "hours/"+hour+"/"+hourImages[random.randint(0,len(hourImages)-1)]

    colonImages = os.listdir("colon")
    colonImagePath = "colon/"+colonImages[random.randint(0,len(colonImages)-1)]

    minTenImages = os.listdir("minute-tens/"+minuteTens)
    minTenImagePath = "minute-tens/"+minuteTens+"/"+minTenImages[random.randint(0,len(minTenImages)-1)]

    minOneImages = os.listdir("minute-ones/"+minuteOnes)
    minOneImagePath = "minute-ones/"+minuteOnes+"/"+minOneImages[random.randint(0,len(minOneImages)-1)]
    
    if ampm == "pm" and (hour == "12" or hour == "1" or hour == "2" or hour == "3" or hour == "4"):
        amPmImagePath = "ampm/pm/toon.png"
    else:
        amPmImages = os.listdir("ampm/"+ampm)
        amPmImagePath = "ampm/"+ampm+"/"+amPmImages[random.randint(0,len(amPmImages)-1)]

    img = Image.open(bgImagePath)

    hourImage = Image.open(hourImagePath)
    img.paste(hourImage, (x,y), hourImage)
    colonImage = Image.open(colonImagePath)
    img.paste(colonImage, (x+64,y), colonImage)
    minTenImage = Image.open(minTenImagePath)
    img.paste(minTenImage, (x+96,y), minTenImage)
    minOneImage = Image.open(minOneImagePath)
    img.paste(minOneImage, (x+128,y), minOneImage)
    amPmImage = Image.open(amPmImagePath)
    img.paste(amPmImage, (x+160,y), amPmImage)

    img.save("time.png")

    if "--display" in sys.argv or "-d" in sys.argv:
        subprocess.run(["sudo", "fbi", "-a", "-T", "1", "time.png"])

    time.sleep(10)