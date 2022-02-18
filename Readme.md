# Converting embedded Text from an Image to Speech.
### What does this project do?
This project reads an image which consists of text using the [_pytesseract_] module. This text is converted from text to speech using [_gTTS (Google Text-to-Speech)_] .
### Installing Libraries
Install [pip], if not installed.

Installing gtts module\
` pip install gTTS`

Installing playsound module\
`pip install playsound `

Installing pytesseract module\
`pip install pytesseract`

Installing PIL module\
`pip install PIL`

### Input
Maxwell.png is given as input, manually.

### Working
After reading the text from the given input image (maxwell.png). The text is converted into an audio file named `voice.mp3` and saved in your current working directory. And this file is used for Speech.



[//]: #Links
[_pytesseract_]:<https://pypi.org/project/pytesseract/>
[_gTTS (Google Text-to-Speech)_]:<https://pypi.org/project/gTTS/>
[pip]:<https://pip.pypa.io/en/stable/installation/>
