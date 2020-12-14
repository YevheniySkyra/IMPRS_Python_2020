import csv
import os
import numpy as np
from pydub import AudioSegment, silence
from pydub.silence import split_on_silence
from pydub.playback import play
from matplotlib.pyplot import plot, show

# We have three conditions: High Frequency (HF), Low Frequency (LF), and Non-Words (NW).
# All words for each condition are stored in one .wav file.
# Your task is to:
#       split the words on the silence
#       make sure they all have the same loudness
#       save them in a folder corresponding to their condition (folder names: HF, LF, NW)

AudioSegment.converter = "C:\\Program Files\\ffmpeg\\bin\\ffmpeg.exe"

path_to_repository = "C:\\Users\\Zhenya\\Desktop\\PhD MPI NL\\Courses\\Python IMPRS\\session2b-sound"  # add your own path here!

# This piece of code is here to help you.
# It reads a text file with information about the stimuli you are going to split (names & condition),
# and returns a dictionary named 'stimuli' with condition as key, and the word itself as value.
# Use this dictionary to name the files you have to save.
stimuli_info = open(os.path.join(path_to_repository, "lexdec_stimuli.txt"))
stimuli_reader = csv.reader(stimuli_info, delimiter=',')
headers = next(stimuli_reader, None)

# Create the dictionary
stimuli = {}
for stimulus in stimuli_reader:
    if stimulus[2] not in stimuli.keys():
        stimuli[stimulus[2]] = list()
    stimuli[stimulus[2]].append(stimulus[3])

# Put them in alphabetical order
for condition, words in stimuli.items():
    sort = sorted(words)
    stimuli[condition] = sort

# change the non-word condition name
stimuli["NW"] = stimuli.pop("none")
#print(stimuli)

# Now you have the stimulus names. Let's take a look at the dictionary:
#print(stimuli)
#print(len(stimuli["HF"]))
#HF and LF contain 5o items each; NW contains 100 (correct?)
#print(stimuli["NW"])

# YOUR CODE HERE.



# Some hints:
# 1. Where are the stimuli?
sound_folder = "C:\\Users\\Zhenya\\Desktop\\PhD MPI NL\\Courses\\Python IMPRS\\session2b-sound\\raw"
sound_list = os.listdir(sound_folder)
#print(sound_list)

#print(os.listdir(sound_folder))

#path to the folders with HF, LF and NW
folder_HF = "C:\\Users\\Zhenya\\Desktop\\PhD MPI NL\\Courses\\Python IMPRS\\session2b-sound\\folder_HF"
folder_LF = "C:\\Users\\Zhenya\\Desktop\\PhD MPI NL\\Courses\\Python IMPRS\\session2b-sound\\folder_LF"
folder_NW = "C:\\Users\\Zhenya\\Desktop\\PhD MPI NL\\Courses\\Python IMPRS\\session2b-sound\\folder_NW"



#sound_path = os.path.join(sound_folder, "HF_recording.wav")
#sound = AudioSegment.from_wav(sound_path)
# 2. How loud do you want your stimuli to be? Store it in a variable
#opening files
#HF = "HF_recording.wav"
#LF = "LF_recording.wav"
#NW = "NW_recording.wav"

sound_HF = AudioSegment.from_wav(os.path.join(sound_folder, "HF_recording.wav"))
sound_LF = AudioSegment.from_wav(os.path.join(sound_folder, "LF_recording.wav"))
sound_NW = AudioSegment.from_wav(os.path.join(sound_folder, "NW_recording.wav"))



#visualize

#array = sound_HF.get_array_of_samples()

#
#print(array)

# Now we plot it. If you don't run in console, you have to type show() to actually open a window with the plot.
#plot(array)
#show()

#print(sound_HF.max)
#print(sound_HF.min)
#print(sound_HF.dBFS)
#-18.170628180228533

target_dBFS = -18

#splitting sound files on silence
HF_chunks = silence.split_on_silence(sound_HF, min_silence_len=100, silence_thresh=-100)
LF_chunks = silence.split_on_silence(sound_LF, min_silence_len=100, silence_thresh=-100)
NW_chunks = silence.split_on_silence(sound_NW, min_silence_len=100, silence_thresh=-100)

 
#play(HF_chunks[1]) # 
#play(HF_chunks)
#HF_chunks.export(os.path.join(sound_folder, HF_chunks), format = "wav" )

#assign splitted sound files a number and save in the respective directory
for i, chunk in enumerate(HF_chunks):                   #adopted from: https://stackoverflow.com/questions/36799902/how-to-splice-an-audio-file-wav-format-into-1-sec-splices-in-python
    chunk_name = "HF_{0}.wav".format(i)
    print ("exporting", chunk_name)
    chunk.export(chunk_name, format="wav") # save sound files in "wav" format
    chunk.export(os.path.join(folder_HF, chunk_name))  # save sound files into the corresponding



#assign splitted sound files a number and save in the respective directory
for i, chunk in enumerate(LF_chunks):                   #adopted from: https://stackoverflow.com/questions/36799902/how-to-splice-an-audio-file-wav-format-into-1-sec-splices-in-python
    chunk_name = "LF_{0}.wav".format(i)
    print ("exporting", chunk_name)
    chunk.export(chunk_name, format="wav") # save sound files in "wav" format
    chunk.export(os.path.join(folder_LF, chunk_name))  # save sound files into the corresponding


 
#assign splitted sound files a number and save in the respective directory
for i, chunk in enumerate(NW_chunks):                   #adopted from: https://stackoverflow.com/questions/36799902/how-to-splice-an-audio-file-wav-format-into-1-sec-splices-in-python
    chunk_name = "NW_{0}.wav".format(i)
    print ("exporting", chunk_name)
    chunk.export(chunk_name, format="wav") # save sound files in "wav" format
    chunk.export(os.path.join(folder_NW, chunk_name))  # save sound files into the corresponding


#convert dictionary to an array
words = list(stimuli.items())
words_array = np.array(words)
#print(words_array[])



#assign names from the words_array to the HF sound files ( I got stuck here )
count = enummerate(HF_chunks)
for i, (chunk, words_array) in enumerate(HF_chunks):                                 #adopted from: https://stackoverflow.com/questions/36799902/how-to-splice-an-audio-file-wav-format-into-1-sec-splices-in-python
    chunk_name = HF_chunks.format(i)
    print ("exporting", chunk_name) 
    chunk.export(chunk_name, format="wav") # save sound files in "wav" format
    chunk.export(os.path.join(folder_HF, chunk_name))  # save sound files into the corresponding

 