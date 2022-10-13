from cgitb import text
from importlib.resources import path
import PyPDF2,pyttsx3

path = open('computacionbasico.pdf', 'rb')

pdfReader = PyPDF2.PdfFileReader(path)

speak = pyttsx3.init()

for pages in range(pdfReader.numPages):
    text = pdfReader.getPage(pages).extractText()
    speak.say(text)
    speak.runAndWait()