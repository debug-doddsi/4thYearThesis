"""Segmentation of a Wav file into sub-files"""
# Turn the code into a function for ease of implementation?


import numpy as np
from scipy.io import wavfile
import os
    
 
def split_audio(prefix, sample_rate, sound_data, num_samples, threshold=8000, clip_length=0.4, clip_pretrigger = 0.1):
    # threshold: could be power??, 5000 still detects keyboard clicks, try 8000
    # clip_length: in seconds, vary to encapsulate the duration of the (longest?) word
    # clip_pretrigger: the amount of time we will rewind to record once we register that sound is being made, this ensure we catch the beginning of the word being spoken

        
    """scan through the sound file, which is stored in the same folder as this code"""
    i = 0
    sound_clip_id = 0
    while i < num_samples:
        if sound_data[int(i)] > threshold:
    
            """extract the clip""" 
            sound_clip_start = int(i - sample_rate * clip_pretrigger)
            sound_clip_end = int(i + sample_rate * (clip_length - clip_pretrigger))
            sound_clip = sound_data[sound_clip_start: sound_clip_end]
    
            """perform normalisation on sound_clip for each individual file"""
            maxi = abs(np.amax(sound_clip))                     # finds the absolute max/min values of the sound clip
            mini = abs(np.amin(sound_clip))     
                                       # tidy up printed results
            if maxi > mini:                                     # normalise to a max value just below the maximum value for an integer (max = 32,767)
                sound_clip = int((np.divide(float(sound_clip), float(maxi))) * 31000.0)
            elif mini > maxi:                                   # normalise to a min value just below the minimum value for an integer (min = -32,767)
                sound_clip = int((np.divide(float(sound_clip), float(mini))) * 31000.0)
    
            """save the clip"""
            # file_name = f'{clip_prefix}{sound_clip_id:05}.wav'
            trigger_time_ms = int(i / sample_rate * 1000.0)
            file_name = f'{clip_prefix}{trigger_time_ms:05}.wav'
            wavfile.write(file_name, sample_rate, sound_clip)
            sound_clip_id += 1
    
            # plot the clip
            # plt.plot(range(sound_clip.shape[0]), sound_clip)
    
            # jump over the clip, we don't need to listen to it again
            i = sound_clip_end
    
        i += 1
    
    print('Complete')

"""Access the Original, Unsplit Audio File"""
path = r'C:\Users\Iona\Pictures\University\4th Year\BE406- DISSERTATION\Python Code\Speech Recognition\Datasets (speaking colours)\Craig\1 Raw Data'
os.chdir(path)                                          # change the cwd to access the audio stored in a different place to the code files (helps to keep my computer organised)
clip_prefix = 'yellow_'                                 # the prefix which shall be stuck onto the beginning of each word file, change as appropriate, ie for each colour 
sample_rate, sound_data = wavfile.read('Yellow.wav')    # read the sound file and extract parameters 
num_samples = sound_data.shape[0]

split_audio(clip_prefix,sample_rate,sound_data,num_samples)
