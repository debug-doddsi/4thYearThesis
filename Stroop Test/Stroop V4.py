"""Stroop Test V4"""
# Random CW pairs, no duplicates
# I have extracted and stored the ink, word and time and put it into a table-like format.
# I have implemented a beep when I press the button to start the code.

# Sourced from:
# https://stackoverflow.com/questions/36255642/stroop-test-in-python-not-working-properly
# 28/1/2021
# https://www.python-course.eu/tkinter_labels.php
# 28/1/2021
# https://python-forum.io/Thread-How-to-get-RGB-colors-in-tkinter
# 28/1/2021

"""Transform RGB into HEX"""
# def rgb_color(rgb):
#     return '#%02x%02x%02x' % rgb
# print(rgb_color((0, 255, 0)))

import tkinter  
import random
import time
import winsound


"""Summary of the words and ink colours I will be using"""
COLOURtxt = [ 'RED',      'GREEN',   'BLUE',   'YELLOW',  'PINK',   'BLACK']
COLOURhex = ['#ff0000', '#00ff00', '#0000ff', '#ffee00', '#ff00ff', '#000000']  # colours of the ink in HEX, representing RBG colours

inkHISTORY   = [] # Create an empty list which we shall store the ink colours in, which is what we want the subjects to be speaking
wordHISTORY  = []
timeHISTORY  = []
completeHISTORY = []

"""Randomisation Function"""
def CWpair(prevword, prevcolour, counter):             # CWpair = Colour-Word Pair
    
    TEXT  = list(COLOURtxt) 
    INK   = list(COLOURhex)
    
    """Ensure that text and colour are not repeated"""
    TEXT.remove(prevword)                  # Temporarily remove the last used word from the list to ensure it cannot be randomly picked for a 2nd time
    INK.remove(prevcolour)                 # Temporarily remove the last used colour from the list to ensure it cannot be randomly picked for a 2nd time
    
    word   = random.choice(TEXT)           # Randomly selects a word
    colour = random.choice(INK)            # Randomly selects ink colour
    
    """Transform hex codes into respective words for ease of user interpretation"""
    pos = COLOURhex.index(colour)          # Find the position of this color in its list
    match = COLOURtxt[pos]                 # Match the hex code to the correct word in the word list
    inkHISTORY.append(match)               # Append the word version of the hex code to the ANSWERS list, this makes it easier for human interpretation of the solutions, hex is confusing
    
    wordHISTORY.append(word)
    
    timer= time.perf_counter()             # Return the value (in fractional seconds) of a performance counter, i.e. a clock with the highest available resolution to measure a short duration. It does include time elapsed during sleep and is system-wide. The reference point of the returned value is undefined, so that only the difference between the results of consecutive calls is valid.
    timeHISTORY.append(timer)
    
    sp = ' , '
    element= (str(counter)+sp+word+sp+match+sp+str(timer))  # Create one element which consists of the word, ink and time on the system
    completeHISTORY.append(element)                         # Add the element to the list
    
    return (word, colour)                  # Outputs the word and ink colour combination

    
"""Options for the Delta T Value, ie the amount of time between presented CW pairs"""
set_time = 1
change = -0    # CHANGE THE VALUE OF DELTA-T HERE


"""Generates a new colourword every X seconds"""
def next_selected():
    prevword  = 'RED'                       # Establish one word and colour that we want to remove in the first iteration, otherwise the code will be confused
    prevcolour= '#ff0000'
    counter = 1
    while True:                             # Enter an endless loop
        word, colour = CWpair(prevword, prevcolour, counter)
        prevcolour = colour                 # Save the current ink colour
        prevword   = word                   # Save the current text
        counter +=1
        label.config(text=word, fg=colour)  # Tells the tkinter feature what to do with the text and the colour, assigns them to the foreground and text components
        label.update()                      # Update the label with the new CW pair
        time.sleep(set_time + change)
    
    
"""Closes the window via a 'close' button"""
def quit_selected():       
    root.destroy()          # Perhaps not the best way to close the tkinter function
    
    
"""Hide buttons until the test has been started"""
def startseq():                             # when the start button is pressed, 
    frequency = 1600                        # Set Frequency To 1600 Hertz
    duration  = 500                         # Set Duration To 500 ms == 0.5 second
    winsound.Beep(frequency, duration)      # Produce a beep to signify the beginning of the Stroop test for Audacity
    closebutton.pack(padx=50, pady=50)      # it makes the 'close test' button appear
    start_button.pack_forget()              # then hides the start button as the test has begun!
    # timer = time.time()                   # starts a timer once the test has started
    next_selected()                         # changes the word one time only
    
    
root = tkinter.Tk()                     # create the window 
"""Create the window which will present the Stroop Test"""
prevword  = 'RED'                       # Establish one word and colour that we want to remove in the first iteration, otherwise the code will be confused
prevcolour= '#ff0000'
word, colour = CWpair(prevword, prevcolour, 0)                 
label = tkinter.Label(root, 
                      bg= "white",      # white has better contrast than light grey
                      text= word,       # word selected at random
                      fg= colour,       # ink colour selected at random
                      width= 15,
                      height= 2,        # any higher than 2 pushes the buttons out of view
                      font = "Verdana 100 bold")
label.pack()                            # presents the window
    

"""Button functions"""
start_button = tkinter.Button(root, text='Click here to start the Stroop Test!', command=startseq)
start_button.pack(padx=50, pady=100)

closebutton = tkinter.Button(root, 
                             text='Close Stroop Test', 
                             command=quit_selected)

root.mainloop()

"""Remove excess elements from the list"""
# The code for some reason adds on 2 extra colours to this list that did not make it to the screen before the close button was pressed
# This code force removes those 2 extra words, making it present only the colours that were seen by the user
# I presume the code works ahead of what it presents, adding elements that were not yet seen
n=2
del inkHISTORY[-n:]  
del wordHISTORY[-n:]  
del completeHISTORY[-n:] 

print('Colours of the Ink, in order of appearance:')
print(inkHISTORY)
print('')
print('Words, in order of appearance:')
print(wordHISTORY)
print('')
print('Complete History: ')
print('# , Text ,   Ink ,    Time (ms)')     # Gives Titles to the Info being provided in the console
print(*completeHISTORY, sep="\n")       # Prints the elements, dividing them by a new line
print('')



