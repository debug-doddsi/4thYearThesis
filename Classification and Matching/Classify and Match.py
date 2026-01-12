"""Classification and Matching"""
# dictate the word that is heard by Sphinx
# find out which list the word belongs to
# name the list that the word has been found under and give it as output

import pandas as pd
import os 
# import statistics
# import numpy as np
import sys
import time


def classify_word(input):
    """Reads data from the training csv file and compares the input word to those lists, tries to find a pair"""
    
    path = r'C:\Users\Iona\Pictures\University\4th Year\BE406- DISSERTATION\Data Collection\Data\ALL DICTIONARIES'
    os.chdir(path)                     # change cwd to the location where the dictionary is stored
    colnames = ['Red', 'Blue', 'Green', 'Yellow', 'Pink', 'Black']
    data = pd.read_csv('everyone no dupes.csv', names=colnames)        
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
        print('ERROR: The number of audio files provided is not equal to the number of Stroop prompts given.')
        print('The program expected', len(inkANS), ' files, instead', len(classification), 'were received.')
        print('Program suspended.')
        sys.exit()
    
    for answer in inkANS:
        if answer == classification[i]:
            score += 1
        i += 1
            
      

classification = []         
# this is the list that I will append all classified words into
# if there is any uncertainty (2+ matches or 0 matches) then the appropriate error will be input into the final list


start_time = time.time()

"""Input User Data Here"""

# Input folder location
source = r'C:\Users\Iona\Pictures\University\4th Year\BE406- DISSERTATION\Data Collection\Data\Iona\Stroop\2s'
os.chdir(source)
path = os.getcwd()

sphinxpath = path + '\Split'
# path1 = the folder containing the csv file which contains words that sphinx believes user has spoken, gibberish
access_elements(sphinxpath)

strooppath = path
# path2 = the data from the Stroop test saved by Python, the expected responses from the subject, solutions
marking(classification, strooppath)


global wrongmatch
wrongmatch = 0


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
        
    elif ans == 'DUPLICATE':
        print(prompt, '  |  ', ans)
    else:
        print(prompt, '  |  ', ans, '(Wrong Match)')
        wrongmatch += 1
    k+=1
print('')



percentage_paired = int((num_paired / (num_paired + num_unpaired)) * 100)
print(percentage_paired,'% of words received were successfully paired to a colour.')
print('')

grade = (score/num_paired)*100
print(grade,'% of the successfully paired words were correct!')
print('')


print('The code took', (time.time()-start_time), 'seconds to complete.')
print('')


print('There were', num_unpaired, 'words which were not matched to a colour:')
if num_unrecognised != 0:
    print(num_unrecognised, 'were unrecognised.')
if num_duplicate != 0:
    print(num_duplicate, 'responses matched multiple colours (duplicates).')
if wrongmatch != 0:
    print(wrongmatch, 'incorrect pairs were made.')














