"""Save words spoken to an excel file to create a dictionary for my Stroop Test"""
# This listens to the repeated cut-up words  for each of the 6 colours andturns speech into text
# It creates a list of gibberish associated with each colour and stores it in a csv file
# Used for traiing purposes ONLY, not for use in actual Stroop test
# PREPARATORY PURPOSES ONLY


# Created a SR function
# SR interprets what is being said
# Code adds the word to a list if it is not already in list
# The list is turned into a dictionary using pandas datafile
# The dictionaries are stored together in csv file

import os
import speech_recognition as sr
import pandas as pd
import time
import winsound


"""Speech Recognition"""
def listbuilder(path, list):
    os.chdir(path)                  # changes CWD to the folder where my audio clips are stored
    entries = os.listdir(path)      # navigate to the location of the audio files I'm going to work with
    i=1                             # counter, shows what number we are at
    print("\n", 'Analysing speech of the word', list[0], '...')
    for entry in entries:           # for each wav file in the folder ...
        print(entry, ', ', i)       # print the name of the wav file being interpreted and the iteration 
        r = sr.Recognizer()         # initialize the SR
        file = sr.AudioFile(entry)
        with file as source:
            audio = r.record(source)
            word =  r.recognize_wit(audio, key = "GXBVOD47MRBYSGW6KDASS2MGWWPZNVOY")                         # feed the audio clip to sphinx
        
            """Build the dictionary"""
            if str(word) not in allwords:           # if the current word is not in any other list (avoid duplicates)
                list.append(str(word))              # add the word to the current list
                allwords.append(str(word))
            else:
                print('Duplicate word encountered. It has not been added to the dictionary.')

            i += 1  # add one to the counter
        
    # print("\n", 'Completed a total of', i, 'enquiries.')
    # print('The completed list:',"\n", list)
    frequency = 2000                        # Set Frequency To 1600 Hertz
    duration  = 500                         # Set Duration To 500 ms == 0.5 second
    winsound.Beep(frequency, duration)      # Produce a beep to signify completion of the code
    print('Complete!')


"""Lists of the different words to be associated with each colour"""
redlist    = ['red']
bluelist   = ['blue']
greenlist  = ['green']
yellowlist = ['yellow']
pinklist   = ['pink']
blacklist  = ['black']

global allwords
allwords = ['red', 'blue', 'green', 'yellow', 'pink', 'black']           
# this list will hold ALL words that are added to the dictionary
# it will serve 2 purposes: to count the total number of words in the dictionary AND prevent duplicate words from being added



start_time = time.time()

"""INPUT SAVE DESTINATION WHERE THE COMPLETED DICTIONARY WILL BE STORED !!!!!"""
destination = r'C:\Users\Iona\Pictures\University\4th Year\BE406- DISSERTATION\Data Collection\Data\NB84D\Training\Dictionaries\Wit Dict'


# Input the Folder location where all th eusb folders containing split up words are stored (access individual folders below)
source = r'C:\Users\Iona\Pictures\University\4th Year\BE406- DISSERTATION\Data Collection\Data\NB84D\Training\Noise Reduced & Normalised\Split'
os.chdir(source)
path = os.getcwd()

redpath = path + '\Red'
listbuilder(redpath,redlist)
bluepath = path + '\Blue'
listbuilder(bluepath,bluelist)
greenpath = path + '\Green'
listbuilder(greenpath,greenlist)
yellowpath = path + '\Yellow'
listbuilder(yellowpath,yellowlist)
pinkpath = path + '\Pink'
listbuilder(pinkpath,pinklist)
blackpath = path + '\Black'
listbuilder(blackpath,blacklist)






"""Construct a dictionary and export to an excel / csv file"""
print("\n\n", 'Constructing dictionary...')

# You can add a blank item to list A, and then export it using pandas. 
# Pandas uses a data structure called a DataFrame, but the columns must be equal length. 
# The output .csv file will not show the blank data cell.

os.chdir(destination)

df1 = pd.DataFrame({'Red':redlist})
df2 = pd.DataFrame({'Blue':bluelist})
df3 = pd.DataFrame({'Green':greenlist})
df4 = pd.DataFrame({'Yellow':yellowlist})
df5 = pd.DataFrame({'Pink':pinklist})
df6 = pd.DataFrame({'Black':blacklist})

pd.concat([df1,df2, df3, df4, df5, df6],axis=1).to_csv('WITdict_nodupes.csv', index = False)

frequency = 1000                        # Set Frequency To 1600 Hertz
duration  = 500                         # Set Duration To 500 ms == 0.5 second
winsound.Beep(frequency, duration)      # Produce a beep to signify completion of the code
print("\n\n", 'Processing Complete. Please observe the Excel file with your data.')
print('The code took', (time.time()-start_time)/60, 'minutes to complete.')





