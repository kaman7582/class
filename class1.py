from random import *
__author__ = 'huke'

def duplicate_encode(word):
    dic={}
    tlst=['(',')']
    outstr=""

    for var in word:
        if(dic.__contains__(var) == False):
            dic[var]=1
        else:
            dic[var] +=1

    for var in word:
        if(dic[var] == 1):
            outstr += tlst[0]
        else:
            outstr += tlst[1]
    print(outstr)

    return

if __name__ == "__main__":
    num = randrange(1,20)
    print("class one %d"%num)
    dic = {'a':[1,2,3,4,5]}
    dd=[]
    dd=dic['a']
    dd.append(7)
    print(dd)
    duplicate_encode('hello')
