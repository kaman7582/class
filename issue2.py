__author__ = 'huke'
from PIL import Image,ImageDraw,ImageFont
import random

def randChar():
    return chr(random.randint(65,90))

def randColor():
    return (random.randint(64,255),random.randint(64,255),random.randint(64,255))

def drawPic():
    width=240
    height=60
    image= Image.new('RGB',(width,height),(255,255,255))
    font = ImageFont.truetype('C:\Windows\Fonts\Arial.ttf', 36)
    draw=ImageDraw.Draw(image)
    for t in range(4):
        draw.text((60*t+10,10),randChar(),font=font, fill=randColor())
    image.show()



if __name__ == "__main__":
    drawPic()
