"""Save words spoken to an excel file to create a dictionary for my Stroop Test"""

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
            print('Sphinx heard:', word)
            """Build the dictionary"""
            if str(word) not in list:               # if the current word is not in any other list (avoid duplicates)
                list.append(str(word))              # add the word to the current list

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

"""INPUT SAVE DESTINATION WHERE THE COMPLETED DICTIONARY WILL BE STORED !!!!!"""
destination = r'C:\Users\Iona\Pictures\University\4th Year\BE406- DISSERTATION\Data Collection\Data\ALL DICTIONARIES'

""" 1 MOGX3 Training Data"""
# Input the Folder location where all the sub folders containing split up words are stored (access individual folders below)
source = r'C:\Users\Iona\Pictures\University\4th Year\BE406- DISSERTATION\Data Collection\Data\MOGX3\Training\Normalised + Noisered\Split'
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


""" 2 NB84D Training Data"""
# Input the Folder location where all the sub folders containing split up words are stored (access individual folders below)
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


""" 3 HJB4F Training Data"""
# Input the Folder location where all the sub folders containing split up words are stored (access individual folders below)
source = r'C:\Users\Iona\Pictures\University\4th Year\BE406- DISSERTATION\Data Collection\Data\HJB4F\Training\Noise Reduced & Normalised\Split'
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



""" 4 P65DG Training Data"""
# Input the Folder location where all the sub folders containing split up words are stored (access individual folders below)
source = r'C:\Users\Iona\Pictures\University\4th Year\BE406- DISSERTATION\Data Collection\Data\P65DG\Training\Normalised + Noisered\Split'
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



""" 5 TJ47B Training Data"""
# Input the Folder location where all the sub folders containing split up words are stored (access individual folders below)
source = r'C:\Users\Iona\Pictures\University\4th Year\BE406- DISSERTATION\Data Collection\Data\TJ47B\Training\Normalised + Noisered\Split'
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


""" 6 GD6K3 Training Data"""
# Input the Folder location where all the sub folders containing split up words are stored (access individual folders below)
source = r'C:\Users\Iona\Pictures\University\4th Year\BE406- DISSERTATION\Data Collection\Data\GD6K3\Training\Noise Reduced & Normalised\Split'
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


""" 7 JN7JK Training Data"""
# Input the Folder location where all the sub folders containing split up words are stored (access individual folders below)
source = r'C:\Users\Iona\Pictures\University\4th Year\BE406- DISSERTATION\Data Collection\Data\JN7JK\Training Data\Noisered + Norm\Split'
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



""" 8 S5BLO Training Data"""
# Input the Folder location where all the sub folders containing split up words are stored (access individual folders below)
source = r'C:\Users\Iona\Pictures\University\4th Year\BE406- DISSERTATION\Data Collection\Data\S5BLO\Training Data\Noisered + Norm\Split'
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


""" 9 FIBF5 Training Data"""
# Input the Folder location where all the sub folders containing split up words are stored (access individual folders below)
source = r'C:\Users\Iona\Pictures\University\4th Year\BE406- DISSERTATION\Data Collection\Data\FIBF5\Training'
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


""" 10 K4GKU Training Data"""
# Input the Folder location where all the sub folders containing split up words are stored (access individual folders below)
source = r'C:\Users\Iona\Pictures\University\4th Year\BE406- DISSERTATION\Data Collection\Data\K4GKU\ALL Training'
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


""" 11 A5GJP Training Data"""
# Input the Folder location where all the sub folders containing split up words are stored (access individual folders below)
source = r'C:\Users\Iona\Pictures\University\4th Year\BE406- DISSERTATION\Data Collection\Data\A5GJP\Training\Noise Reduced & Normalised\Split'
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

pd.concat([df1,df2, df3, df4, df5, df6],axis=1).to_csv('Dictionary.csv', index = False)

frequency = 1000                        # Set Frequency To 1600 Hertz
duration  = 500                         # Set Duration To 500 ms == 0.5 second
winsound.Beep(frequency, duration)      # Produce a beep to signify completion of the code
print("\n\n", 'Processing Complete. Please observe the Excel file with your data.')
print('The code took', (time.time()-start_time)/60, 'minutes to complete.')





