#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.2.2),
    on October 13, 2022, at 23:53
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2022.2.2'
expName = 'LDTProject'  # from the Builder filename that created this script
expInfo = {
    'participant': f"{randint(0, 999999):06.0f}",
    'session': '001',
}
# --- Show participant info dialog --
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
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
    originPath='C:\\Users\\adosh\\Desktop\\Lab_Psychology\\Project\\LDTProject_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# --- Setup the Window ---
win = visual.Window(
    size=(1024, 768), fullscr=True, screen=0, 
    winType='pyglet', allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
win.mouseVisible = False
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess
# --- Setup input devices ---
ioConfig = {}

# Setup iohub keyboard
ioConfig['Keyboard'] = dict(use_keymap='psychopy')

ioSession = '1'
if 'session' in expInfo:
    ioSession = str(expInfo['session'])
ioServer = io.launchHubServer(window=win, **ioConfig)
eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard(backend='iohub')

# --- Initialize components for Routine "Introduction" ---
Intro = visual.TextStim(win=win, name='Intro',
    text='Hello,\nThank you for being a part of this study!\nThis project is a part of PSY310 Lab in Psychology course. We ask you to ensure that you are seated in a quiet place for the next 10-15 mins and read the following instructions carefully.\nClick anywhere on the screen to move forward.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
mouse = event.Mouse(win=win)
x, y = [None, None]
mouse.mouseClock = core.Clock()

# --- Initialize components for Routine "Instructions" ---
Instr = visual.TextStim(win=win, name='Instr',
    text="Ensure that you are not disturbed for the next 10-15 mins. \nYou will be performing a simple linguistic study, where you have to find a spoken English word among a group of non-sensical words. The spoken English word might or might not be present.\nIf you feel that the word is present, press 'y' on your keyboard. If you feel that the word is not present, press 'n'.\nContinue to answer in the same way till the experiment comes to an end.\nHAVE FUN!\nClick anywhere on the screen to start the experiment.",
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
mouse_2 = event.Mouse(win=win)
x, y = [None, None]
mouse_2.mouseClock = core.Clock()

# --- Initialize components for Routine "Control" ---
fixation = visual.ShapeStim(
    win=win, name='fixation', vertices='cross',
    size=(0.01, 0.01),
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=0.0, interpolate=True)
Target = visual.TextStim(win=win, name='Target',
    text='',
    font='Open Sans',
    pos=(random()-0.5, random()-0.5), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
key_resp = keyboard.Keyboard()
D1 = visual.TextStim(win=win, name='D1',
    text='',
    font='Open Sans',
    pos=[0,0], height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
D2 = visual.TextStim(win=win, name='D2',
    text='',
    font='Open Sans',
    pos=[0,0], height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
D3 = visual.TextStim(win=win, name='D3',
    text='',
    font='Open Sans',
    pos=[0,0], height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);
D4 = visual.TextStim(win=win, name='D4',
    text='',
    font='Open Sans',
    pos=[0,0], height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-6.0);
D5 = visual.TextStim(win=win, name='D5',
    text='',
    font='Open Sans',
    pos=[0,0], height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-7.0);

# --- Initialize components for Routine "Font_Size" ---
Target_2 = visual.TextStim(win=win, name='Target_2',
    text='',
    font='Open Sans',
    pos=(random()-0.5, random()-0.5), height=1.0, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
fixation_2 = visual.ShapeStim(
    win=win, name='fixation_2', vertices='cross',
    size=(0.01, 0.01),
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-1.0, interpolate=True)
key_resp_2 = keyboard.Keyboard()
D1_2 = visual.TextStim(win=win, name='D1_2',
    text='',
    font='Open Sans',
    pos=[0,0], height=1.0, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
D2_2 = visual.TextStim(win=win, name='D2_2',
    text='',
    font='Open Sans',
    pos=[0,0], height=1.0, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
D3_2 = visual.TextStim(win=win, name='D3_2',
    text='',
    font='Open Sans',
    pos=[0,0], height=1.0, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);
D4_2 = visual.TextStim(win=win, name='D4_2',
    text='',
    font='Open Sans',
    pos=[0,0], height=1.0, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-6.0);
D5_2 = visual.TextStim(win=win, name='D5_2',
    text='',
    font='Open Sans',
    pos=[0,0], height=1.0, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-7.0);

# --- Initialize components for Routine "Speed_Res" ---
fixation_3 = visual.ShapeStim(
    win=win, name='fixation_3', vertices='cross',
    size=(0.01, 0.01),
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=0.0, interpolate=True)
Target_3 = visual.TextStim(win=win, name='Target_3',
    text='',
    font='Open Sans',
    pos=[0,0], height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
key_resp_3 = keyboard.Keyboard()
D1_3 = visual.TextStim(win=win, name='D1_3',
    text='',
    font='Open Sans',
    pos=[0,0], height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
D2_3 = visual.TextStim(win=win, name='D2_3',
    text='',
    font='Open Sans',
    pos=[0,0], height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
D3_3 = visual.TextStim(win=win, name='D3_3',
    text='',
    font='Open Sans',
    pos=[0,0], height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);
D4_3 = visual.TextStim(win=win, name='D4_3',
    text='',
    font='Open Sans',
    pos=[0,0], height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-6.0);
D5_3 = visual.TextStim(win=win, name='D5_3',
    text='',
    font='Open Sans',
    pos=[0,0], height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-7.0);

# --- Initialize components for Routine "Thank_You" ---
text = visual.TextStim(win=win, name='text',
    text='The experiment is now over. Thank you for being a part of this project!',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine 

# --- Prepare to start Routine "Introduction" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# setup some python lists for storing info about the mouse
mouse.x = []
mouse.y = []
mouse.leftButton = []
mouse.midButton = []
mouse.rightButton = []
mouse.time = []
gotValidClick = False  # until a click is received
# keep track of which components have finished
IntroductionComponents = [Intro, mouse]
for thisComponent in IntroductionComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "Introduction" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Intro* updates
    if Intro.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Intro.frameNStart = frameN  # exact frame index
        Intro.tStart = t  # local t and not account for scr refresh
        Intro.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Intro, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'Intro.started')
        Intro.setAutoDraw(True)
    # *mouse* updates
    if mouse.status == NOT_STARTED and t >= 1.0-frameTolerance:
        # keep track of start time/frame for later
        mouse.frameNStart = frameN  # exact frame index
        mouse.tStart = t  # local t and not account for scr refresh
        mouse.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mouse, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.addData('mouse.started', t)
        mouse.status = STARTED
        mouse.mouseClock.reset()
        prevButtonState = mouse.getPressed()  # if button is down already this ISN'T a new click
    if mouse.status == STARTED:  # only update if started and not finished!
        buttons = mouse.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                x, y = mouse.getPos()
                mouse.x.append(x)
                mouse.y.append(y)
                buttons = mouse.getPressed()
                mouse.leftButton.append(buttons[0])
                mouse.midButton.append(buttons[1])
                mouse.rightButton.append(buttons[2])
                mouse.time.append(mouse.mouseClock.getTime())
                
                continueRoutine = False  # abort routine on response
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in IntroductionComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Introduction" ---
for thisComponent in IntroductionComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# store data for thisExp (ExperimentHandler)
thisExp.addData('mouse.x', mouse.x)
thisExp.addData('mouse.y', mouse.y)
thisExp.addData('mouse.leftButton', mouse.leftButton)
thisExp.addData('mouse.midButton', mouse.midButton)
thisExp.addData('mouse.rightButton', mouse.rightButton)
thisExp.addData('mouse.time', mouse.time)
thisExp.nextEntry()
# the Routine "Introduction" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "Instructions" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# setup some python lists for storing info about the mouse_2
mouse_2.x = []
mouse_2.y = []
mouse_2.leftButton = []
mouse_2.midButton = []
mouse_2.rightButton = []
mouse_2.time = []
gotValidClick = False  # until a click is received
# keep track of which components have finished
InstructionsComponents = [Instr, mouse_2]
for thisComponent in InstructionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "Instructions" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Instr* updates
    if Instr.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Instr.frameNStart = frameN  # exact frame index
        Instr.tStart = t  # local t and not account for scr refresh
        Instr.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Instr, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'Instr.started')
        Instr.setAutoDraw(True)
    # *mouse_2* updates
    if mouse_2.status == NOT_STARTED and t >= 1.0-frameTolerance:
        # keep track of start time/frame for later
        mouse_2.frameNStart = frameN  # exact frame index
        mouse_2.tStart = t  # local t and not account for scr refresh
        mouse_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mouse_2, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.addData('mouse_2.started', t)
        mouse_2.status = STARTED
        mouse_2.mouseClock.reset()
        prevButtonState = mouse_2.getPressed()  # if button is down already this ISN'T a new click
    if mouse_2.status == STARTED:  # only update if started and not finished!
        buttons = mouse_2.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                x, y = mouse_2.getPos()
                mouse_2.x.append(x)
                mouse_2.y.append(y)
                buttons = mouse_2.getPressed()
                mouse_2.leftButton.append(buttons[0])
                mouse_2.midButton.append(buttons[1])
                mouse_2.rightButton.append(buttons[2])
                mouse_2.time.append(mouse_2.mouseClock.getTime())
                
                continueRoutine = False  # abort routine on response
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in InstructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Instructions" ---
for thisComponent in InstructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# store data for thisExp (ExperimentHandler)
thisExp.addData('mouse_2.x', mouse_2.x)
thisExp.addData('mouse_2.y', mouse_2.y)
thisExp.addData('mouse_2.leftButton', mouse_2.leftButton)
thisExp.addData('mouse_2.midButton', mouse_2.midButton)
thisExp.addData('mouse_2.rightButton', mouse_2.rightButton)
thisExp.addData('mouse_2.time', mouse_2.time)
thisExp.nextEntry()
# the Routine "Instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_4 = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('loopTemplate1.xlsx'),
    seed=None, name='trials_4')
thisExp.addLoop(trials_4)  # add the loop to the experiment
thisTrial_4 = trials_4.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_4.rgb)
if thisTrial_4 != None:
    for paramName in thisTrial_4:
        exec('{} = thisTrial_4[paramName]'.format(paramName))

for thisTrial_4 in trials_4:
    currentLoop = trials_4
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_4.rgb)
    if thisTrial_4 != None:
        for paramName in thisTrial_4:
            exec('{} = thisTrial_4[paramName]'.format(paramName))
    
    # set up handler to look after randomisation of conditions etc
    trials = data.TrialHandler(nReps=nreps1, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('Control.xlsx'),
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
        
        # --- Prepare to start Routine "Control" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        Target.setText(word_valid)
        key_resp.keys = []
        key_resp.rt = []
        _key_resp_allKeys = []
        D1.setPos((random()-0.5, random()-0.5))
        D1.setText(word_invalid)
        D2.setPos((random()-0.5, random()-0.5))
        D2.setText(word_invalid_1)
        D3.setPos((random()-0.5, random()-0.5))
        D3.setText(word_invalid_2)
        D4.setPos((random()-0.5, random()-0.5))
        D4.setText(word_invalid_3)
        D5.setPos((random()-0.5, random()-0.5))
        D5.setText(word_invalid_4)
        # keep track of which components have finished
        ControlComponents = [fixation, Target, key_resp, D1, D2, D3, D4, D5]
        for thisComponent in ControlComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "Control" ---
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *fixation* updates
            if fixation.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                fixation.frameNStart = frameN  # exact frame index
                fixation.tStart = t  # local t and not account for scr refresh
                fixation.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fixation, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'fixation.started')
                fixation.setAutoDraw(True)
            if fixation.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > fixation.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    fixation.tStop = t  # not accounting for scr refresh
                    fixation.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'fixation.stopped')
                    fixation.setAutoDraw(False)
            
            # *Target* updates
            if Target.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
                # keep track of start time/frame for later
                Target.frameNStart = frameN  # exact frame index
                Target.tStart = t  # local t and not account for scr refresh
                Target.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Target, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Target.started')
                Target.setAutoDraw(True)
            if Target.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Target.tStartRefresh + 7.0-frameTolerance:
                    # keep track of stop time/frame for later
                    Target.tStop = t  # not accounting for scr refresh
                    Target.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'Target.stopped')
                    Target.setAutoDraw(False)
            
            # *key_resp* updates
            waitOnFlip = False
            if key_resp.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp.frameNStart = frameN  # exact frame index
                key_resp.tStart = t  # local t and not account for scr refresh
                key_resp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp.started')
                key_resp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp.status == STARTED and not waitOnFlip:
                theseKeys = key_resp.getKeys(keyList=['y','n'], waitRelease=False)
                _key_resp_allKeys.extend(theseKeys)
                if len(_key_resp_allKeys):
                    key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
                    key_resp.rt = _key_resp_allKeys[-1].rt
                    # was this correct?
                    if (key_resp.keys == str(word_valid_status)) or (key_resp.keys == word_valid_status):
                        key_resp.corr = 1
                    else:
                        key_resp.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # *D1* updates
            if D1.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
                # keep track of start time/frame for later
                D1.frameNStart = frameN  # exact frame index
                D1.tStart = t  # local t and not account for scr refresh
                D1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(D1, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'D1.started')
                D1.setAutoDraw(True)
            if D1.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > D1.tStartRefresh + 7.0-frameTolerance:
                    # keep track of stop time/frame for later
                    D1.tStop = t  # not accounting for scr refresh
                    D1.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'D1.stopped')
                    D1.setAutoDraw(False)
            
            # *D2* updates
            if D2.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
                # keep track of start time/frame for later
                D2.frameNStart = frameN  # exact frame index
                D2.tStart = t  # local t and not account for scr refresh
                D2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(D2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'D2.started')
                D2.setAutoDraw(True)
            if D2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > D2.tStartRefresh + 7.0-frameTolerance:
                    # keep track of stop time/frame for later
                    D2.tStop = t  # not accounting for scr refresh
                    D2.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'D2.stopped')
                    D2.setAutoDraw(False)
            
            # *D3* updates
            if D3.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
                # keep track of start time/frame for later
                D3.frameNStart = frameN  # exact frame index
                D3.tStart = t  # local t and not account for scr refresh
                D3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(D3, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'D3.started')
                D3.setAutoDraw(True)
            if D3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > D3.tStartRefresh + 7.0-frameTolerance:
                    # keep track of stop time/frame for later
                    D3.tStop = t  # not accounting for scr refresh
                    D3.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'D3.stopped')
                    D3.setAutoDraw(False)
            
            # *D4* updates
            if D4.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
                # keep track of start time/frame for later
                D4.frameNStart = frameN  # exact frame index
                D4.tStart = t  # local t and not account for scr refresh
                D4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(D4, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'D4.started')
                D4.setAutoDraw(True)
            if D4.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > D4.tStartRefresh + 7.0-frameTolerance:
                    # keep track of stop time/frame for later
                    D4.tStop = t  # not accounting for scr refresh
                    D4.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'D4.stopped')
                    D4.setAutoDraw(False)
            
            # *D5* updates
            if D5.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
                # keep track of start time/frame for later
                D5.frameNStart = frameN  # exact frame index
                D5.tStart = t  # local t and not account for scr refresh
                D5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(D5, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'D5.started')
                D5.setAutoDraw(True)
            if D5.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > D5.tStartRefresh + 7.0-frameTolerance:
                    # keep track of stop time/frame for later
                    D5.tStop = t  # not accounting for scr refresh
                    D5.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'D5.stopped')
                    D5.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in ControlComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "Control" ---
        for thisComponent in ControlComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if key_resp.keys in ['', [], None]:  # No response was made
            key_resp.keys = None
            # was no response the correct answer?!
            if str(word_valid_status).lower() == 'none':
               key_resp.corr = 1;  # correct non-response
            else:
               key_resp.corr = 0;  # failed to respond (incorrectly)
        # store data for trials (TrialHandler)
        trials.addData('key_resp.keys',key_resp.keys)
        trials.addData('key_resp.corr', key_resp.corr)
        if key_resp.keys != None:  # we had a response
            trials.addData('key_resp.rt', key_resp.rt)
        # the Routine "Control" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed nreps1 repeats of 'trials'
    
    
    # set up handler to look after randomisation of conditions etc
    trials_2 = data.TrialHandler(nReps=nreps2, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('Font_Size.xlsx'),
        seed=None, name='trials_2')
    thisExp.addLoop(trials_2)  # add the loop to the experiment
    thisTrial_2 = trials_2.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
    if thisTrial_2 != None:
        for paramName in thisTrial_2:
            exec('{} = thisTrial_2[paramName]'.format(paramName))
    
    for thisTrial_2 in trials_2:
        currentLoop = trials_2
        # abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
        if thisTrial_2 != None:
            for paramName in thisTrial_2:
                exec('{} = thisTrial_2[paramName]'.format(paramName))
        
        # --- Prepare to start Routine "Font_Size" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        Target_2.setText(word_valid_1)
        Target_2.setHeight(font_size)
        key_resp_2.keys = []
        key_resp_2.rt = []
        _key_resp_2_allKeys = []
        D1_2.setPos((random()-0.5, random()-0.5))
        D1_2.setText(word_invalid_0)
        D1_2.setHeight(font_size)
        D2_2.setPos((random()-0.5, random()-0.5))
        D2_2.setText(word_invalid_01)
        D2_2.setHeight(font_size)
        D3_2.setPos((random()-0.5, random()-0.5))
        D3_2.setText(word_invalid_02)
        D3_2.setHeight(font_size)
        D4_2.setPos((random()-0.5, random()-0.5))
        D4_2.setText(word_invalid_03)
        D4_2.setHeight(font_size)
        D5_2.setPos((random()-0.5, random()-0.5))
        D5_2.setText(word_invalid_04)
        D5_2.setHeight(font_size)
        # keep track of which components have finished
        Font_SizeComponents = [Target_2, fixation_2, key_resp_2, D1_2, D2_2, D3_2, D4_2, D5_2]
        for thisComponent in Font_SizeComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "Font_Size" ---
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *Target_2* updates
            if Target_2.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
                # keep track of start time/frame for later
                Target_2.frameNStart = frameN  # exact frame index
                Target_2.tStart = t  # local t and not account for scr refresh
                Target_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Target_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Target_2.started')
                Target_2.setAutoDraw(True)
            if Target_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Target_2.tStartRefresh + 6.0-frameTolerance:
                    # keep track of stop time/frame for later
                    Target_2.tStop = t  # not accounting for scr refresh
                    Target_2.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'Target_2.stopped')
                    Target_2.setAutoDraw(False)
            
            # *fixation_2* updates
            if fixation_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                fixation_2.frameNStart = frameN  # exact frame index
                fixation_2.tStart = t  # local t and not account for scr refresh
                fixation_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fixation_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'fixation_2.started')
                fixation_2.setAutoDraw(True)
            if fixation_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > fixation_2.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    fixation_2.tStop = t  # not accounting for scr refresh
                    fixation_2.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'fixation_2.stopped')
                    fixation_2.setAutoDraw(False)
            
            # *key_resp_2* updates
            waitOnFlip = False
            if key_resp_2.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_2.frameNStart = frameN  # exact frame index
                key_resp_2.tStart = t  # local t and not account for scr refresh
                key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp_2.started')
                key_resp_2.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_2.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_2.getKeys(keyList=['y','n'], waitRelease=False)
                _key_resp_2_allKeys.extend(theseKeys)
                if len(_key_resp_2_allKeys):
                    key_resp_2.keys = _key_resp_2_allKeys[-1].name  # just the last key pressed
                    key_resp_2.rt = _key_resp_2_allKeys[-1].rt
                    # was this correct?
                    if (key_resp_2.keys == str(word_valid_status_1)) or (key_resp_2.keys == word_valid_status_1):
                        key_resp_2.corr = 1
                    else:
                        key_resp_2.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # *D1_2* updates
            if D1_2.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
                # keep track of start time/frame for later
                D1_2.frameNStart = frameN  # exact frame index
                D1_2.tStart = t  # local t and not account for scr refresh
                D1_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(D1_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'D1_2.started')
                D1_2.setAutoDraw(True)
            if D1_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > D1_2.tStartRefresh + 7.0-frameTolerance:
                    # keep track of stop time/frame for later
                    D1_2.tStop = t  # not accounting for scr refresh
                    D1_2.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'D1_2.stopped')
                    D1_2.setAutoDraw(False)
            
            # *D2_2* updates
            if D2_2.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
                # keep track of start time/frame for later
                D2_2.frameNStart = frameN  # exact frame index
                D2_2.tStart = t  # local t and not account for scr refresh
                D2_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(D2_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'D2_2.started')
                D2_2.setAutoDraw(True)
            if D2_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > D2_2.tStartRefresh + 7.0-frameTolerance:
                    # keep track of stop time/frame for later
                    D2_2.tStop = t  # not accounting for scr refresh
                    D2_2.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'D2_2.stopped')
                    D2_2.setAutoDraw(False)
            
            # *D3_2* updates
            if D3_2.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
                # keep track of start time/frame for later
                D3_2.frameNStart = frameN  # exact frame index
                D3_2.tStart = t  # local t and not account for scr refresh
                D3_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(D3_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'D3_2.started')
                D3_2.setAutoDraw(True)
            if D3_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > D3_2.tStartRefresh + 7.0-frameTolerance:
                    # keep track of stop time/frame for later
                    D3_2.tStop = t  # not accounting for scr refresh
                    D3_2.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'D3_2.stopped')
                    D3_2.setAutoDraw(False)
            
            # *D4_2* updates
            if D4_2.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
                # keep track of start time/frame for later
                D4_2.frameNStart = frameN  # exact frame index
                D4_2.tStart = t  # local t and not account for scr refresh
                D4_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(D4_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'D4_2.started')
                D4_2.setAutoDraw(True)
            if D4_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > D4_2.tStartRefresh + 7.0-frameTolerance:
                    # keep track of stop time/frame for later
                    D4_2.tStop = t  # not accounting for scr refresh
                    D4_2.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'D4_2.stopped')
                    D4_2.setAutoDraw(False)
            
            # *D5_2* updates
            if D5_2.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
                # keep track of start time/frame for later
                D5_2.frameNStart = frameN  # exact frame index
                D5_2.tStart = t  # local t and not account for scr refresh
                D5_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(D5_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'D5_2.started')
                D5_2.setAutoDraw(True)
            if D5_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > D5_2.tStartRefresh + 7.0-frameTolerance:
                    # keep track of stop time/frame for later
                    D5_2.tStop = t  # not accounting for scr refresh
                    D5_2.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'D5_2.stopped')
                    D5_2.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Font_SizeComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "Font_Size" ---
        for thisComponent in Font_SizeComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if key_resp_2.keys in ['', [], None]:  # No response was made
            key_resp_2.keys = None
            # was no response the correct answer?!
            if str(word_valid_status_1).lower() == 'none':
               key_resp_2.corr = 1;  # correct non-response
            else:
               key_resp_2.corr = 0;  # failed to respond (incorrectly)
        # store data for trials_2 (TrialHandler)
        trials_2.addData('key_resp_2.keys',key_resp_2.keys)
        trials_2.addData('key_resp_2.corr', key_resp_2.corr)
        if key_resp_2.keys != None:  # we had a response
            trials_2.addData('key_resp_2.rt', key_resp_2.rt)
        # the Routine "Font_Size" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed nreps2 repeats of 'trials_2'
    
    
    # set up handler to look after randomisation of conditions etc
    trials_3 = data.TrialHandler(nReps=nreps3, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('Speed.xlsx'),
        seed=None, name='trials_3')
    thisExp.addLoop(trials_3)  # add the loop to the experiment
    thisTrial_3 = trials_3.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_3.rgb)
    if thisTrial_3 != None:
        for paramName in thisTrial_3:
            exec('{} = thisTrial_3[paramName]'.format(paramName))
    
    for thisTrial_3 in trials_3:
        currentLoop = trials_3
        # abbreviate parameter names if possible (e.g. rgb = thisTrial_3.rgb)
        if thisTrial_3 != None:
            for paramName in thisTrial_3:
                exec('{} = thisTrial_3[paramName]'.format(paramName))
        
        # --- Prepare to start Routine "Speed_Res" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        Target_3.setPos((random()-0.5, random()-0.5))
        Target_3.setText(word_valid_2)
        key_resp_3.keys = []
        key_resp_3.rt = []
        _key_resp_3_allKeys = []
        D1_3.setPos((random()-0.5, random()-0.5))
        D1_3.setText(word_invalid_00)
        D2_3.setPos((random()-0.5, random()-0.5))
        D2_3.setText(word_invalid_001)
        D3_3.setPos((random()-0.5, random()-0.5))
        D3_3.setText(word_invalid_002)
        D4_3.setPos((random()-0.5, random()-0.5))
        D4_3.setText(word_invalid_003)
        D5_3.setPos((random()-0.5, random()-0.5))
        D5_3.setText(word_invalid_004)
        # keep track of which components have finished
        Speed_ResComponents = [fixation_3, Target_3, key_resp_3, D1_3, D2_3, D3_3, D4_3, D5_3]
        for thisComponent in Speed_ResComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "Speed_Res" ---
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *fixation_3* updates
            if fixation_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                fixation_3.frameNStart = frameN  # exact frame index
                fixation_3.tStart = t  # local t and not account for scr refresh
                fixation_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fixation_3, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'fixation_3.started')
                fixation_3.setAutoDraw(True)
            if fixation_3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > fixation_3.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    fixation_3.tStop = t  # not accounting for scr refresh
                    fixation_3.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'fixation_3.stopped')
                    fixation_3.setAutoDraw(False)
            
            # *Target_3* updates
            if Target_3.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
                # keep track of start time/frame for later
                Target_3.frameNStart = frameN  # exact frame index
                Target_3.tStart = t  # local t and not account for scr refresh
                Target_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Target_3, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Target_3.started')
                Target_3.setAutoDraw(True)
            if Target_3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Target_3.tStartRefresh + speed_res-frameTolerance:
                    # keep track of stop time/frame for later
                    Target_3.tStop = t  # not accounting for scr refresh
                    Target_3.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'Target_3.stopped')
                    Target_3.setAutoDraw(False)
            
            # *key_resp_3* updates
            waitOnFlip = False
            if key_resp_3.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_3.frameNStart = frameN  # exact frame index
                key_resp_3.tStart = t  # local t and not account for scr refresh
                key_resp_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_3, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp_3.started')
                key_resp_3.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_3.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_3.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_3.getKeys(keyList=['y','n'], waitRelease=False)
                _key_resp_3_allKeys.extend(theseKeys)
                if len(_key_resp_3_allKeys):
                    key_resp_3.keys = _key_resp_3_allKeys[-1].name  # just the last key pressed
                    key_resp_3.rt = _key_resp_3_allKeys[-1].rt
                    # was this correct?
                    if (key_resp_3.keys == str(word_valid_status_2)) or (key_resp_3.keys == word_valid_status_2):
                        key_resp_3.corr = 1
                    else:
                        key_resp_3.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # *D1_3* updates
            if D1_3.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
                # keep track of start time/frame for later
                D1_3.frameNStart = frameN  # exact frame index
                D1_3.tStart = t  # local t and not account for scr refresh
                D1_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(D1_3, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'D1_3.started')
                D1_3.setAutoDraw(True)
            if D1_3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > D1_3.tStartRefresh + speed_res-frameTolerance:
                    # keep track of stop time/frame for later
                    D1_3.tStop = t  # not accounting for scr refresh
                    D1_3.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'D1_3.stopped')
                    D1_3.setAutoDraw(False)
            
            # *D2_3* updates
            if D2_3.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
                # keep track of start time/frame for later
                D2_3.frameNStart = frameN  # exact frame index
                D2_3.tStart = t  # local t and not account for scr refresh
                D2_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(D2_3, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'D2_3.started')
                D2_3.setAutoDraw(True)
            if D2_3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > D2_3.tStartRefresh + speed_res-frameTolerance:
                    # keep track of stop time/frame for later
                    D2_3.tStop = t  # not accounting for scr refresh
                    D2_3.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'D2_3.stopped')
                    D2_3.setAutoDraw(False)
            
            # *D3_3* updates
            if D3_3.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
                # keep track of start time/frame for later
                D3_3.frameNStart = frameN  # exact frame index
                D3_3.tStart = t  # local t and not account for scr refresh
                D3_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(D3_3, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'D3_3.started')
                D3_3.setAutoDraw(True)
            if D3_3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > D3_3.tStartRefresh + speed_res-frameTolerance:
                    # keep track of stop time/frame for later
                    D3_3.tStop = t  # not accounting for scr refresh
                    D3_3.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'D3_3.stopped')
                    D3_3.setAutoDraw(False)
            
            # *D4_3* updates
            if D4_3.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
                # keep track of start time/frame for later
                D4_3.frameNStart = frameN  # exact frame index
                D4_3.tStart = t  # local t and not account for scr refresh
                D4_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(D4_3, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'D4_3.started')
                D4_3.setAutoDraw(True)
            if D4_3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > D4_3.tStartRefresh + speed_res-frameTolerance:
                    # keep track of stop time/frame for later
                    D4_3.tStop = t  # not accounting for scr refresh
                    D4_3.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'D4_3.stopped')
                    D4_3.setAutoDraw(False)
            
            # *D5_3* updates
            if D5_3.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
                # keep track of start time/frame for later
                D5_3.frameNStart = frameN  # exact frame index
                D5_3.tStart = t  # local t and not account for scr refresh
                D5_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(D5_3, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'D5_3.started')
                D5_3.setAutoDraw(True)
            if D5_3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > D5_3.tStartRefresh + speed_res-frameTolerance:
                    # keep track of stop time/frame for later
                    D5_3.tStop = t  # not accounting for scr refresh
                    D5_3.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'D5_3.stopped')
                    D5_3.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Speed_ResComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "Speed_Res" ---
        for thisComponent in Speed_ResComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if key_resp_3.keys in ['', [], None]:  # No response was made
            key_resp_3.keys = None
            # was no response the correct answer?!
            if str(word_valid_status_2).lower() == 'none':
               key_resp_3.corr = 1;  # correct non-response
            else:
               key_resp_3.corr = 0;  # failed to respond (incorrectly)
        # store data for trials_3 (TrialHandler)
        trials_3.addData('key_resp_3.keys',key_resp_3.keys)
        trials_3.addData('key_resp_3.corr', key_resp_3.corr)
        if key_resp_3.keys != None:  # we had a response
            trials_3.addData('key_resp_3.rt', key_resp_3.rt)
        # the Routine "Speed_Res" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed nreps3 repeats of 'trials_3'
    
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trials_4'


# --- Prepare to start Routine "Thank_You" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# keep track of which components have finished
Thank_YouComponents = [text]
for thisComponent in Thank_YouComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "Thank_You" ---
while continueRoutine and routineTimer.getTime() < 11.0:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text* updates
    if text.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
        # keep track of start time/frame for later
        text.frameNStart = frameN  # exact frame index
        text.tStart = t  # local t and not account for scr refresh
        text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'text.started')
        text.setAutoDraw(True)
    if text.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text.tStartRefresh + 10.0-frameTolerance:
            # keep track of stop time/frame for later
            text.tStop = t  # not accounting for scr refresh
            text.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text.stopped')
            text.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Thank_YouComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Thank_You" ---
for thisComponent in Thank_YouComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-11.000000)

# --- End experiment ---
# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
if eyetracker:
    eyetracker.setConnectionState(False)
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
