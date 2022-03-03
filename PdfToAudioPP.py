#Marbellys Campos
#Colocas el nro de pagina del pdf y genera el audio

import pyttsx3
import PyPDF2
book = open('Los gatos.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
print(pages)
speaker = pyttsx3.init()
page = pdfReader.getPage(1)
text = page.extractText()
speaker.say(text)
speaker.runAndWait()