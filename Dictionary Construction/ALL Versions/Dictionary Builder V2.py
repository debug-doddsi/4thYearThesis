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
            word = r.recognize_sphinx(audio)                         # feed the audio clip to sphinx
        
            """Build the dictionary"""
            if str(word) not in list:  # if the current word is not already in the currently accessed list
                if str(word) not in (redlist or bluelist or greenlist or yellowlist or pinklist or blacklist):    # if the current word is not in any other list (avoid duplicates)
                    list.append(str(word))              # add the word to the current list
                else:
                    print('Duplicate word encountered in a different list.')
            else:
                print('Duplicate word encountered within the same list.')

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


start_time = time.time()


"""Craig"""
print('Analysing speech by : Craig')
redpath = r'C:\Users\Iona\Pictures\University\4th Year\BE406- DISSERTATION\Python Code\Speech Recognition\Datasets (speaking colours)\Craig\Dictionary Data\#1\3 Noise Reduction and Normalised\SPLIT\Red'
listbuilder(redpath,redlist)

bluepath = r'C:\Users\Iona\Pictures\University\4th Year\BE406- DISSERTATION\Python Code\Speech Recognition\Datasets (speaking colours)\Craig\Dictionary Data\#1\3 Noise Reduction and Normalised\SPLIT\Blue'
listbuilder(bluepath,bluelist)

greenpath = r'C:\Users\Iona\Pictures\University\4th Year\BE406- DISSERTATION\Python Code\Speech Recognition\Datasets (speaking colours)\Craig\Dictionary Data\#1\3 Noise Reduction and Normalised\SPLIT\Green'
listbuilder(greenpath,greenlist)

yellowpath = r'C:\Users\Iona\Pictures\University\4th Year\BE406- DISSERTATION\Python Code\Speech Recognition\Datasets (speaking colours)\Craig\Dictionary Data\#1\3 Noise Reduction and Normalised\SPLIT\Yellow'
listbuilder(yellowpath,yellowlist)

pinkpath = r'C:\Users\Iona\Pictures\University\4th Year\BE406- DISSERTATION\Python Code\Speech Recognition\Datasets (speaking colours)\Craig\Dictionary Data\#1\3 Noise Reduction and Normalised\SPLIT\Pink'
listbuilder(pinkpath,pinklist)

blackpath = r'C:\Users\Iona\Pictures\University\4th Year\BE406- DISSERTATION\Python Code\Speech Recognition\Datasets (speaking colours)\Craig\Dictionary Data\#1\3 Noise Reduction and Normalised\SPLIT\Black'
listbuilder(blackpath,blacklist)


"""Iona, set 1"""
print("\n\n", 'Analysing speech by : Iona (set 1)')
redpath = r'C:\Users\Iona\Pictures\University\4th Year\BE406- DISSERTATION\Python Code\Speech Recognition\Datasets (speaking colours)\Iona\Dictionary Constuction Data\Dictionary Data 1\3 Raw Data Noise Normalised\SPLIT UP\Red'
listbuilder(redpath,redlist)

bluepath = r'C:\Users\Iona\Pictures\University\4th Year\BE406- DISSERTATION\Python Code\Speech Recognition\Datasets (speaking colours)\Iona\Dictionary Constuction Data\Dictionary Data 1\3 Raw Data Noise Normalised\SPLIT UP\Blue'
listbuilder(bluepath,bluelist)

greenpath = r'C:\Users\Iona\Pictures\University\4th Year\BE406- DISSERTATION\Python Code\Speech Recognition\Datasets (speaking colours)\Iona\Dictionary Constuction Data\Dictionary Data 1\3 Raw Data Noise Normalised\SPLIT UP\Green'
listbuilder(greenpath,greenlist)

yellowpath = r'C:\Users\Iona\Pictures\University\4th Year\BE406- DISSERTATION\Python Code\Speech Recognition\Datasets (speaking colours)\Iona\Dictionary Constuction Data\Dictionary Data 1\3 Raw Data Noise Normalised\SPLIT UP\Yellow'
listbuilder(yellowpath,yellowlist)

pinkpath = r'C:\Users\Iona\Pictures\University\4th Year\BE406- DISSERTATION\Python Code\Speech Recognition\Datasets (speaking colours)\Iona\Dictionary Constuction Data\Dictionary Data 1\3 Raw Data Noise Normalised\SPLIT UP\Pink'
listbuilder(pinkpath,pinklist)

blackpath = r'C:\Users\Iona\Pictures\University\4th Year\BE406- DISSERTATION\Python Code\Speech Recognition\Datasets (speaking colours)\Iona\Dictionary Constuction Data\Dictionary Data 1\3 Raw Data Noise Normalised\SPLIT UP\Black'
listbuilder(blackpath,blacklist)


"""Iona, set 2"""
print("\n\n", 'Analysing speech by : Iona (set 2)')
redpath = r'C:\Users\Iona\Pictures\University\4th Year\BE406- DISSERTATION\Python Code\Speech Recognition\Datasets (speaking colours)\Iona\Dictionary Constuction Data\Dictionary Data 2\Noise Reduction + Normalised\cut up\red'
listbuilder(redpath,redlist)

bluepath = r'C:\Users\Iona\Pictures\University\4th Year\BE406- DISSERTATION\Python Code\Speech Recognition\Datasets (speaking colours)\Iona\Dictionary Constuction Data\Dictionary Data 2\Noise Reduction + Normalised\cut up\blue'
listbuilder(bluepath,bluelist)

greenpath = r'C:\Users\Iona\Pictures\University\4th Year\BE406- DISSERTATION\Python Code\Speech Recognition\Datasets (speaking colours)\Iona\Dictionary Constuction Data\Dictionary Data 2\Noise Reduction + Normalised\cut up\green'
listbuilder(greenpath,greenlist)

yellowpath = r'C:\Users\Iona\Pictures\University\4th Year\BE406- DISSERTATION\Python Code\Speech Recognition\Datasets (speaking colours)\Iona\Dictionary Constuction Data\Dictionary Data 2\Noise Reduction + Normalised\cut up\yellow'
listbuilder(yellowpath,yellowlist)

pinkpath = r'C:\Users\Iona\Pictures\University\4th Year\BE406- DISSERTATION\Python Code\Speech Recognition\Datasets (speaking colours)\Iona\Dictionary Constuction Data\Dictionary Data 2\Noise Reduction + Normalised\cut up\pink'
listbuilder(pinkpath,pinklist)

blackpath = r'C:\Users\Iona\Pictures\University\4th Year\BE406- DISSERTATION\Python Code\Speech Recognition\Datasets (speaking colours)\Iona\Dictionary Constuction Data\Dictionary Data 2\Noise Reduction + Normalised\cut up\black'
listbuilder(blackpath,blacklist)


"""Iona, set 3"""
print("\n\n", 'Analysing speech by : Iona (set 3)')
redpath = r'C:\Users\Iona\Pictures\University\4th Year\BE406- DISSERTATION\Python Code\Speech Recognition\Datasets (speaking colours)\Iona\Dictionary Constuction Data\Dictionary Data 3\Noisered + norm\cut up\red'
listbuilder(redpath,redlist)

bluepath = r'C:\Users\Iona\Pictures\University\4th Year\BE406- DISSERTATION\Python Code\Speech Recognition\Datasets (speaking colours)\Iona\Dictionary Constuction Data\Dictionary Data 3\Noisered + norm\cut up\blue'
listbuilder(bluepath,bluelist)

greenpath = r'C:\Users\Iona\Pictures\University\4th Year\BE406- DISSERTATION\Python Code\Speech Recognition\Datasets (speaking colours)\Iona\Dictionary Constuction Data\Dictionary Data 3\Noisered + norm\cut up\green'
listbuilder(greenpath,greenlist)

yellowpath = r'C:\Users\Iona\Pictures\University\4th Year\BE406- DISSERTATION\Python Code\Speech Recognition\Datasets (speaking colours)\Iona\Dictionary Constuction Data\Dictionary Data 3\Noisered + norm\cut up\yellow'
listbuilder(yellowpath,yellowlist)

pinkpath = r'C:\Users\Iona\Pictures\University\4th Year\BE406- DISSERTATION\Python Code\Speech Recognition\Datasets (speaking colours)\Iona\Dictionary Constuction Data\Dictionary Data 3\Noisered + norm\cut up\pink'
listbuilder(pinkpath,pinklist)

blackpath = r'C:\Users\Iona\Pictures\University\4th Year\BE406- DISSERTATION\Python Code\Speech Recognition\Datasets (speaking colours)\Iona\Dictionary Constuction Data\Dictionary Data 3\Noisered + norm\cut up\black'
listbuilder(blackpath,blacklist)


"""Iona, set 4"""
print("\n\n", 'Analysing speech by : Iona (set 4)')
redpath = r'C:\Users\Iona\Pictures\University\4th Year\BE406- DISSERTATION\Python Code\Speech Recognition\Datasets (speaking colours)\Iona\Dictionary Constuction Data\Dictionary Data 4\Noise Reduced + Norm\Cut Up\Red'
listbuilder(redpath,redlist)

bluepath = r'C:\Users\Iona\Pictures\University\4th Year\BE406- DISSERTATION\Python Code\Speech Recognition\Datasets (speaking colours)\Iona\Dictionary Constuction Data\Dictionary Data 4\Noise Reduced + Norm\Cut Up\Blue'
listbuilder(bluepath,bluelist)

greenpath = r'C:\Users\Iona\Pictures\University\4th Year\BE406- DISSERTATION\Python Code\Speech Recognition\Datasets (speaking colours)\Iona\Dictionary Constuction Data\Dictionary Data 4\Noise Reduced + Norm\Cut Up\Green'
listbuilder(greenpath,greenlist)

yellowpath = r'C:\Users\Iona\Pictures\University\4th Year\BE406- DISSERTATION\Python Code\Speech Recognition\Datasets (speaking colours)\Iona\Dictionary Constuction Data\Dictionary Data 4\Noise Reduced + Norm\Cut Up\Yellow'
listbuilder(yellowpath,yellowlist)

pinkpath = r'C:\Users\Iona\Pictures\University\4th Year\BE406- DISSERTATION\Python Code\Speech Recognition\Datasets (speaking colours)\Iona\Dictionary Constuction Data\Dictionary Data 4\Noise Reduced + Norm\Cut Up\Pink'
listbuilder(pinkpath,pinklist)

blackpath = r'C:\Users\Iona\Pictures\University\4th Year\BE406- DISSERTATION\Python Code\Speech Recognition\Datasets (speaking colours)\Iona\Dictionary Constuction Data\Dictionary Data 4\Noise Reduced + Norm\Cut Up\Black'
listbuilder(blackpath,blacklist)




"""Construct a dictionary and export to an excel / csv file"""
print("\n\n", 'Constructing dictionary...')

# You can add a blank item to list A, and then export it using pandas. 
# Pandas uses a data structure called a DataFrame, but the columns must be equal length. 
# The output .csv file will not show the blank data cell.
destination = r'C:\Users\Iona\Pictures\University\4th Year\BE406- DISSERTATION\Python Code\Dictionary Construction'
os.chdir(destination)

df1 = pd.DataFrame({'Red':redlist})
df2 = pd.DataFrame({'Blue':bluelist})
df3 = pd.DataFrame({'Green':greenlist})
df4 = pd.DataFrame({'Yellow':yellowlist})
df5 = pd.DataFrame({'Pink':pinklist})
df6 = pd.DataFrame({'Black':blacklist})

pd.concat([df1,df2, df3, df4, df5, df6],axis=1).to_csv('Dictionary.csv', index = False)

frequency = 1000                        # Set Frequency To 1600 Hertz
duration  = 500                         # Set Duration To 500 ms == 0.5 second
winsound.Beep(frequency, duration)      # Produce a beep to signify completion of the code
print("\n\n", 'Processing Complete. Please observe the Excel file with your data.')
print('The code took', (time.time()-start_time)/60, 'minutes to complete.')





