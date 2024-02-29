#imports
from gtts import gTTS
import os
from googletrans import Translator
import speech_recognition as s


#translate to hindi
def translate_to_hindi(text):
    translator=Translator()
    translated_text=translator.translate(text,dest='bn').text
    return translated_text
    
    
    

#speech recognize
sr=s.Recognizer()
print("HI i am here to listen you ...")


with s.Microphone() as m:
    audio =sr.listen(m)
    query=sr.recognize_google(audio, language='en-IN')
    print("audio-",query)


#save to file
with open("query.txt","w") as file:
    file.write(query)
    print("query is saved")




#save to audio
with open("query.txt","r") as file:
    english_text=file.read()
    
hindi_text=translate_to_hindi(english_text)
print(hindi_text)



#speak 
tts=gTTS(text=hindi_text, lang='hi')
tts.save("output.mp3")

os.system("start output.mp3") 
print("finish usecase")
 
 
