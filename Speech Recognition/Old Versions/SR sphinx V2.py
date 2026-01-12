# Code Type 1
# Sourced from:
# https://www.pragnakalp.com/speech-recognition-speech-to-text-python-using-google-api-wit-ai-ibm-cmusphinx/
# with modifications to the 'recog' variable to utilise sphinx instead of wit.ai

import os
import speech_recognition as sr

#currently in the current working directory (CWD) that this file is stored in
print(' ')
print("\n", 'Current Working Directory (CWD): ', os.getcwd(),"\n") # tells me where my CWD is right now, where my code is saved
path = r'C:\Users\Iona\Pictures\University\4th Year\BE406- DISSERTATION\Python Code\Speech Recognition\Datasets (speaking colours)\Craig\3 Noise Reduction and Normalised\SPLIT\Blue'
os.chdir(path)      # changes CWD to the folder where my audio clips are stored
print('New Working Directory (CWD): ', os.getcwd(), "\n")

# Build a dictionary so that each prediction of the colour can be added 
colours = {"red": 'red',
        'blue': 'blue',
        'green': 'green',
        'yellow': 'yellow',
        'pink': 'pink',
        'black': 'black'}   # creates an empty dictionary
# I am creating an initial dictionary, telling the code that if it hears red, the answer is red, etc.

# Code sourced from:
# https://thispointer.com/python-how-to-add-append-key-value-pairs-in-dictionary-using-dict-update/#2
def append_value(dict_obj, key, value):
    # # Check if key exist in dict or not
    # if key in dict_obj:
    #     # Key exists in dict.
    #     # Check if type of value of key is list or not
    #     if not isinstance(dict_obj[key], list):
    #         # If type is not list then make it list
    # dict_obj[key] = [dict_obj[key]]
    # Append the value in list
    dict_obj[key].append(value)
    
    #else:
        # As key is not in dict,
        # so, add key-value pair
        #dict_obj[key] = value
        # FIX THIS

entries = os.listdir(path) # navigate to the location of the audio files I'm going to work with
i=1     #counter, shows what number we are at and allows the code to sho
for entry in entries:
    print(entry, ', ', i)      # prints all the names of the files within the specified folder,
    r = sr.Recognizer()
    file = sr.AudioFile(entry)
    with file as source:
        audio = r.record(source)
        recog = r.recognize_sphinx(audio)   # feed the audio clip to sphinx
        print("Sphinx thinks that you said: " + recog)
        print(' ')
        
        # add the word that Sphinx thinks it hears to the dictionary
        if recog not in 'red':   # only add this new word if it is not already featured in the dictionary
            append_value(colours, 'red', recog)
        i += 1  # add one to the counter
        
print('Completed a total of', i, 'enquiries.')
print('The completed dictionary:', colours)













# Code Type 2- too long, when it can be done in 17 lines as above, but keep anyway for reference
# Sourced from:
# https://github.com/nikhilkumarsingh/Wit-Speech-API-Wrapper/blob/master/speech_to_text.py    
    
    
    
# import requests
# import json
# from Recorder import record_audio, read_audio

# # Wit speech API endpoint
# API_ENDPOINT = 'https://api.wit.ai/speech'

# # Wit.ai api access token
# wit_access_token = 'GXBVOD47MRBYSGW6KDASS2MGWWPZNVOY'


# def RecognizeSpeech(AUDIO_FILENAME, num_seconds = 5):
    
#     # reading audio
#     audio = read_audio(AUDIO_FILENAME)
    
#     # defining headers for HTTP request
#     headers = {'authorization': 'Bearer ' + wit_access_token,
#                'Content-Type': 'audio/wav'}

#     # making an HTTP post request
#     resp = requests.post(API_ENDPOINT, headers = headers,
#                          data = audio)
    
#     # converting response content to JSON format
#     data = json.loads(resp.content)
    
#     # get text from data
#     text = data['_text']
    
#     # return the text
#     return text


# if __name__ == "__main__":
#     text =  RecognizeSpeech('single_blue.wav', 4)
#     print("\nYou said: {}".format(text))