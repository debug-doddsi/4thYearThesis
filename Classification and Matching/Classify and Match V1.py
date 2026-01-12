"""Classification and Matching"""
# dictate the word that is heard by Sphinx
# find out which list the word belongs to
# name the list that the word has been found under and give it as output

import pandas as pd
import os 
import statistics
import numpy as np
import sys
import time


def classify_word(input):
    """Reads data from the training csv file and compares the input word to those lists, tries to find a pair"""
    
    path = r'C:\Users\Iona\Pictures\University\4th Year\BE406- DISSERTATION\Data Collection\Data\Guillermo V\Training'
    os.chdir(path)                     # change cwd to the location where the dictionary is stored
    colnames = ['Red', 'Blue', 'Green', 'Yellow', 'Pink', 'Black']
    data = pd.read_csv('Unique Dict (NO dupes).csv', names=colnames)        
    match = []  # create an empty list to store potential matches in, will show if there is one, or multiple matches
    
    """Turn the data into lists"""
    # Note: the first element [1] of each list is the correct word
    # ie, reddata[0] = 'red', bluedata[0] = 'blue' ... append the first element to the match list
    reddata = data.Red.tolist()
    bluedata = data.Blue.tolist()
    greendata = data.Green.tolist()
    yellowdata = data.Yellow.tolist()
    pinkdata = data.Pink.tolist()
    blackdata = data.Black.tolist()
    

    
    """If the input word is featured in the training dictionary, add it to the match list"""
    # Ideally there will only be one match, but if there are multiple matches we can see all which apply in the match list
    if input in reddata:
        match.append(reddata[0])
    if input in bluedata:
        match.append(bluedata[0])
    if input in greendata:
        match.append(greendata[0])
    if input in yellowdata:
        match.append(yellowdata[0])
    if input in pinkdata:
        match.append(pinkdata[0])
    if input in blackdata:
        match.append(blackdata[0])   
    
    """Present the findings"""
    # print(input)
    # print('matches:', match)
    
    global paired
    paired = 0
    global unpaired
    unpaired = 0
    global unrecognised
    unrecognised = 0
    global duplicate
    duplicate = 0
    
    
    # There is one correct match
    if len(match) == 1:             
        classification.append(match[0])
        paired +=1
    
    # There are 2+ matches (same word in 2+ lists?), therefore we are unsure which word was actually spoken, ERROR
    elif len(match) > 1:           
        error1= 'DUPLICATE'           # add to the output to hold space AND also indicate what the problem was
        classification.append(error1)
        unpaired += 1
        duplicate += 1
    
    # There are 0 matches, an unrecognised word / a word that was not registered in the training dictionary has been received, ERROR
    elif len(match) == 0:           
        error2= 'UNRECOGNISED'      # add to the output to hold space AND also indicate what the problem was
        classification.append(error2)
        unpaired += 1
        unrecognised += 1
    




def access_elements(path):
    """Accesses csv file within a specified destination folder, extracts each word individually"""
    
    os.chdir(path)                                          # changes CWD to the folder where audio clips are stored
    column= ["Stroop"]                                      # the header of what we are looking for
    df = pd.read_csv("StroopWords.csv", names=column)       # extract the data
    speech = df.Stroop.to_list()                            # transform it into a useable form, a list
    # print(speech, ',', len(speech))
    del speech[0]                                           # remove the 0 which occupies the first element, it is not part of our data and it offsets our classification code
    # print(speech, ',', len(speech))
    # print('Speech:', speech)
    
    global num_paired
    num_paired = 0 
    global num_unpaired
    num_unpaired = 0 
    
    global num_unrecognised
    num_unrecognised = 0
    global num_duplicate
    num_duplicate = 0
    
    
    print('')
    print('Analysing speech...')
    for eachword in speech:                                 # accesses each file in the folder one by one ...
        classify_word(eachword)                             # sends each file to the classify function
        
        num_paired = num_paired + paired
        num_unpaired = num_unpaired + unpaired
        
        num_unrecognised = num_unrecognised + unrecognised
        num_duplicate = num_duplicate + duplicate
        
        
        
def marking(classification, path):
    """Accesses csv file of the REAL info from the Stroop test and marks the classified responses"""
    
    os.chdir(path)                     # change cwd to the location where the dictionary is stored
    colnames = ['Ink', 'Word', 'Time']
    data = pd.read_csv('StroopData.csv', names=colnames)        
    global inkANS
    inkANS = data.Ink.tolist()          # This is what I am marking against
    # print(inkANS)
    del inkANS[0]                       # Removes the first word, 'Ink', from the list, this is the header of the data column, not part of the data we want
    global score
    score = 0                           # Initially 0
    i = 0                               # Counter
    # print('len ink answers:', len(inkANS))
    # print('len responses:', len(classification))
    
    if len(inkANS) != len(classification):
        print('ERROR: The number of audio files provided is not equal to the number of Stroop prompts given. Code suspended.')
        sys.exit()
    
    for answer in inkANS:
        if answer == classification[i]:
            score += 1
        i += 1
    
    
    
    
def presentation_time(path):
       """Extract the presentation times from the ACTUAL DATA file, turn it from perfcounter data to actual, usable data"""
       os.chdir(path)
       colnames = ['Ink', 'Word', 'Time']
       data = pd.read_csv('StroopData.csv', names=colnames)  
       timing = data.Time.tolist()                   # extract the perftimer data ONLY
       del timing[0]                                 # delete the first value 'time', it is not actual data
       global presentation_timestamps
       presentation_timestamps=[]                    # store the time data here
       i = 0
       for element in timing:
           time = round(((float(timing[i])) - (float(timing[0]))),3)   # the difference between each perfcounter value is more useful than the raw perfcounter data
           presentation_timestamps.append(time)
           i += 1
       # print(presentation_timestamps)
       global deltaT
       deltaT = np.diff(presentation_timestamps)                        # find the difference between each element in the list
       # print(deltaT)




def subject_elapsed_time(path):
      """The time elapsed from 'start' at the beginning of each word, as detected by the split-up-audio code and saved in the .wav files"""
      filenames = os.listdir(path)                                  # access the original cut-up .wav files, the file names contain the 'trigger time', the time at which thr word was beginning to be spoken
      del filenames[0]                                              # delete the first element, this is a csv file which stores other data we do not need right now
      strList = map( str, filenames)                                # turn it into a map for ease of manipulation
      strList = map( lambda x: x.replace( 'stroop_', ''), strList)  # remove the 'stroop_' prefix
      strList = map( lambda x: x.replace( '.wav', ''), strList)     # remove the '.wav' suffix
      filenames = list(strList)                                     # left only with timings 
      filenames = list(map(int, filenames))                         # maps it into integer format (ms)
      global elapsedtime
      elapsedtime =[]                                               # create an empty list to store time in 
      for element in filenames:
          elapsedtime.append(element / 1000)                        # divide each element by 1e3 to transform from milliseconds to seconds
      # print(elapsedtime)
      
      
      
      
def reaction_time():
    # elapsedtime and presentation_timestamps are both global variables I can access inside this function
    global timediff
    timediff =[]    # create empty list to store times in
    i = 0
    for times in elapsedtime:
        diff = round((float(elapsedtime[i]) - float(presentation_timestamps[i])),3)
        timediff.append(diff)
        i += 1
        
      

classification = []         
# this is the list that I will append all classified words into
# if there is any uncertainty (2+ matches or 0 matches) then the appropriate error will be input into the final list


start_time = time.time()

"""Input User Data Here"""
# Input Sphinx-interpreted csv file
path1 = r'C:\Users\Iona\Pictures\University\4th Year\BE406- DISSERTATION\Data Collection\Data\Guillermo V\Stroop\2s\Split'   
# path1 = the folder containing the csv file which contains words that sphinx believes user has spoken, gibberish
subject_elapsed_time(path1)
access_elements(path1)

path2 = r'C:\Users\Iona\Pictures\University\4th Year\BE406- DISSERTATION\Data Collection\Data\Guillermo V\Stroop\2s'
# path2 = the data from the Stroop test saved by Python, the expected responses from the subject, solutions
marking(classification, path2)
presentation_time(path2)

global wrongmatch
wrongmatch = 0

reaction_time()

"""Show what the classification process has achieved"""
print('')
# print('The Stroop Test presented the following ink colours to you:')
#print(inkANS)
k=0
print('You were Shown  |  Your Interpreted Response')
for each in inkANS:
    prompt = inkANS[k]
    ans = classification[k]
    if prompt == ans:
        print(prompt, '  |  ', ans)
    elif ans == 'UNRECOGNISED':
        print(prompt, '  |  ', ans)
    else:
        print(prompt, '  |  ', ans, '(Wrong Match)')
        wrongmatch += 1
    k+=1
print('')

# print('')
# print('Your responses to the Stroop Test were classified as follows:')
# print(classification)
# print('')

percentage_correct = int((num_paired / (num_paired + num_unpaired)) * 100)
print(percentage_correct,'% of words received were successfully paired to a colour.')
print('')

grade = (score/num_paired)*100
print(grade,'% of the successfully paired words were correct!')
print('')

# avgtime= round(statistics.mean(deltaT),3)
# print('The average time between word presentation was:', avgtime, 's.')
# print('')

# print('The elapsed time at the start of each word spoken by the subject:', elapsedtime)
# print('')

# print('The elapsed time when each Colour-Word pair was presented to the subject:', presentation_timestamps)    
# print('')

# print('The subjects reaction times are as follows:', timediff)
# print('')

# avgreaction= round(statistics.mean(timediff),3)
# print('The subjects average reaction time was:', avgreaction)
# print('')

# print('The code took', (time.time()-start_time), 'seconds to complete.')
# print('')


print('There were', num_unpaired, 'words which were not matched to a colour:')
if num_unrecognised != 0:
    print(num_unrecognised, 'were unrecognised.')
if num_duplicate != 0:
    print(num_duplicate, 'responses matched multiple colours (duplicates).')
if wrongmatch != 0:
    print(wrongmatch, 'incorrect pairs were made (poor training?)')














