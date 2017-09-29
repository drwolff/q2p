from nltk import tokenize
import nltk.data
from wand.image import Image
from wand.font import Font

n = 2
i = open('file.txt').read()
sent_detector = nltk.data.load('tokenizers/punkt/english.pickle')
for x in sent_detector.tokenize(i.strip()):
    with Image(filename='1.jpg') as img:
        font=Font(
            path=('C:\Windows\Fonts\BRUSHSCI.TTF'),
            size=60)      
        img.caption(x,50,50,1300,500,font,gravity='north_west')
        temp = str(n)+ ('.jpg')
        img.save(filename=temp)
        n += 1
