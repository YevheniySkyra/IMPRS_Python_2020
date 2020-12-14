from psychopy import sound, visual, event, core
import pandas as pd
import numpy as np
import os


os.chdir("C:\\Users\\Zhenya\\Desktop\\PhD MPI NL\\Courses\\Python IMPRS\\Session3\\session3")

#create a window the text will be displayed on
window = visual.Window((800, 600), color=(1, 1, 1))

#Create a fixation cross with a given color
fixation = visual.TextStim(window, text='+', color=(-1, -1, -1))


response = visual.TextStim(window, text= "Please enter your response.", color=(-1, -1, -1))

#Show the fixation cross for 1 second
fixation.draw()
window.flip()
core.wait(1.0)

#instruction text
window.flip()
instruction = visual.TextStim(window, text= "Welcome to the experiment! Press the spacebar to start the experiment. After you hear a word press a on the keyboard if you hear a word, otherwise press l.", 
                               color=(-1, -1, -1))
instruction.draw()
window.flip()
event.waitKeys()


#load stimuli
sound_stimuli = pd.read_csv("lexical_decision_stimuli.csv")
#print(stimuli)


sounds = []
for i, row in sound_stimuli.iterrows():
    sounds.append(sound.Sound(value = 'sounds' + '\\' + row['freq_category'] + '\\'  + row['word'] + '.wav'))
sounds = np.random.permutation(sounds)

conditions = []
for condition in sound_stimuli["freq_category"]: 
    conditions.append(condition["freq_category"])


clock = core.Clock()
results = []

for sound in sounds[:5]:
    #Play a sound
    #audio = sound.Sound('sounds/HF/auto.wav')
    fixation.draw()
    window.flip()
    core.wait(0.5)    
    

    sound.play()
    core.wait(sound.getDuration())
    response.draw()
    window.flip()
    #core.wait(1.0)

    #wait for user input
    start_time = clock.getTime()
    clock = core.Clock()
    keys = event.waitKeys(maxWait=5, keyList=["a", "l"], timeStamped=clock, clearEvents=True)
    if keys is not None:
        key, reaction_time = keys[0]  
    else:
        key = None
    reaction_time = 5 # clock.getTime() #or reaction_time = 5 - to wait 5 seconds to show the next trial
    end_time = clock.getTime()
    #condition = visual.TextStim(window, text=condition)
    
    #Store the results
    results.append({
        "sound" : sounds[3:],   #
        "freq_category" : condition.text, # 
        "key" : key,
        "start_time" : start_time,
        "end_time" : end_time
    })
results = pd.DataFrame(results)
results['reaction_time'] = results['end_time'] - results['start_time']  # Calculate all the reaction times
results.to_csv('results.csv')
