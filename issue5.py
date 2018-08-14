__author__ = 'huke'
from PIL import Image
import os
cur=os.getcwd()
#files= os.listdir('pic')
pic_path=os.path.join(cur,'pic')
#for im in
files=os.listdir(pic_path)
ip5size=(300,500)
for img in files:
    nimg=Image.open(os.path.join(pic_path,img))
    nimg=nimg.resize(ip5size)
    nimg.show()
    #print(nimg.size)
