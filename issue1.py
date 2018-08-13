__author__ = 'huke'
from PIL import Image ,ImageDraw
from PIL import ImageFont

import random

if __name__=="__main__":
    im=Image.open("123.jpg")
    font = ImageFont.load_default().font

    print(font)
    #im.show()
    w,h=im.size
    rnum=random.randrange(1,10)
    draw = ImageDraw.Draw(im)
    draw.text((w-10,0), str(rnum),font = font, fill = 'red')
    im.show()





