#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2020.2.3),
    on september 28, 2020, at 14:57
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2020.2.3'
expName = 'speciale_eksperiment'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sort_keys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\User\\OneDrive\\Dokumenter\\speciale\\forsøgsdesign\\eksperiment\\speciale_eksperiment.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=[1366, 768], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color='black', colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "instruction_1"
instruction_1Clock = core.Clock()
instruktion = visual.TextStim(win=win, name='instruktion',
    text='Velkommen til forsøget!\n\nI forsøget vil du blive præsenteret for nogle sætninger. Til hver sætning er der et spørgsmål, du skal svare på. Du skal klikke på det svar, du tror er rigtigt, så hurtigt som muligt.\n\nDu går videre ved at klikke med musen på krydset.\n',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
instruction_mouse = event.Mouse(win=win)
x, y = [None, None]
instruction_mouse.mouseClock = core.Clock()
start_1 = visual.ShapeStim(
    win=win, name='start_1', vertices='cross',
    size=(0.1, 0.1),
    ori=0, pos=(0, -0.4),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-2.0, interpolate=True)

# Initialize components for Routine "pause"
pauseClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "instruction_2"
instruction_2Clock = core.Clock()
instr_2 = visual.TextStim(win=win, name='instr_2',
    text='Du skal trykke med musen på krydset for at få præsenteret ny tekst i løbet af forsøget.\n\nDer vil først være en træningsrunde, hvor det bliver klart, hvad du skal gøre.\n\nTryk på krydset, når du er klar til at starte træningsrunden.',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
intr_2_mouse = event.Mouse(win=win)
x, y = [None, None]
intr_2_mouse.mouseClock = core.Clock()
start_2 = visual.ShapeStim(
    win=win, name='start_2', vertices='cross',
    size=(0.1, 0.1),
    ori=0, pos=(0, -0.4),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-2.0, interpolate=True)

# Initialize components for Routine "pause"
pauseClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "training_stimuli"
training_stimuliClock = core.Clock()
train_stim_1 = visual.TextStim(win=win, name='train_stim_1',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
train_stim_1_next = visual.ShapeStim(
    win=win, name='train_stim_1_next', vertices='cross',
    size=(0.1, 0.1),
    ori=0, pos=(0, -0.4),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-1.0, interpolate=True)
train_stim_1_mouse = event.Mouse(win=win)
x, y = [None, None]
train_stim_1_mouse.mouseClock = core.Clock()
train_count = visual.TextStim(win=win, name='train_count',
    text='default text',
    font='Arial',
    pos=(0.7, -0.40), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "training_trial_3"
training_trial_3Clock = core.Clock()
training_mousetrack = event.Mouse(win=win)
x, y = [None, None]
training_mousetrack.mouseClock = core.Clock()
option_left_train = visual.TextStim(win=win, name='option_left_train',
    text='default text',
    font='Arial',
    pos=(-0.7, 0.4), height=0.075, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
option_right_train = visual.TextStim(win=win, name='option_right_train',
    text='default text',
    font='Arial',
    pos=(0.70, 0.4), height=0.075, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
question_train = visual.TextStim(win=win, name='question_train',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.075, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
train_trial_start = visual.ShapeStim(
    win=win, name='train_trial_start', vertices='cross',
    size=(0.1, 0.1),
    ori=0, pos=(0, -0.40),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-4.0, interpolate=True)
trial_count_train = visual.TextStim(win=win, name='trial_count_train',
    text='default text',
    font='Arial',
    pos=(0.7, -0.40), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);

# Initialize components for Routine "tak"
takClock = core.Clock()
next_text = visual.TextStim(win=win, name='next_text',
    text='Tak!\n\nTryk på krydset',
    font='Arial',
    pos=(0, 0), height=0.075, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
next_text_cross = visual.ShapeStim(
    win=win, name='next_text_cross', vertices='cross',
    size=(0.1, 0.1),
    ori=0, pos=(0, -0.4),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-1.0, interpolate=True)
next_text_mouse = event.Mouse(win=win)
x, y = [None, None]
next_text_mouse.mouseClock = core.Clock()
tak_train_count = visual.TextStim(win=win, name='tak_train_count',
    text='default text',
    font='Arial',
    pos=(0.7, -0.4), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "nu_starter_vi"
nu_starter_viClock = core.Clock()
real_start = visual.TextStim(win=win, name='real_start',
    text='Sådan! Det var træningsrunden\n\nTal med den forsøgsansvarlige for at gå videre til forsøget.',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
start_real = keyboard.Keyboard()

# Initialize components for Routine "start_real_2"
start_real_2Clock = core.Clock()
start_between = visual.ShapeStim(
    win=win, name='start_between', vertices='cross',
    size=(0.1, 0.1),
    ori=0, pos=(0, -0.40),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
starting_text = visual.TextStim(win=win, name='starting_text',
    text='Tryk på krydset for at starte',
    font='Arial',
    pos=(0, 0), height=0.075, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
real_start_mouse = event.Mouse(win=win)
x, y = [None, None]
real_start_mouse.mouseClock = core.Clock()

# Initialize components for Routine "pause"
pauseClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "stimuli"
stimuliClock = core.Clock()
stim_1_text = visual.TextStim(win=win, name='stim_1_text',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
stim_1_mouse = event.Mouse(win=win)
x, y = [None, None]
stim_1_mouse.mouseClock = core.Clock()
stim_1_next = visual.ShapeStim(
    win=win, name='stim_1_next', vertices='cross',
    size=(0.1, 0.1),
    ori=0, pos=(0, -0.4),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-2.0, interpolate=True)
trial_count = visual.TextStim(win=win, name='trial_count',
    text='default text',
    font='Arial',
    pos=(0.70, -0.40), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "trial_2"
trial_2Clock = core.Clock()
trial_mouse = event.Mouse(win=win)
x, y = [None, None]
trial_mouse.mouseClock = core.Clock()
option_left = visual.TextStim(win=win, name='option_left',
    text='default text',
    font='Arial',
    pos=(0.7, 0.4), height=0.075, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
option_right = visual.TextStim(win=win, name='option_right',
    text='default text',
    font='Arial',
    pos=(-0.7, 0.4), height=0.075, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
trial_quest = visual.TextStim(win=win, name='trial_quest',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.075, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
trial_start = visual.ShapeStim(
    win=win, name='trial_start', vertices='cross',
    size=(0.1, 0.1),
    ori=0, pos=(0, -0.4),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-4.0, interpolate=True)
triCount = visual.TextStim(win=win, name='triCount',
    text='default text',
    font='Arial',
    pos=(0.7, -0.40), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);

# Initialize components for Routine "tak"
takClock = core.Clock()
next_text = visual.TextStim(win=win, name='next_text',
    text='Tak!\n\nTryk på krydset',
    font='Arial',
    pos=(0, 0), height=0.075, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
next_text_cross = visual.ShapeStim(
    win=win, name='next_text_cross', vertices='cross',
    size=(0.1, 0.1),
    ori=0, pos=(0, -0.4),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-1.0, interpolate=True)
next_text_mouse = event.Mouse(win=win)
x, y = [None, None]
next_text_mouse.mouseClock = core.Clock()
tak_train_count = visual.TextStim(win=win, name='tak_train_count',
    text='default text',
    font='Arial',
    pos=(0.7, -0.4), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "end"
endClock = core.Clock()
end_text = visual.TextStim(win=win, name='end_text',
    text='Forsøget er slut!\nTak for din deltagelse.',
    font='Arial',
    pos=(0, 0), height=0.075, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "instruction_1"-------
continueRoutine = True
# update component parameters for each repeat
# setup some python lists for storing info about the instruction_mouse
instruction_mouse.clicked_name = []
gotValidClick = False  # until a click is received
# keep track of which components have finished
instruction_1Components = [instruktion, instruction_mouse, start_1]
for thisComponent in instruction_1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instruction_1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "instruction_1"-------
while continueRoutine:
    # get current time
    t = instruction_1Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instruction_1Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instruktion* updates
    if instruktion.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instruktion.frameNStart = frameN  # exact frame index
        instruktion.tStart = t  # local t and not account for scr refresh
        instruktion.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instruktion, 'tStartRefresh')  # time at next scr refresh
        instruktion.setAutoDraw(True)
    # *instruction_mouse* updates
    if instruction_mouse.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instruction_mouse.frameNStart = frameN  # exact frame index
        instruction_mouse.tStart = t  # local t and not account for scr refresh
        instruction_mouse.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instruction_mouse, 'tStartRefresh')  # time at next scr refresh
        instruction_mouse.status = STARTED
        instruction_mouse.mouseClock.reset()
        prevButtonState = instruction_mouse.getPressed()  # if button is down already this ISN'T a new click
    if instruction_mouse.status == STARTED:  # only update if started and not finished!
        buttons = instruction_mouse.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                # check if the mouse was inside our 'clickable' objects
                gotValidClick = False
                for obj in [start_1]:
                    if obj.contains(instruction_mouse):
                        gotValidClick = True
                        instruction_mouse.clicked_name.append(obj.name)
                if gotValidClick:  # abort routine on response
                    continueRoutine = False
    
    # *start_1* updates
    if start_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        start_1.frameNStart = frameN  # exact frame index
        start_1.tStart = t  # local t and not account for scr refresh
        start_1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(start_1, 'tStartRefresh')  # time at next scr refresh
        start_1.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instruction_1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instruction_1"-------
for thisComponent in instruction_1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('instruktion.started', instruktion.tStartRefresh)
thisExp.addData('instruktion.stopped', instruktion.tStopRefresh)
# store data for thisExp (ExperimentHandler)
thisExp.addData('instruction_mouse.started', instruction_mouse.tStart)
thisExp.addData('instruction_mouse.stopped', instruction_mouse.tStop)
thisExp.nextEntry()
thisExp.addData('start_1.started', start_1.tStartRefresh)
thisExp.addData('start_1.stopped', start_1.tStopRefresh)
# the Routine "instruction_1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "pause"-------
continueRoutine = True
routineTimer.add(0.500000)
# update component parameters for each repeat
# keep track of which components have finished
pauseComponents = [text]
for thisComponent in pauseComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
pauseClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "pause"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = pauseClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=pauseClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text* updates
    if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text.frameNStart = frameN  # exact frame index
        text.tStart = t  # local t and not account for scr refresh
        text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
        text.setAutoDraw(True)
    if text.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text.tStartRefresh + 0.5-frameTolerance:
            # keep track of stop time/frame for later
            text.tStop = t  # not accounting for scr refresh
            text.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text, 'tStopRefresh')  # time at next scr refresh
            text.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in pauseComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "pause"-------
for thisComponent in pauseComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text.started', text.tStartRefresh)
thisExp.addData('text.stopped', text.tStopRefresh)

# ------Prepare to start Routine "instruction_2"-------
continueRoutine = True
# update component parameters for each repeat
# setup some python lists for storing info about the intr_2_mouse
intr_2_mouse.clicked_name = []
gotValidClick = False  # until a click is received
# keep track of which components have finished
instruction_2Components = [instr_2, intr_2_mouse, start_2]
for thisComponent in instruction_2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instruction_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "instruction_2"-------
while continueRoutine:
    # get current time
    t = instruction_2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instruction_2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instr_2* updates
    if instr_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instr_2.frameNStart = frameN  # exact frame index
        instr_2.tStart = t  # local t and not account for scr refresh
        instr_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instr_2, 'tStartRefresh')  # time at next scr refresh
        instr_2.setAutoDraw(True)
    # *intr_2_mouse* updates
    if intr_2_mouse.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        intr_2_mouse.frameNStart = frameN  # exact frame index
        intr_2_mouse.tStart = t  # local t and not account for scr refresh
        intr_2_mouse.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(intr_2_mouse, 'tStartRefresh')  # time at next scr refresh
        intr_2_mouse.status = STARTED
        intr_2_mouse.mouseClock.reset()
        prevButtonState = intr_2_mouse.getPressed()  # if button is down already this ISN'T a new click
    if intr_2_mouse.status == STARTED:  # only update if started and not finished!
        buttons = intr_2_mouse.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                # check if the mouse was inside our 'clickable' objects
                gotValidClick = False
                for obj in [start_2]:
                    if obj.contains(intr_2_mouse):
                        gotValidClick = True
                        intr_2_mouse.clicked_name.append(obj.name)
                if gotValidClick:  # abort routine on response
                    continueRoutine = False
    
    # *start_2* updates
    if start_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        start_2.frameNStart = frameN  # exact frame index
        start_2.tStart = t  # local t and not account for scr refresh
        start_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(start_2, 'tStartRefresh')  # time at next scr refresh
        start_2.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instruction_2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instruction_2"-------
for thisComponent in instruction_2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('instr_2.started', instr_2.tStartRefresh)
thisExp.addData('instr_2.stopped', instr_2.tStopRefresh)
# store data for thisExp (ExperimentHandler)
thisExp.addData('intr_2_mouse.started', intr_2_mouse.tStart)
thisExp.addData('intr_2_mouse.stopped', intr_2_mouse.tStop)
thisExp.nextEntry()
thisExp.addData('start_2.started', start_2.tStartRefresh)
thisExp.addData('start_2.stopped', start_2.tStopRefresh)
# the Routine "instruction_2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
training_trial = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('training_stimuli.xlsx'),
    seed=None, name='training_trial')
thisExp.addLoop(training_trial)  # add the loop to the experiment
thisTraining_trial = training_trial.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTraining_trial.rgb)
if thisTraining_trial != None:
    for paramName in thisTraining_trial:
        exec('{} = thisTraining_trial[paramName]'.format(paramName))

for thisTraining_trial in training_trial:
    currentLoop = training_trial
    # abbreviate parameter names if possible (e.g. rgb = thisTraining_trial.rgb)
    if thisTraining_trial != None:
        for paramName in thisTraining_trial:
            exec('{} = thisTraining_trial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "pause"-------
    continueRoutine = True
    routineTimer.add(0.500000)
    # update component parameters for each repeat
    # keep track of which components have finished
    pauseComponents = [text]
    for thisComponent in pauseComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    pauseClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "pause"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = pauseClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=pauseClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text* updates
        if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text.frameNStart = frameN  # exact frame index
            text.tStart = t  # local t and not account for scr refresh
            text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
            text.setAutoDraw(True)
        if text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                text.tStop = t  # not accounting for scr refresh
                text.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text, 'tStopRefresh')  # time at next scr refresh
                text.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in pauseComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "pause"-------
    for thisComponent in pauseComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    training_trial.addData('text.started', text.tStartRefresh)
    training_trial.addData('text.stopped', text.tStopRefresh)
    
    # ------Prepare to start Routine "training_stimuli"-------
    continueRoutine = True
    routineTimer.add(5.000000)
    # update component parameters for each repeat
    train_stim_1.setText(stim)
    # setup some python lists for storing info about the train_stim_1_mouse
    train_stim_1_mouse.x = []
    train_stim_1_mouse.y = []
    train_stim_1_mouse.leftButton = []
    train_stim_1_mouse.midButton = []
    train_stim_1_mouse.rightButton = []
    train_stim_1_mouse.time = []
    train_stim_1_mouse.clicked_name = []
    gotValidClick = False  # until a click is received
    train_stim_1_mouse.mouseClock.reset()
    train_count.setText(trial_counter
)
    # keep track of which components have finished
    training_stimuliComponents = [train_stim_1, train_stim_1_next, train_stim_1_mouse, train_count]
    for thisComponent in training_stimuliComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    training_stimuliClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "training_stimuli"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = training_stimuliClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=training_stimuliClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *train_stim_1* updates
        if train_stim_1.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            train_stim_1.frameNStart = frameN  # exact frame index
            train_stim_1.tStart = t  # local t and not account for scr refresh
            train_stim_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(train_stim_1, 'tStartRefresh')  # time at next scr refresh
            train_stim_1.setAutoDraw(True)
        if train_stim_1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > train_stim_1.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                train_stim_1.tStop = t  # not accounting for scr refresh
                train_stim_1.frameNStop = frameN  # exact frame index
                win.timeOnFlip(train_stim_1, 'tStopRefresh')  # time at next scr refresh
                train_stim_1.setAutoDraw(False)
        
        # *train_stim_1_next* updates
        if train_stim_1_next.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            train_stim_1_next.frameNStart = frameN  # exact frame index
            train_stim_1_next.tStart = t  # local t and not account for scr refresh
            train_stim_1_next.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(train_stim_1_next, 'tStartRefresh')  # time at next scr refresh
            train_stim_1_next.setAutoDraw(True)
        if train_stim_1_next.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > train_stim_1_next.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                train_stim_1_next.tStop = t  # not accounting for scr refresh
                train_stim_1_next.frameNStop = frameN  # exact frame index
                win.timeOnFlip(train_stim_1_next, 'tStopRefresh')  # time at next scr refresh
                train_stim_1_next.setAutoDraw(False)
        # *train_stim_1_mouse* updates
        if train_stim_1_mouse.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            train_stim_1_mouse.frameNStart = frameN  # exact frame index
            train_stim_1_mouse.tStart = t  # local t and not account for scr refresh
            train_stim_1_mouse.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(train_stim_1_mouse, 'tStartRefresh')  # time at next scr refresh
            train_stim_1_mouse.status = STARTED
            prevButtonState = train_stim_1_mouse.getPressed()  # if button is down already this ISN'T a new click
        if train_stim_1_mouse.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > train_stim_1_mouse.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                train_stim_1_mouse.tStop = t  # not accounting for scr refresh
                train_stim_1_mouse.frameNStop = frameN  # exact frame index
                win.timeOnFlip(train_stim_1_mouse, 'tStopRefresh')  # time at next scr refresh
                train_stim_1_mouse.status = FINISHED
        if train_stim_1_mouse.status == STARTED:  # only update if started and not finished!
            buttons = train_stim_1_mouse.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    for obj in [train_stim_1_next]:
                        if obj.contains(train_stim_1_mouse):
                            gotValidClick = True
                            train_stim_1_mouse.clicked_name.append(obj.name)
                    x, y = train_stim_1_mouse.getPos()
                    train_stim_1_mouse.x.append(x)
                    train_stim_1_mouse.y.append(y)
                    buttons = train_stim_1_mouse.getPressed()
                    train_stim_1_mouse.leftButton.append(buttons[0])
                    train_stim_1_mouse.midButton.append(buttons[1])
                    train_stim_1_mouse.rightButton.append(buttons[2])
                    train_stim_1_mouse.time.append(train_stim_1_mouse.mouseClock.getTime())
                    if gotValidClick:  # abort routine on response
                        continueRoutine = False
        
        # *train_count* updates
        if train_count.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            train_count.frameNStart = frameN  # exact frame index
            train_count.tStart = t  # local t and not account for scr refresh
            train_count.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(train_count, 'tStartRefresh')  # time at next scr refresh
            train_count.setAutoDraw(True)
        if train_count.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > train_count.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                train_count.tStop = t  # not accounting for scr refresh
                train_count.frameNStop = frameN  # exact frame index
                win.timeOnFlip(train_count, 'tStopRefresh')  # time at next scr refresh
                train_count.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in training_stimuliComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "training_stimuli"-------
    for thisComponent in training_stimuliComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    training_trial.addData('train_stim_1.started', train_stim_1.tStartRefresh)
    training_trial.addData('train_stim_1.stopped', train_stim_1.tStopRefresh)
    training_trial.addData('train_stim_1_next.started', train_stim_1_next.tStartRefresh)
    training_trial.addData('train_stim_1_next.stopped', train_stim_1_next.tStopRefresh)
    # store data for training_trial (TrialHandler)
    if len(train_stim_1_mouse.x): training_trial.addData('train_stim_1_mouse.x', train_stim_1_mouse.x[0])
    if len(train_stim_1_mouse.y): training_trial.addData('train_stim_1_mouse.y', train_stim_1_mouse.y[0])
    if len(train_stim_1_mouse.leftButton): training_trial.addData('train_stim_1_mouse.leftButton', train_stim_1_mouse.leftButton[0])
    if len(train_stim_1_mouse.midButton): training_trial.addData('train_stim_1_mouse.midButton', train_stim_1_mouse.midButton[0])
    if len(train_stim_1_mouse.rightButton): training_trial.addData('train_stim_1_mouse.rightButton', train_stim_1_mouse.rightButton[0])
    if len(train_stim_1_mouse.time): training_trial.addData('train_stim_1_mouse.time', train_stim_1_mouse.time[0])
    if len(train_stim_1_mouse.clicked_name): training_trial.addData('train_stim_1_mouse.clicked_name', train_stim_1_mouse.clicked_name[0])
    training_trial.addData('train_stim_1_mouse.started', train_stim_1_mouse.tStart)
    training_trial.addData('train_stim_1_mouse.stopped', train_stim_1_mouse.tStop)
    training_trial.addData('train_count.started', train_count.tStartRefresh)
    training_trial.addData('train_count.stopped', train_count.tStopRefresh)
    
    # ------Prepare to start Routine "training_trial_3"-------
    continueRoutine = True
    routineTimer.add(10.500000)
    # update component parameters for each repeat
    # setup some python lists for storing info about the training_mousetrack
    training_mousetrack.x = []
    training_mousetrack.y = []
    training_mousetrack.leftButton = []
    training_mousetrack.midButton = []
    training_mousetrack.rightButton = []
    training_mousetrack.time = []
    training_mousetrack.clicked_name = []
    gotValidClick = False  # until a click is received
    training_mousetrack.mouseClock.reset()
    option_left_train.setText(option_1)
    option_right_train.setText(option_2)
    question_train.setText(question)
    trial_count_train.setText(trial_counter
)
    # keep track of which components have finished
    training_trial_3Components = [training_mousetrack, option_left_train, option_right_train, question_train, train_trial_start, trial_count_train]
    for thisComponent in training_trial_3Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    training_trial_3Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "training_trial_3"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = training_trial_3Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=training_trial_3Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # *training_mousetrack* updates
        if training_mousetrack.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            training_mousetrack.frameNStart = frameN  # exact frame index
            training_mousetrack.tStart = t  # local t and not account for scr refresh
            training_mousetrack.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(training_mousetrack, 'tStartRefresh')  # time at next scr refresh
            training_mousetrack.status = STARTED
            prevButtonState = training_mousetrack.getPressed()  # if button is down already this ISN'T a new click
        if training_mousetrack.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > training_mousetrack.tStartRefresh + 10-frameTolerance:
                # keep track of stop time/frame for later
                training_mousetrack.tStop = t  # not accounting for scr refresh
                training_mousetrack.frameNStop = frameN  # exact frame index
                win.timeOnFlip(training_mousetrack, 'tStopRefresh')  # time at next scr refresh
                training_mousetrack.status = FINISHED
        if training_mousetrack.status == STARTED:  # only update if started and not finished!
            x, y = training_mousetrack.getPos()
            training_mousetrack.x.append(x)
            training_mousetrack.y.append(y)
            buttons = training_mousetrack.getPressed()
            training_mousetrack.leftButton.append(buttons[0])
            training_mousetrack.midButton.append(buttons[1])
            training_mousetrack.rightButton.append(buttons[2])
            training_mousetrack.time.append(training_mousetrack.mouseClock.getTime())
            buttons = training_mousetrack.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    for obj in [option_left_train, option_right_train]:
                        if obj.contains(training_mousetrack):
                            gotValidClick = True
                            training_mousetrack.clicked_name.append(obj.name)
                    if gotValidClick:  # abort routine on response
                        continueRoutine = False
        
        # *option_left_train* updates
        if option_left_train.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            option_left_train.frameNStart = frameN  # exact frame index
            option_left_train.tStart = t  # local t and not account for scr refresh
            option_left_train.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(option_left_train, 'tStartRefresh')  # time at next scr refresh
            option_left_train.setAutoDraw(True)
        if option_left_train.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > option_left_train.tStartRefresh + 10-frameTolerance:
                # keep track of stop time/frame for later
                option_left_train.tStop = t  # not accounting for scr refresh
                option_left_train.frameNStop = frameN  # exact frame index
                win.timeOnFlip(option_left_train, 'tStopRefresh')  # time at next scr refresh
                option_left_train.setAutoDraw(False)
        
        # *option_right_train* updates
        if option_right_train.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            option_right_train.frameNStart = frameN  # exact frame index
            option_right_train.tStart = t  # local t and not account for scr refresh
            option_right_train.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(option_right_train, 'tStartRefresh')  # time at next scr refresh
            option_right_train.setAutoDraw(True)
        if option_right_train.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > option_right_train.tStartRefresh + 10-frameTolerance:
                # keep track of stop time/frame for later
                option_right_train.tStop = t  # not accounting for scr refresh
                option_right_train.frameNStop = frameN  # exact frame index
                win.timeOnFlip(option_right_train, 'tStopRefresh')  # time at next scr refresh
                option_right_train.setAutoDraw(False)
        
        # *question_train* updates
        if question_train.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            question_train.frameNStart = frameN  # exact frame index
            question_train.tStart = t  # local t and not account for scr refresh
            question_train.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(question_train, 'tStartRefresh')  # time at next scr refresh
            question_train.setAutoDraw(True)
        if question_train.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > question_train.tStartRefresh + 10-frameTolerance:
                # keep track of stop time/frame for later
                question_train.tStop = t  # not accounting for scr refresh
                question_train.frameNStop = frameN  # exact frame index
                win.timeOnFlip(question_train, 'tStopRefresh')  # time at next scr refresh
                question_train.setAutoDraw(False)
        
        # *train_trial_start* updates
        if train_trial_start.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            train_trial_start.frameNStart = frameN  # exact frame index
            train_trial_start.tStart = t  # local t and not account for scr refresh
            train_trial_start.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(train_trial_start, 'tStartRefresh')  # time at next scr refresh
            train_trial_start.setAutoDraw(True)
        if train_trial_start.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > train_trial_start.tStartRefresh + 10-frameTolerance:
                # keep track of stop time/frame for later
                train_trial_start.tStop = t  # not accounting for scr refresh
                train_trial_start.frameNStop = frameN  # exact frame index
                win.timeOnFlip(train_trial_start, 'tStopRefresh')  # time at next scr refresh
                train_trial_start.setAutoDraw(False)
        
        # *trial_count_train* updates
        if trial_count_train.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            trial_count_train.frameNStart = frameN  # exact frame index
            trial_count_train.tStart = t  # local t and not account for scr refresh
            trial_count_train.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trial_count_train, 'tStartRefresh')  # time at next scr refresh
            trial_count_train.setAutoDraw(True)
        if trial_count_train.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > trial_count_train.tStartRefresh + 10-frameTolerance:
                # keep track of stop time/frame for later
                trial_count_train.tStop = t  # not accounting for scr refresh
                trial_count_train.frameNStop = frameN  # exact frame index
                win.timeOnFlip(trial_count_train, 'tStopRefresh')  # time at next scr refresh
                trial_count_train.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in training_trial_3Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "training_trial_3"-------
    for thisComponent in training_trial_3Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store data for training_trial (TrialHandler)
    training_trial.addData('training_mousetrack.x', training_mousetrack.x)
    training_trial.addData('training_mousetrack.y', training_mousetrack.y)
    training_trial.addData('training_mousetrack.leftButton', training_mousetrack.leftButton)
    training_trial.addData('training_mousetrack.midButton', training_mousetrack.midButton)
    training_trial.addData('training_mousetrack.rightButton', training_mousetrack.rightButton)
    training_trial.addData('training_mousetrack.time', training_mousetrack.time)
    training_trial.addData('training_mousetrack.clicked_name', training_mousetrack.clicked_name)
    training_trial.addData('training_mousetrack.started', training_mousetrack.tStart)
    training_trial.addData('training_mousetrack.stopped', training_mousetrack.tStop)
    training_trial.addData('option_left_train.started', option_left_train.tStartRefresh)
    training_trial.addData('option_left_train.stopped', option_left_train.tStopRefresh)
    training_trial.addData('option_right_train.started', option_right_train.tStartRefresh)
    training_trial.addData('option_right_train.stopped', option_right_train.tStopRefresh)
    training_trial.addData('question_train.started', question_train.tStartRefresh)
    training_trial.addData('question_train.stopped', question_train.tStopRefresh)
    training_trial.addData('train_trial_start.started', train_trial_start.tStartRefresh)
    training_trial.addData('train_trial_start.stopped', train_trial_start.tStopRefresh)
    training_trial.addData('trial_count_train.started', trial_count_train.tStartRefresh)
    training_trial.addData('trial_count_train.stopped', trial_count_train.tStopRefresh)
    
    # ------Prepare to start Routine "tak"-------
    continueRoutine = True
    # update component parameters for each repeat
    # setup some python lists for storing info about the next_text_mouse
    next_text_mouse.clicked_name = []
    gotValidClick = False  # until a click is received
    tak_train_count.setText(trial_counter
)
    # keep track of which components have finished
    takComponents = [next_text, next_text_cross, next_text_mouse, tak_train_count]
    for thisComponent in takComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    takClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "tak"-------
    while continueRoutine:
        # get current time
        t = takClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=takClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *next_text* updates
        if next_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            next_text.frameNStart = frameN  # exact frame index
            next_text.tStart = t  # local t and not account for scr refresh
            next_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(next_text, 'tStartRefresh')  # time at next scr refresh
            next_text.setAutoDraw(True)
        
        # *next_text_cross* updates
        if next_text_cross.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            next_text_cross.frameNStart = frameN  # exact frame index
            next_text_cross.tStart = t  # local t and not account for scr refresh
            next_text_cross.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(next_text_cross, 'tStartRefresh')  # time at next scr refresh
            next_text_cross.setAutoDraw(True)
        # *next_text_mouse* updates
        if next_text_mouse.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            next_text_mouse.frameNStart = frameN  # exact frame index
            next_text_mouse.tStart = t  # local t and not account for scr refresh
            next_text_mouse.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(next_text_mouse, 'tStartRefresh')  # time at next scr refresh
            next_text_mouse.status = STARTED
            next_text_mouse.mouseClock.reset()
            prevButtonState = next_text_mouse.getPressed()  # if button is down already this ISN'T a new click
        if next_text_mouse.status == STARTED:  # only update if started and not finished!
            buttons = next_text_mouse.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    for obj in [next_text_cross]:
                        if obj.contains(next_text_mouse):
                            gotValidClick = True
                            next_text_mouse.clicked_name.append(obj.name)
                    if gotValidClick:  # abort routine on response
                        continueRoutine = False
        
        # *tak_train_count* updates
        if tak_train_count.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            tak_train_count.frameNStart = frameN  # exact frame index
            tak_train_count.tStart = t  # local t and not account for scr refresh
            tak_train_count.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(tak_train_count, 'tStartRefresh')  # time at next scr refresh
            tak_train_count.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in takComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "tak"-------
    for thisComponent in takComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    training_trial.addData('next_text.started', next_text.tStartRefresh)
    training_trial.addData('next_text.stopped', next_text.tStopRefresh)
    training_trial.addData('next_text_cross.started', next_text_cross.tStartRefresh)
    training_trial.addData('next_text_cross.stopped', next_text_cross.tStopRefresh)
    # store data for training_trial (TrialHandler)
    training_trial.addData('next_text_mouse.started', next_text_mouse.tStart)
    training_trial.addData('next_text_mouse.stopped', next_text_mouse.tStop)
    training_trial.addData('tak_train_count.started', tak_train_count.tStartRefresh)
    training_trial.addData('tak_train_count.stopped', tak_train_count.tStopRefresh)
    # the Routine "tak" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'training_trial'


# ------Prepare to start Routine "nu_starter_vi"-------
continueRoutine = True
# update component parameters for each repeat
start_real.keys = []
start_real.rt = []
_start_real_allKeys = []
# keep track of which components have finished
nu_starter_viComponents = [real_start, start_real]
for thisComponent in nu_starter_viComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
nu_starter_viClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "nu_starter_vi"-------
while continueRoutine:
    # get current time
    t = nu_starter_viClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=nu_starter_viClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *real_start* updates
    if real_start.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        real_start.frameNStart = frameN  # exact frame index
        real_start.tStart = t  # local t and not account for scr refresh
        real_start.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(real_start, 'tStartRefresh')  # time at next scr refresh
        real_start.setAutoDraw(True)
    
    # *start_real* updates
    waitOnFlip = False
    if start_real.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        start_real.frameNStart = frameN  # exact frame index
        start_real.tStart = t  # local t and not account for scr refresh
        start_real.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(start_real, 'tStartRefresh')  # time at next scr refresh
        start_real.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(start_real.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(start_real.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if start_real.status == STARTED and not waitOnFlip:
        theseKeys = start_real.getKeys(keyList=['x', 'y'], waitRelease=False)
        _start_real_allKeys.extend(theseKeys)
        if len(_start_real_allKeys):
            start_real.keys = _start_real_allKeys[-1].name  # just the last key pressed
            start_real.rt = _start_real_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in nu_starter_viComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "nu_starter_vi"-------
for thisComponent in nu_starter_viComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('real_start.started', real_start.tStartRefresh)
thisExp.addData('real_start.stopped', real_start.tStopRefresh)
# check responses
if start_real.keys in ['', [], None]:  # No response was made
    start_real.keys = None
thisExp.addData('start_real.keys',start_real.keys)
if start_real.keys != None:  # we had a response
    thisExp.addData('start_real.rt', start_real.rt)
thisExp.addData('start_real.started', start_real.tStartRefresh)
thisExp.addData('start_real.stopped', start_real.tStopRefresh)
thisExp.nextEntry()
# the Routine "nu_starter_vi" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "start_real_2"-------
continueRoutine = True
# update component parameters for each repeat
# setup some python lists for storing info about the real_start_mouse
real_start_mouse.x = []
real_start_mouse.y = []
real_start_mouse.leftButton = []
real_start_mouse.midButton = []
real_start_mouse.rightButton = []
real_start_mouse.time = []
real_start_mouse.clicked_name = []
gotValidClick = False  # until a click is received
# keep track of which components have finished
start_real_2Components = [start_between, starting_text, real_start_mouse]
for thisComponent in start_real_2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
start_real_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "start_real_2"-------
while continueRoutine:
    # get current time
    t = start_real_2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=start_real_2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *start_between* updates
    if start_between.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        start_between.frameNStart = frameN  # exact frame index
        start_between.tStart = t  # local t and not account for scr refresh
        start_between.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(start_between, 'tStartRefresh')  # time at next scr refresh
        start_between.setAutoDraw(True)
    
    # *starting_text* updates
    if starting_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        starting_text.frameNStart = frameN  # exact frame index
        starting_text.tStart = t  # local t and not account for scr refresh
        starting_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(starting_text, 'tStartRefresh')  # time at next scr refresh
        starting_text.setAutoDraw(True)
    # *real_start_mouse* updates
    if real_start_mouse.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        real_start_mouse.frameNStart = frameN  # exact frame index
        real_start_mouse.tStart = t  # local t and not account for scr refresh
        real_start_mouse.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(real_start_mouse, 'tStartRefresh')  # time at next scr refresh
        real_start_mouse.status = STARTED
        real_start_mouse.mouseClock.reset()
        prevButtonState = real_start_mouse.getPressed()  # if button is down already this ISN'T a new click
    if real_start_mouse.status == STARTED:  # only update if started and not finished!
        buttons = real_start_mouse.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                # check if the mouse was inside our 'clickable' objects
                gotValidClick = False
                for obj in [start_between]:
                    if obj.contains(real_start_mouse):
                        gotValidClick = True
                        real_start_mouse.clicked_name.append(obj.name)
                x, y = real_start_mouse.getPos()
                real_start_mouse.x.append(x)
                real_start_mouse.y.append(y)
                buttons = real_start_mouse.getPressed()
                real_start_mouse.leftButton.append(buttons[0])
                real_start_mouse.midButton.append(buttons[1])
                real_start_mouse.rightButton.append(buttons[2])
                real_start_mouse.time.append(real_start_mouse.mouseClock.getTime())
                if gotValidClick:  # abort routine on response
                    continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in start_real_2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "start_real_2"-------
for thisComponent in start_real_2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('start_between.started', start_between.tStartRefresh)
thisExp.addData('start_between.stopped', start_between.tStopRefresh)
thisExp.addData('starting_text.started', starting_text.tStartRefresh)
thisExp.addData('starting_text.stopped', starting_text.tStopRefresh)
# store data for thisExp (ExperimentHandler)
if len(real_start_mouse.x): thisExp.addData('real_start_mouse.x', real_start_mouse.x[0])
if len(real_start_mouse.y): thisExp.addData('real_start_mouse.y', real_start_mouse.y[0])
if len(real_start_mouse.leftButton): thisExp.addData('real_start_mouse.leftButton', real_start_mouse.leftButton[0])
if len(real_start_mouse.midButton): thisExp.addData('real_start_mouse.midButton', real_start_mouse.midButton[0])
if len(real_start_mouse.rightButton): thisExp.addData('real_start_mouse.rightButton', real_start_mouse.rightButton[0])
if len(real_start_mouse.time): thisExp.addData('real_start_mouse.time', real_start_mouse.time[0])
if len(real_start_mouse.clicked_name): thisExp.addData('real_start_mouse.clicked_name', real_start_mouse.clicked_name[0])
thisExp.addData('real_start_mouse.started', real_start_mouse.tStart)
thisExp.addData('real_start_mouse.stopped', real_start_mouse.tStop)
thisExp.nextEntry()
# the Routine "start_real_2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('trial_stimuli_1.xlsx'),
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "pause"-------
    continueRoutine = True
    routineTimer.add(0.500000)
    # update component parameters for each repeat
    # keep track of which components have finished
    pauseComponents = [text]
    for thisComponent in pauseComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    pauseClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "pause"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = pauseClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=pauseClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text* updates
        if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text.frameNStart = frameN  # exact frame index
            text.tStart = t  # local t and not account for scr refresh
            text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
            text.setAutoDraw(True)
        if text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                text.tStop = t  # not accounting for scr refresh
                text.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text, 'tStopRefresh')  # time at next scr refresh
                text.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in pauseComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "pause"-------
    for thisComponent in pauseComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('text.started', text.tStartRefresh)
    trials.addData('text.stopped', text.tStopRefresh)
    
    # ------Prepare to start Routine "stimuli"-------
    continueRoutine = True
    routineTimer.add(5.000000)
    # update component parameters for each repeat
    stim_1_text.setText(stim)
    # setup some python lists for storing info about the stim_1_mouse
    stim_1_mouse.clicked_name = []
    gotValidClick = False  # until a click is received
    trial_count.setText(trial_counter)
    # keep track of which components have finished
    stimuliComponents = [stim_1_text, stim_1_mouse, stim_1_next, trial_count]
    for thisComponent in stimuliComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    stimuliClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "stimuli"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = stimuliClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=stimuliClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *stim_1_text* updates
        if stim_1_text.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            stim_1_text.frameNStart = frameN  # exact frame index
            stim_1_text.tStart = t  # local t and not account for scr refresh
            stim_1_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(stim_1_text, 'tStartRefresh')  # time at next scr refresh
            stim_1_text.setAutoDraw(True)
        if stim_1_text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > stim_1_text.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                stim_1_text.tStop = t  # not accounting for scr refresh
                stim_1_text.frameNStop = frameN  # exact frame index
                win.timeOnFlip(stim_1_text, 'tStopRefresh')  # time at next scr refresh
                stim_1_text.setAutoDraw(False)
        # *stim_1_mouse* updates
        if stim_1_mouse.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            stim_1_mouse.frameNStart = frameN  # exact frame index
            stim_1_mouse.tStart = t  # local t and not account for scr refresh
            stim_1_mouse.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(stim_1_mouse, 'tStartRefresh')  # time at next scr refresh
            stim_1_mouse.status = STARTED
            stim_1_mouse.mouseClock.reset()
            prevButtonState = stim_1_mouse.getPressed()  # if button is down already this ISN'T a new click
        if stim_1_mouse.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > stim_1_mouse.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                stim_1_mouse.tStop = t  # not accounting for scr refresh
                stim_1_mouse.frameNStop = frameN  # exact frame index
                win.timeOnFlip(stim_1_mouse, 'tStopRefresh')  # time at next scr refresh
                stim_1_mouse.status = FINISHED
        if stim_1_mouse.status == STARTED:  # only update if started and not finished!
            buttons = stim_1_mouse.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    for obj in [stim_1_next]:
                        if obj.contains(stim_1_mouse):
                            gotValidClick = True
                            stim_1_mouse.clicked_name.append(obj.name)
                    if gotValidClick:  # abort routine on response
                        continueRoutine = False
        
        # *stim_1_next* updates
        if stim_1_next.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            stim_1_next.frameNStart = frameN  # exact frame index
            stim_1_next.tStart = t  # local t and not account for scr refresh
            stim_1_next.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(stim_1_next, 'tStartRefresh')  # time at next scr refresh
            stim_1_next.setAutoDraw(True)
        if stim_1_next.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > stim_1_next.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                stim_1_next.tStop = t  # not accounting for scr refresh
                stim_1_next.frameNStop = frameN  # exact frame index
                win.timeOnFlip(stim_1_next, 'tStopRefresh')  # time at next scr refresh
                stim_1_next.setAutoDraw(False)
        
        # *trial_count* updates
        if trial_count.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            trial_count.frameNStart = frameN  # exact frame index
            trial_count.tStart = t  # local t and not account for scr refresh
            trial_count.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trial_count, 'tStartRefresh')  # time at next scr refresh
            trial_count.setAutoDraw(True)
        if trial_count.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > trial_count.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                trial_count.tStop = t  # not accounting for scr refresh
                trial_count.frameNStop = frameN  # exact frame index
                win.timeOnFlip(trial_count, 'tStopRefresh')  # time at next scr refresh
                trial_count.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in stimuliComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "stimuli"-------
    for thisComponent in stimuliComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('stim_1_text.started', stim_1_text.tStartRefresh)
    trials.addData('stim_1_text.stopped', stim_1_text.tStopRefresh)
    # store data for trials (TrialHandler)
    x, y = stim_1_mouse.getPos()
    buttons = stim_1_mouse.getPressed()
    if sum(buttons):
        # check if the mouse was inside our 'clickable' objects
        gotValidClick = False
        for obj in [stim_1_next]:
            if obj.contains(stim_1_mouse):
                gotValidClick = True
                stim_1_mouse.clicked_name.append(obj.name)
    trials.addData('stim_1_mouse.x', x)
    trials.addData('stim_1_mouse.y', y)
    trials.addData('stim_1_mouse.leftButton', buttons[0])
    trials.addData('stim_1_mouse.midButton', buttons[1])
    trials.addData('stim_1_mouse.rightButton', buttons[2])
    if len(stim_1_mouse.clicked_name):
        trials.addData('stim_1_mouse.clicked_name', stim_1_mouse.clicked_name[0])
    trials.addData('stim_1_mouse.started', stim_1_mouse.tStart)
    trials.addData('stim_1_mouse.stopped', stim_1_mouse.tStop)
    trials.addData('stim_1_next.started', stim_1_next.tStartRefresh)
    trials.addData('stim_1_next.stopped', stim_1_next.tStopRefresh)
    trials.addData('trial_count.started', trial_count.tStartRefresh)
    trials.addData('trial_count.stopped', trial_count.tStopRefresh)
    
    # ------Prepare to start Routine "trial_2"-------
    continueRoutine = True
    routineTimer.add(20.500000)
    # update component parameters for each repeat
    # setup some python lists for storing info about the trial_mouse
    trial_mouse.x = []
    trial_mouse.y = []
    trial_mouse.leftButton = []
    trial_mouse.midButton = []
    trial_mouse.rightButton = []
    trial_mouse.time = []
    trial_mouse.clicked_name = []
    gotValidClick = False  # until a click is received
    trial_mouse.mouseClock.reset()
    option_left.setText(left_option)
    option_right.setText(right_option)
    trial_quest.setText(question)
    triCount.setText(trial_counter)
    # keep track of which components have finished
    trial_2Components = [trial_mouse, option_left, option_right, trial_quest, trial_start, triCount]
    for thisComponent in trial_2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    trial_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "trial_2"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = trial_2Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=trial_2Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # *trial_mouse* updates
        if trial_mouse.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            trial_mouse.frameNStart = frameN  # exact frame index
            trial_mouse.tStart = t  # local t and not account for scr refresh
            trial_mouse.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trial_mouse, 'tStartRefresh')  # time at next scr refresh
            trial_mouse.status = STARTED
            prevButtonState = [0, 0, 0]  # if now button is down we will treat as 'new' click
        if trial_mouse.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > trial_mouse.tStartRefresh + 20-frameTolerance:
                # keep track of stop time/frame for later
                trial_mouse.tStop = t  # not accounting for scr refresh
                trial_mouse.frameNStop = frameN  # exact frame index
                win.timeOnFlip(trial_mouse, 'tStopRefresh')  # time at next scr refresh
                trial_mouse.status = FINISHED
        if trial_mouse.status == STARTED:  # only update if started and not finished!
            x, y = trial_mouse.getPos()
            trial_mouse.x.append(x)
            trial_mouse.y.append(y)
            buttons = trial_mouse.getPressed()
            trial_mouse.leftButton.append(buttons[0])
            trial_mouse.midButton.append(buttons[1])
            trial_mouse.rightButton.append(buttons[2])
            trial_mouse.time.append(trial_mouse.mouseClock.getTime())
            buttons = trial_mouse.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    for obj in [option_left, option_right]:
                        if obj.contains(trial_mouse):
                            gotValidClick = True
                            trial_mouse.clicked_name.append(obj.name)
                    if gotValidClick:  # abort routine on response
                        continueRoutine = False
        
        # *option_left* updates
        if option_left.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            option_left.frameNStart = frameN  # exact frame index
            option_left.tStart = t  # local t and not account for scr refresh
            option_left.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(option_left, 'tStartRefresh')  # time at next scr refresh
            option_left.setAutoDraw(True)
        if option_left.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > option_left.tStartRefresh + 20-frameTolerance:
                # keep track of stop time/frame for later
                option_left.tStop = t  # not accounting for scr refresh
                option_left.frameNStop = frameN  # exact frame index
                win.timeOnFlip(option_left, 'tStopRefresh')  # time at next scr refresh
                option_left.setAutoDraw(False)
        
        # *option_right* updates
        if option_right.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            option_right.frameNStart = frameN  # exact frame index
            option_right.tStart = t  # local t and not account for scr refresh
            option_right.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(option_right, 'tStartRefresh')  # time at next scr refresh
            option_right.setAutoDraw(True)
        if option_right.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > option_right.tStartRefresh + 20-frameTolerance:
                # keep track of stop time/frame for later
                option_right.tStop = t  # not accounting for scr refresh
                option_right.frameNStop = frameN  # exact frame index
                win.timeOnFlip(option_right, 'tStopRefresh')  # time at next scr refresh
                option_right.setAutoDraw(False)
        
        # *trial_quest* updates
        if trial_quest.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            trial_quest.frameNStart = frameN  # exact frame index
            trial_quest.tStart = t  # local t and not account for scr refresh
            trial_quest.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trial_quest, 'tStartRefresh')  # time at next scr refresh
            trial_quest.setAutoDraw(True)
        if trial_quest.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > trial_quest.tStartRefresh + 20-frameTolerance:
                # keep track of stop time/frame for later
                trial_quest.tStop = t  # not accounting for scr refresh
                trial_quest.frameNStop = frameN  # exact frame index
                win.timeOnFlip(trial_quest, 'tStopRefresh')  # time at next scr refresh
                trial_quest.setAutoDraw(False)
        
        # *trial_start* updates
        if trial_start.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            trial_start.frameNStart = frameN  # exact frame index
            trial_start.tStart = t  # local t and not account for scr refresh
            trial_start.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trial_start, 'tStartRefresh')  # time at next scr refresh
            trial_start.setAutoDraw(True)
        if trial_start.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > trial_start.tStartRefresh + 20-frameTolerance:
                # keep track of stop time/frame for later
                trial_start.tStop = t  # not accounting for scr refresh
                trial_start.frameNStop = frameN  # exact frame index
                win.timeOnFlip(trial_start, 'tStopRefresh')  # time at next scr refresh
                trial_start.setAutoDraw(False)
        
        # *triCount* updates
        if triCount.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            triCount.frameNStart = frameN  # exact frame index
            triCount.tStart = t  # local t and not account for scr refresh
            triCount.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(triCount, 'tStartRefresh')  # time at next scr refresh
            triCount.setAutoDraw(True)
        if triCount.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > triCount.tStartRefresh + 20-frameTolerance:
                # keep track of stop time/frame for later
                triCount.tStop = t  # not accounting for scr refresh
                triCount.frameNStop = frameN  # exact frame index
                win.timeOnFlip(triCount, 'tStopRefresh')  # time at next scr refresh
                triCount.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trial_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trial_2"-------
    for thisComponent in trial_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store data for trials (TrialHandler)
    trials.addData('trial_mouse.x', trial_mouse.x)
    trials.addData('trial_mouse.y', trial_mouse.y)
    trials.addData('trial_mouse.leftButton', trial_mouse.leftButton)
    trials.addData('trial_mouse.midButton', trial_mouse.midButton)
    trials.addData('trial_mouse.rightButton', trial_mouse.rightButton)
    trials.addData('trial_mouse.time', trial_mouse.time)
    trials.addData('trial_mouse.clicked_name', trial_mouse.clicked_name)
    trials.addData('trial_mouse.started', trial_mouse.tStartRefresh)
    trials.addData('trial_mouse.stopped', trial_mouse.tStopRefresh)
    trials.addData('option_left.started', option_left.tStartRefresh)
    trials.addData('option_left.stopped', option_left.tStopRefresh)
    trials.addData('option_right.started', option_right.tStartRefresh)
    trials.addData('option_right.stopped', option_right.tStopRefresh)
    trials.addData('trial_quest.started', trial_quest.tStartRefresh)
    trials.addData('trial_quest.stopped', trial_quest.tStopRefresh)
    trials.addData('trial_start.started', trial_start.tStartRefresh)
    trials.addData('trial_start.stopped', trial_start.tStopRefresh)
    trials.addData('triCount.started', triCount.tStartRefresh)
    trials.addData('triCount.stopped', triCount.tStopRefresh)
    
    # ------Prepare to start Routine "tak"-------
    continueRoutine = True
    # update component parameters for each repeat
    # setup some python lists for storing info about the next_text_mouse
    next_text_mouse.clicked_name = []
    gotValidClick = False  # until a click is received
    tak_train_count.setText(trial_counter
)
    # keep track of which components have finished
    takComponents = [next_text, next_text_cross, next_text_mouse, tak_train_count]
    for thisComponent in takComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    takClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "tak"-------
    while continueRoutine:
        # get current time
        t = takClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=takClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *next_text* updates
        if next_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            next_text.frameNStart = frameN  # exact frame index
            next_text.tStart = t  # local t and not account for scr refresh
            next_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(next_text, 'tStartRefresh')  # time at next scr refresh
            next_text.setAutoDraw(True)
        
        # *next_text_cross* updates
        if next_text_cross.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            next_text_cross.frameNStart = frameN  # exact frame index
            next_text_cross.tStart = t  # local t and not account for scr refresh
            next_text_cross.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(next_text_cross, 'tStartRefresh')  # time at next scr refresh
            next_text_cross.setAutoDraw(True)
        # *next_text_mouse* updates
        if next_text_mouse.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            next_text_mouse.frameNStart = frameN  # exact frame index
            next_text_mouse.tStart = t  # local t and not account for scr refresh
            next_text_mouse.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(next_text_mouse, 'tStartRefresh')  # time at next scr refresh
            next_text_mouse.status = STARTED
            next_text_mouse.mouseClock.reset()
            prevButtonState = next_text_mouse.getPressed()  # if button is down already this ISN'T a new click
        if next_text_mouse.status == STARTED:  # only update if started and not finished!
            buttons = next_text_mouse.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    for obj in [next_text_cross]:
                        if obj.contains(next_text_mouse):
                            gotValidClick = True
                            next_text_mouse.clicked_name.append(obj.name)
                    if gotValidClick:  # abort routine on response
                        continueRoutine = False
        
        # *tak_train_count* updates
        if tak_train_count.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            tak_train_count.frameNStart = frameN  # exact frame index
            tak_train_count.tStart = t  # local t and not account for scr refresh
            tak_train_count.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(tak_train_count, 'tStartRefresh')  # time at next scr refresh
            tak_train_count.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in takComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "tak"-------
    for thisComponent in takComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('next_text.started', next_text.tStartRefresh)
    trials.addData('next_text.stopped', next_text.tStopRefresh)
    trials.addData('next_text_cross.started', next_text_cross.tStartRefresh)
    trials.addData('next_text_cross.stopped', next_text_cross.tStopRefresh)
    # store data for trials (TrialHandler)
    trials.addData('next_text_mouse.started', next_text_mouse.tStart)
    trials.addData('next_text_mouse.stopped', next_text_mouse.tStop)
    trials.addData('tak_train_count.started', tak_train_count.tStartRefresh)
    trials.addData('tak_train_count.stopped', tak_train_count.tStopRefresh)
    # the Routine "tak" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials'


# ------Prepare to start Routine "end"-------
continueRoutine = True
routineTimer.add(20.000000)
# update component parameters for each repeat
# keep track of which components have finished
endComponents = [end_text]
for thisComponent in endComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
endClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "end"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = endClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=endClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *end_text* updates
    if end_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        end_text.frameNStart = frameN  # exact frame index
        end_text.tStart = t  # local t and not account for scr refresh
        end_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(end_text, 'tStartRefresh')  # time at next scr refresh
        end_text.setAutoDraw(True)
    if end_text.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > end_text.tStartRefresh + 20-frameTolerance:
            # keep track of stop time/frame for later
            end_text.tStop = t  # not accounting for scr refresh
            end_text.frameNStop = frameN  # exact frame index
            win.timeOnFlip(end_text, 'tStopRefresh')  # time at next scr refresh
            end_text.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in endComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "end"-------
for thisComponent in endComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('end_text.started', end_text.tStartRefresh)
thisExp.addData('end_text.stopped', end_text.tStopRefresh)

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
