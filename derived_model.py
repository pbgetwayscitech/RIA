import random
import json
import tensorflow as tf
import numpy as np 
import os
import nltk



working_directory = os.getcwd()
word  = "who you"
matachable_array = []

def inintialise():
    print("intialiseing...")

    file  = open("final_intents.json")
    intents = json.load(file)

    # print(inetnts)

    for intent in intents['intents']:
        for pattern in intent['patterns']:
            tag = intent['tag']

            pattern = pattern.lower()

            #print(pattern)

            if word.lower() in pattern:
                # print(pattern , tag)
                matachable_array.append(tag) # pattern + tag
            else:{}
               # print("Nothing Found in Model")
    
    #print(matachable_array)
    speable_tag = matachable_array[0]
    #print(speable_tag)

    replies = []

    for intent in intents['intents']:
        if speable_tag in intent['tag']:
            responses = intent['responses']
            replies.append(responses)

    print(replies)

    length_replies  = len(replies[0])
    if length_replies>0 :

        print(length_replies)

        rand_pos = random.randint(0,length_replies-1)
        reply  = replies[0][rand_pos]

        print(reply)

inintialise()