"""Segmentation of a Wav file into WAV snippets"""


#import numpy as np
from scipy.io import wavfile
import os
import time
import numpy as np

start_time = time.time()

# import matplotlib.pyplot as plt

# path1 = cwd where the long audio clip (that we want to divide) is stored
path1 = r'C:\Users\Iona\Pictures\University\4th Year\BE406- DISSERTATION\Data Collection\1 word testing'
# path2 = cwd where we want to store the chopped up audio
path2 = r'C:\Users\Iona\Pictures\University\4th Year\BE406- DISSERTATION\Data Collection\1 word testing\split'

os.chdir(path1)  # go to the cwd where the audio file is stored
number_of_clips = 0

# parameters
threshold = 7000                # baseline 7000
clip_length = 0.7               # in seconds, vary to encapsulate the duration of the (longest?) word
clip_pretrigger = 0.1           # the amount of time we will rewind to record once we register that sound is being made, this ensure we catch the beginning of the word being spoken
clip_prefix = 'stroop_'         # the prefix which shall be stuck onto the beginning of each word file, change as appropriate, ie for each colour

# read the sound file and extract parameters from 
sample_rate, sound_data = wavfile.read('noisered + norm.wav')       # identify the audio file name you want to cut up
num_samples = sound_data.shape[0]
# print(num_samples)
# print(sample_rate) 

os.chdir(path2)     
# scan through the sound file, which is stored in the same folder as this code
i = 0
sound_clip_id = 0
while i < num_samples:
    if sound_data[int(i)] > threshold:

        """Extract the clip""" 
        sound_clip_start = int(i - sample_rate * clip_pretrigger)
        sound_clip_end   = int(i + sample_rate * (clip_length - clip_pretrigger))
        # clip_duration = sound_clip_end-sound_clip_start
        sound_clip = sound_data[sound_clip_start: sound_clip_end].astype(float)
        
        
        """Perform normalisation on sound_clip for each individual file"""
        maxi = float(abs(np.amax(sound_clip)))                # finds the absolute max/min values of the sound clip
        mini = float(abs(np.amin(sound_clip)))     
        # print('Maximum: ', maxi)                            # prints the max/min values of the vectors
        # print('Minimum: ', mini)
        
        sound_clip= np.array(sound_clip)                      # transform into a np array

        
        if maxi > mini:                                     
            sound_clip = 31000.0 * sound_clip / maxi    # normalise to a max value just below the maximum value for an integer (max = 32,767)
        else:                                   
            sound_clip = 31000.0 * sound_clip / mini    # normalise to a min value just below the minimum value for an integer (min = -32,767)
    
 
        """Save the clip"""
        
        trigger_time_ms = int(i / sample_rate * 1000.0)
        file_name = f'{clip_prefix}{trigger_time_ms:05}.wav'
        wavfile.write(file_name, sample_rate, sound_clip.astype(np.int16))
        sound_clip_id += 1

        # plot the clip
        # plt.plot(range(sound_clip.shape[0]), sound_clip)

        # jump over the clip, we don't need to listen to it again
        i = sound_clip_end
        number_of_clips += 1

    i += 1

print('Complete')
print('The code took', (time.time()-start_time), 'seconds to complete.')
print('There were', number_of_clips, 'clips created.')
