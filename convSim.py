# -*- coding: utf-8 -*-
"""
Created on Tue Nov 15 16:19:20 2016

@author: anayp2
"""
import random
import numpy as np
import matplotlib.pyplot as plt
from agent import agent
import func
import settings
plotting=False
reward=0
QM=np.zeros((9999,5))
#%% Learning loop starts
for i in range(settings.episodes):
    active=True                                  # State of the Game
    detected=0
    crash=0
#%% Initialize positions for each episode
    conInit= np.array([random.randrange(0,settings.gridSize[0]),0])
    patInit=np.array([random.randrange(0,settings.gridSize[0]),random.randrange(settings.gridSize[1]-1)])
    enemy=agent(patInit,'enemy',detected)
    convoy=agent( conInit,'convoy',detected)
#    print "initiat"+ str(convoy.location)+str(enemy.location)
    crash=func.crasher(crash, enemy, convoy ) #crash from beginning
    func.detector(enemy,convoy)               #Detected from beginning
#%% Start the episode
    timer=0
    while active and timer<=settings.maxSteps:
        if plotting:
            func.plotter(convoy,enemy) 
            
        prevState=func.hashFunction(convoy,enemy) # Store in form of look up table
        action=func.convoyMovement(QM,prevState,convoy)  #convoy movement
        crash=func.crasher(crash, enemy, convoy ) #crash ?
        func.detector(enemy,convoy)               #Detected ?
        func.patrolMovement(enemy,convoy,prevState) #patrol movement
        crash=func.crasher(crash, enemy, convoy ) #crash ?
        func.detector(enemy,convoy)               #Detected ?
        newState=func.hashFunction(convoy,enemy)  # Store the new state in look up table
        if crash or timer==settings.maxSteps:
            active=False                              #Game ends
            reward=settings.losePenalty
            if plotting:
                func.plotter(convoy,enemy)
                plt.close()
        elif convoy.location[1]==settings.gridSize[1]-1:
            active=False
            reward=settings.winReward
            if plotting:
                func.plotter(convoy,enemy)
                plt.close()
        else:
           reward=settings.livReward 
#        print convoy.location,enemy.location  
        func.Qlearn(QM,prevState,action,newState,reward) #Update Q matrix
        timer=timer+1
        
           
            
            

            
                
            
        
        
        
        
            
            
            
#            timer=timer+1
        
#plt.close()     Use this to close the empty plot after each episode    
    
