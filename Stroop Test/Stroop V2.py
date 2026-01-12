"""Stroop V2"""
# Successful CW pairing
# Tidied up and removed excess code from source
# More context for my task added


# Sourced from:
# https://stackoverflow.com/questions/36255642/stroop-test-in-python-not-working-properly
# 28/1/2021
# https://www.python-course.eu/tkinter_labels.php
# 28/1/2021
# Works well, I changed the font size to fit the whole screen and changed bg colour to dark grey from white to make colours more legible 
# However, a button must be manually clicked to move on to the next colour.

# Wanted to find true blue/red/green etc using RGB
# tkinter doesn't naturally use rbg- uses hex
# transform our RGB colours into tkinter friendly codes then sub into the COLORS_W list
# Sourced from:
# https://python-forum.io/Thread-How-to-get-RGB-colors-in-tkinter

# def rgb_color(rgb):
#     return '#%02x%02x%02x' % rgb
# print(rgb_color((0, 255, 0)))

import tkinter  # use for the Button, Label and Frame
import random
import time

"""Summary of the words and ink colours I will be using"""
COLOURtext = ['RED',      'GREEN',    'BLUE',   'YELLOW',  'PINK',    'BLACK']
COLOURhex  = ['#ff0000', '#00ff00', '#0000ff', '#ffee00', '#ff00ff', '#000000']  # colours of the ink in HEX, representing RBG colours


"""Randomising function"""
def CWpair():
    text  = list(COLOURtext)
    ink   = list(COLOURhex)
   
    word   = random.choice(text)         # Randomly selects a word from the list of colours
    colour = random.choice(ink)          # Randomly selects the colour of the ink to be used
    
    return (word, colour)                 # Outputs the word and ink colour combination

    
"""Options for the Delta T Value, ie the amount of time between presented CW pairs"""
D1 = 0.5
D2 = 1
D3 = 1.5
D4 = 2
    

"""Generates a new colourword every X seconds"""
def next_selected():
    while True:                             #Enter endless loop
        word, colour = CWpair()
        label.config(text=word, fg=colour)   # Tells the tkinter feature what to do with the text and the colour, assigns them to the foreground and text components
        label.update()                      # Update the label with the new CW pair
        time.sleep(D1)                      # CHANGE THE VALUE OF D HERE
    
    
"""Closes the window via a button"""
def quit_selected():        # Closes the window if the user clicks 'close' button
    root.destroy()
    
    
"""Hide buttons until the test has been started"""
def startseq():                             # when the start button is pressed, 
    closebutton.pack(padx=50, pady=50)      # it makes the 'close test' button appear
    start_button.pack_forget()              # then hides the start button as the test has begun!
    # timer = time.time()                   # and finally starts a timer once the test has started
    next_selected()                         # changes the word one time only
    
    
root = tkinter.Tk()                     # create the window 
"""Create the window which will present the Stroop Test"""
word, colour = CWpair()            # accesses random colour and word combinations, separating the two returned outputs
label = tkinter.Label(root, 
                      bg= "white",      # white has better contrast than light grey
                      text= word,       # word selected at random
                      fg= colour,        # ink colour selected at random
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

