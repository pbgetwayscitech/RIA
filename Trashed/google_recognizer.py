import speech_recognition


print("Sarting...")
recognizer = speech_recognition.Recognizer()

done  = False

while not done :
    with speech_recognition.Microphone() as mic :
     try :
        mic.get_pyaudio()
        recognizer.adjust_for_ambient_noise(mic,duration=0.2)
        audio  = recognizer.listen(mic)
        speaking_text = recognizer.recognize_google(audio)
        print("Recognizing .... ")
        print(speaking_text)
     except speech_recognition.UnknownValueError :
        print("Error Occured...")
        recognizer = speech_recognition.Recognizer()
        print("Unknown Error Occured .. .. .. ")