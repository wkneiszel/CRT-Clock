from PIL import Image, ImageDraw, ImageFilter, ImageFont
from datetime import datetime
import subprocess
import time
import os
import random
import sys

basepath = sys.path[0]
print(basepath)

while True:
    useFlavor = random.randint(0,5) == 0
    minY = 0
    if useFlavor:
        minY = 64

    currentTime = datetime.now()
    hour = currentTime.strftime('%I')
    minute = currentTime.strftime('%M')
    minuteTens = minute[:1]
    minuteOnes = minute[1:]
    ampm = currentTime.strftime('%p').lower()
    x = random.randint(0, 128)
    y = random.randint(minY, 176)

    bgImages = os.listdir(basepath + "/images")
    bgImage = bgImages[random.randint(0,len(bgImages)-1)]
    bgImagePath = basepath +"/images/"+bgImage

    hourImages = os.listdir(basepath + "/hours/"+hour)
    hourImagePath = basepath +"/hours/"+hour+"/"+hourImages[random.randint(0,len(hourImages)-1)]

    colonImages = os.listdir(basepath +"/colon")
    colonImagePath = basepath +"/colon/"+colonImages[random.randint(0,len(colonImages)-1)]

    minTenImages = os.listdir(basepath +"/minute-tens/"+minuteTens)
    minTenImagePath = basepath +"/minute-tens/"+minuteTens+"/"+minTenImages[random.randint(0,len(minTenImages)-1)]

    minOneImages = os.listdir(basepath +"/minute-ones/"+minuteOnes)
    minOneImagePath = basepath +"/minute-ones/"+minuteOnes+"/"+minOneImages[random.randint(0,len(minOneImages)-1)]
    
    if ampm == "pm" and (hour == "12" or hour == "01" or hour == "02" or hour == "03" or hour == "04"):
        amPmImagePath = basepath +"/ampm/pm/toon.png"
    else:
        amPmImages = os.listdir("ampm/"+ampm)
        amPmImagePath = basepath +"/ampm/"+ampm+"/"+amPmImages[random.randint(0,len(amPmImages)-1)]

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

    if useFlavor:
        flavorImages = os.listdir(basepath +"/flavor")
        flavorImagePath = basepath +"/flavor/"+flavorImages[random.randint(0,len(flavorImages)-1)]
        flavorImage = Image.open(flavorImagePath)
        img.paste(flavorImage, (0,0), flavorImage)


    img.save(basepath +"/time.png")

    if "--display" in sys.argv or "-d" in sys.argv:
        subprocess.run(["sudo", "fbi", "-a", "-T", "1", basepath +"/time.png"])

    time.sleep(20)