import vosk
import pyaudio
import speech_recognition
from vosk import KaldiRecognizer as kr
import os

current_directory = os.getcwd()
print("Current Dir : "+current_directory)
model_dir = current_directory+"/vosk-model-small-en-us-0.15/"
gigamodel_dir = current_directory+"/vosk-model-en-us-0.42-gigaspeech/"
model_hi_dir = current_directory+"/vosk-model-small-hi-0.22/"
print("Model Dir : "+model_dir)
model = vosk.Model(model_dir)
recognizer = kr(model,16000)

done  = False
islistening = False

mic = pyaudio.PyAudio()
stream = mic.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192)
stream.start_stream()

while not done :
     data  = stream.read(4096, exception_on_overflow= False)
     if(islistening == False):
             print("Listening...")
             islistening = True

     try :
        if recognizer.AcceptWaveform(data):
            speaking_text = recognizer.Result()
            print(" Recoginized : "+f"{speaking_text[14:-3]}")

     except speech_recognition.UnknownValueError :
        print("Error Occured...")

