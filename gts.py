from gtts import gTTS
from playsound import playsound
import pytesseract
from PIL import Image
def i2t(img,usrInput):
    value = Image.open(img)
    text = pytesseract.image_to_string(value,config='')
    print(text)
    if usrInput ==1:
        aud(text)
def aud(para):
    #file = open('file.txt','r').read().replace('\n','')
    language = 'en'
    speech = gTTS(text = str(para),lang = language,slow = False)
    speech.save('voice.mp3')
    playsound('voice.mp3')

usrInput =int(input('For text give 0,for audio give 1\n'))
i2t('maxwell.png',usrInput)