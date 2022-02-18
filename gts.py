#importing the necessary modules
from gtts import gTTS
from playsound import playsound
import pytesseract
from PIL import Image
#converting image to text
def imagetoText(img):
    value = Image.open(img)
    text = pytesseract.image_to_string(value,config='')
    print(text)
    texttoAudio(text)
#converting the text to speech
def texttoAudio(para):
    language = 'en'
    speech = gTTS(text = str(para),lang = language,slow = False)
    speech.save('voice.mp3')
    playsound('voice.mp3')

#Input Image
imagetoText('maxwell.png')
