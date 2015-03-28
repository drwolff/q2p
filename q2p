from nltk import tokenize
import nltk.data
from wand.image import Image
from wand.drawing import Drawing

n = 2
f = open('tesla.txt').read()
sent_detector = nltk.data.load('tokenizers/punkt/english.pickle')
#print ('\n \n'.join(sent_detector.tokenize(f.strip())))
for x in sent_detector.tokenize(f.strip()):
    with Image(filename='1.jpg') as img:
        with Drawing() as draw:
            draw.font = 'C:\Windows\Fonts\BRUSHSCI.TTF'
            draw.font_size = 100
            draw.text(100, 150, x)
            draw(img)
        temp = str(n)+ ('.jpg')
        img.save(filename=temp)
        n += 1
        
