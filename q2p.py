from nltk import tokenize
import nltk.data
from wand.image import Image
from wand.font import Font

n = 2
f = open('tesla.txt').read()
sent_detector = nltk.data.load('tokenizers/punkt/english.pickle')

for x in sent_detector.tokenize(f.strip()):
    with Image(filename='1.jpg') as img:
        font=Font(
            path=('C:\Windows\Fonts\BRUSHSCI.TTF'),
            size=60)
        img.caption(x,100,50,1300,500,font,gravity='west')
        temp = str(n)+ ('.jpg')
        img.save(filename=temp)
        n += 1
