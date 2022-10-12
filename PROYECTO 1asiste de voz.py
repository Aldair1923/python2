from distutils.cmd import Command
from email.mime import audio
from time import time
from unittest import SkipTest
import pyttsx3 as voz
import speech_recognition as sr
import subprocess as sub
from datetime import datetime

#configuracion de la voz asistente
voice=voz.init()
voices=voice.getProperty('voices')
voice.setProperty('voice' ,voices[0].id)
voice.setProperty('rate' ,140)

def say(text):
    voice.say(text)
    voice.runAnWait()

while True:
    recognizer= sr.Recognizer()
# Activar el microfono
    with sr.Microphone() as source:
        print('Escuchando...')
        audio=recognizer.listen(source, phrase_time_limit=3)

    try: # Si se entiende nuestra peticion entramos a la logica principal
        Comando=recognizer.recognize_google(audio, language='es-MX')
        print('creo que dijiste "{comando}"')

        Comando=Comando.lower()
        Comando=Comando.split('')

        if 'computadora' in Comando:
            if 'abre' in Comando or 'abrir' in Comando:

                sites={
                    'google':'google.com',
                    'youtube':'youtube.com',
                    'instagram':'instragram.com',
                }

                for i in list(sites.keys()):
                    if i in Comando:
                        sub.call(f'star brave.exe {sites[i]}', shell=True)
                        say(f'Abriendo {i}')

            elif'hora' in Comando:
                time=datetime.now().strftime('%H:%H')
                say(f'Son las{time}')

            for i in ['temina','terminar','término']:
                if i in Comando:
                    say('Sesión finalaizada')
                    break

    except:# Si no se entiende nos dara este mensaje
        print('No entendi, por favor vuelva a intertarlo')                    