__author__ = 'huke'
import os
codelines=0
commentlines=0
blankline=0
def countCode(path):
    global commentlines,codelines,blankline
    fp=open(path,'r')
    while True:
        line=fp.readline()
        if not line:
            print("End of file")
            break
        elif line.strip( ).startswith('#'):
            commentlines +=1
        elif line.strip( ):
            codelines +=1
        else:
            blankline +=1


countCode('issue1.py')
print("code line:%d comment line:%d empty line:%d"%(codelines,commentlines,blankline))


