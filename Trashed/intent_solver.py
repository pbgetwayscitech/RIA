import os
import pyttsx3 as tts
import model as GenericAssistant

# nuralintents as GenericAsistant

working_dir = os.getcwd()
intentspath = working_dir+'\intents.json'
print("Intents Methods :"+intentspath)

assistant  = GenericAssistant.GenericAssistant(intentspath)
print("loading model ...")
assistant.train_model()
print("model trained...")
responce  = assistant.request("Hi")
print("generating responce...")

print(responce)
