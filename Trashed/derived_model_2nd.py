import nltk
import json
import random

sen  = "who are you?"

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
    if value == mval :
        mtag = tag

#print(mtag , mval)

replies = []
for intent in intents['intents']:
    if mtag in intent['tag']:
        responses = intent['responses']
        replies.append(responses)


reply  = random.choice(replies[0])
print(reply)
