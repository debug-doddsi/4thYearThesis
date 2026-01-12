"""Speech Recogniser"""
# This code takes the chopped-up audio files OF AN ACTUAL STROOP TEST and turns them into a list
# This list is then exported to a csv file for access elsewhere
# It does not make dictionaries and it is not used for training
# SOMETIMES GENERATES AN ERROR IF THERE IS ALREADY AN EXCEL DOCUMENT IN THE FOLDER

import os
import pandas as pd
import speech_recognition as sr
import time



"""Speech Recognition, Speech-To-Text (STT)"""
def STT(path, list):
    os.chdir(path)                  # changes CWD to the folder where my audio clips are stored
    entries = os.listdir(path)      # navigate to the location of the audio files I'm going to work with
    global i
    i=0                             # counter, shows what number we are at
    print("\n", 'Analysing speech...')
    for entry in entries:           # for each wav file in the folder ...
        r = sr.Recognizer()         # initialize the SR
        file = sr.AudioFile(entry)
        with file as source:
            audio = r.record(source)
            recog = r.recognize_wit(audio, key = "GXBVOD47MRBYSGW6KDASS2MGWWPZNVOY")                         # feed the audio clip to sphinx
            i += 1  # add one to the counter
            print(i)
            print("Wit.ai thinks that you said: " + recog + "\n")   # output to console what Sphinx thinks it heard
            list.append(str(recog))         # even if there are duplicates in what is detected, we want to see every word!
           
        
    print("\n", 'Completed a total of', i, 'enquiries.')
    print('The completed list:',"\n", list)
    
    print('Complete!')
    
"""Provide the folder in which the noise reduced, normalised, chopped audio files are stored"""
start_time = time.time()

# Where is the data that you want to interpret?
path = r'C:\Users\Iona\Pictures\University\4th Year\BE406- DISSERTATION\Data Collection\Data\Iona\Training\Noise Reduced & Normalised\Split\blue'

speech = []      # speech that sphinxs believes it has heard from the participant
STT(path,speech)
 # Save the interpreted words to a csv file inside the same folder as the cut up audio
df = pd.DataFrame(speech)
df.to_csv('WIT_StroopWords.csv', index=False)

print('The code took', (time.time()-start_time), 'seconds to complete.')

