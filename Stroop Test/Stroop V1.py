"""Stroop V1"""
# Code copied from source, some excess code still in here
# Need to push a button to initiate next CW pair
# Want to automate this process

# Sourced from:
# https://stackoverflow.com/questions/36255642/stroop-test-in-python-not-working-properly
# 28/1/2021
# https://www.python-course.eu/tkinter_labels.php
# 28/1/2021
# Works well, I changed the font size to fit the whole screen and changed bg colour to dark grey from white to make colours more legible 
# However, a button must be manually clicked to move on to the next colour.

# Wanted to find true blue/red/green etc using RGB
# tkinter doesn't naturally use rbg- helper function
# transform our RGB colours into ikinter friendly codes then sub into the COLORS_W list
# Sourced from:
# https://python-forum.io/Thread-How-to-get-RGB-colors-in-tkinter
# 255 = 1

# def rgb_color(rgb):
#     return '#%02x%02x%02x' % rgb
 
# print(rgb_color((0, 255, 0)))


import tkinter  # use for the Button, Label and Frame
import random
import time

"""Summary of the words and ink colours I will be using"""
COLORS = ['red', 'blue', 'green', 'yellow', 'pink', 'black']
COLORS_W = ['#ff0000', '#00ff00', '#0000ff', '#ffff00', '#ff00ff', '#000000']  # colours of the ink in HEX, representing RBG colours

"""Randomising function"""
def stimulus(same):
    colors = list(COLORS) 
    colorsW= list(COLORS_W)      
    word = random.choice(colors)         # Randomly selects a word from the list of colours
    # if same:            
    #     return (word, word)            # Unnecessary code for matching coreect ink to word pairs
    colors.remove(word)
    color = random.choice(colorsW)       # Randomly selects the colour of the ink to be used
    return (word, color)                 # Outputs the word and ink colour combination

"""Prepares the label to present new data"""
def next_selected():
    word, color = stimulus(random.choice((True, False)))
    label.config(text=word, fg=color)   # Tells the tkinter feature what to do with the text and the colour, assigns them to the foreground and text components
    label.update()

"""Closes the window via a button"""
def quit_selected():        # Closes the window if the user clicks 'close' button
    root.destroy()
    

root = tkinter.Tk()         # Create the window

# Create label using stimulus
word, color = stimulus(True)        # accesses random colour and word combination, separating the two returned outputs
label = tkinter.Label(root, 
                      bg= "white",  # white has better contrast than light grey
                      text= word,   # word selected at random
                      fg= color,    # ink colour selected at random
                      width= 15,
                      height= 2,
                      font = "Verdana 100 bold")
label.pack()


"""Specify the text on the buttons and the locations"""
nextbutton = tkinter.Button(root, 
                            text='Next Colour', 
                            command=next_selected)
nextbutton.pack(padx=50, pady=50)

closebutton = tkinter.Button(root, 
                             text='Close Stroop Test', 
                             command=quit_selected)
closebutton.pack(padx=50, pady=50)


# NEED TO AUTOMATE THE SKIPPING PROCESS WITH A TIMER, MODIFIABLE T VALUE


root.mainloop()