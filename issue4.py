__author__ = 'huke'
import nltk

#nltk.download()
#nltk.download('punkt')

if __name__ == "__main__":
    f=open(r"eng.txt","r")
    tok=nltk.word_tokenize( f.read())
    fdisk=nltk.FreqDist(tok)
    #for key in fdisk:
    #    print(key,fdisk[key])
    fdisk.plot()


