import vosk
import os
import pyaudio
import json
import nltk
import random
import time
import pyttsx3 as tts
from enum import Enum
from vosk import KaldiRecognizer as kr
from  Trashed.model import GenericAssistant

current_directory = os.getcwd()
print("Current Dir : "+current_directory)
model_dir = current_directory+"/vosk-model-small-en-us-0.15/"
print("Model Dir : "+model_dir)
model = vosk.Model(model_dir)
recognizer = kr(model,16000)

class state(Enum) :
        Listening  = 0,
        Speaking  = 1,

main_current_state = state.Listening
printing_state  = ()
current_text = ""

mic = pyaudio.PyAudio()
stream = mic.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192)
#stream.start_stream()

istoquit = False

while not istoquit :

     while main_current_state==state.Listening :
          if(printing_state != main_current_state ):
               print(main_current_state.name+"...")
               printing_state = main_current_state

          data = ()
          stream.start_stream()
          data  = stream.read(4096, exception_on_overflow= False) # 4096 #2048
          try :
               if recognizer.AcceptWaveform(data):
                    speaking_text = recognizer.Result()
                    print("Recoginized : "+f"{speaking_text[14:-3]}")
                    formatted_text = f"{speaking_text[14:-3]}"
                    if formatted_text.strip() != "":
                         current_text = f"{speaking_text[14:-3]}"
                         main_current_state = state.Speaking
                         stream.stop_stream()
          except Exception :
               print("Error Occured..."+Exception)


     while main_current_state == state.Speaking :
      if(printing_state != main_current_state ):
          print(main_current_state.name+"...")
          printing_state = main_current_state

          speaker =  tts.init()
          voices = speaker.getProperty('voices')
          speaker.setProperty('voice',voices[1].id)

          sen  = current_text

          words = nltk.tokenize.word_tokenize(sen)
          ignore = ["?","!","@","#","$","%","*","/","&"]


          lower_words  = []
          for word in words:
               lower_words.append(word.lower())


          filtered_words = []
          for lo_word in lower_words :
               if lo_word not in ignore :
                    filtered_words.append(lo_word)

          tags = []
          file  = open("final_intents.json")
          intents = json.load(file)

          for each_word in filtered_words:
               for intent in intents['intents']:
                    for pattern in intent['patterns']:
                         tag = intent['tag']

                    pattern = pattern.lower()

                    if each_word in pattern :
                         tags.append(tag)

          frquency = {}
          for tag in tags:
               if tag in frquency:
                    frquency[tag] += 1
               else:
                    frquency[tag] = 1

          print(frquency)
          mtag = ""
          mval = 0
          for tag,value in frquency.items():
               if value > mval :
                    mval = value

          for tag,value in frquency.items():
               if mval == 1:
                    print("mval is 1")
                    mtag = tag
                    break
               elif value == mval :
                    print("mval is "+str(mval))
                    mtag = tag
                    break

          print(mtag , mval)

          replies = []
          for intent in intents['intents']:
                if mtag in intent['tag']:
                    responses = intent['responses']
                    replies.append(responses)

          reply  = random.choice(replies[0])
          print(reply)

          speaker.say(reply)
          current_text = ""
          speaker.runAndWait()

          #time.sleep(3)

          main_current_state = state.Listening
