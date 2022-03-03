#Marbellys Campos
#Colocas el nombre del pdf y genera en audio

import pyttsx3
import PyPDF2
book = open('Los gatos.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
print(pages)
speaker = pyttsx3.init()
text=''
for i in range(0,pages):
    page = pdfReader.getPage(i)
    text = text + page.extractText()
speaker.say(text)
speaker.runAndWait()