# -*- coding: utf-8 -*-
"""
Created on Sun Nov 13 11:17:51 2016

@author: Anay
"""
import time
import numpy as np
import math
import random
import matplotlib.pyplot as plt
import settings

def cal_euc_distance(x1,x2,y1,y2):
    return math.sqrt((x2-x1)**2+(y2-y1)**2)

## Detector
def detector(enemy,convoy):
    distVec = cal_euc_distance(enemy.x, convoy.x, enemy.y, convoy.y)

# Old code distVec= np.abs(enemy.location-convoy.location);        
#    print np.amax(distVec)
    if distVec < settings.threshold:
        enemy.detected=1        
        convoy.detected=1
#        print enemy.detected
     
    
## Crasher  
def crasher(crash, enemy, convoy):
    if crash==0:
        #TODO: Set threshold for crashing
        if cal_euc_distance(enemy.x, convoy.x, enemy.y, convoy.y) < 2:
            crash=1        
    return crash
    
## Chase
def chase( prevState,currConvLocation ):
    currConv_x=currConvLocation[0]
    currConv_y=currConvLocation[1]
    currPat_x= (prevState%100)/10
    currPat_y=prevState%10
    

    if currPat_x != currConv_x:
        nextPat_x=currPat_x + np.sign(currConv_x-currPat_x);
        nextPat_y=currPat_y;
        
    else:
        nextPat_x=currPat_x;
        nextPat_y=currPat_y + np.sign(currConv_y-currPat_y);
    
    nextPatLoc=np.array([nextPat_x, nextPat_y])
        
    return nextPatLoc
    
## Hash function
def hashFunction(convoy,pat):
    stateNum= 1000*convoy.location[0] + 100*convoy.location[1] + 10*pat.location[0] + pat.location[1]  
    return stateNum
    
## Q learn    
def Qlearn(QM,prevState,action,newState,reward):
    QM[prevState,action]=(1-settings.alpha)*QM[prevState,action] + settings.alpha*(reward + settings.gamma*np.amax(QM[newState,:]))
    
    
### Convoy Movement
#def convoyMovement(QM,prevState):
#    maxVal=np.amax(QM[prevState,:])
#    req_row=QM[prevState,:]
#    idx=np.where(req_row==maxVal)
#    idxRand=np.random.permutation(range(len(idx)))
#    action=idxRand[0]
#    return action
    


## Patrol Movement
def patrolMovement(enemy,convoy,prevState):
#    print enemy.detected
    if enemy.detected !=1:
        enemy.move()    
    
    else:
        newPatLoc=chase(prevState,convoy.location)
        enemy.location=newPatLoc
        
## Convoy Movement                            
def convoyMovement(QM, prevState,convoy):
    if random.uniform(0,1)>settings.epsilon:
        action=random.randrange(0,5)
    else:
        maxVal=np.amax(QM[prevState,:])    
        idx=np.array([])
        for i in range(len(QM[prevState,:])):    
            if QM[prevState,i]==maxVal:
                idx=np.append(idx,[i])   
        idx=idx.astype(int)
        idx=np.random.permutation(idx)
        action=idx[0]
#    print action
    convoy.setAction(action)
#    print action    
    convoy.move()
#    print convoy.kind
    return action
    
##Plotter
def plotter(convoy,enemy):
    for i in range(settings.gridSize[0]+1):
        plt.plot((i-0.5,i-0.5), (-0.5,-0.5+settings.gridSize[1]),'k-')
    
    for i in range(settings.gridSize[0]+1):
        plt.plot((-0.5,-0.5+settings.gridSize[1]),(-0.5+i,-0.5+i),'k-')
        
#    plt.scatter([convoy.location[1]],[convoy.location[0]],color='b')
#    plt.scatter([enemy.location[1]],[enemy.location[0]],color='r')
#    plt.title('Convoy Simulation')

    plt.scatter([convoy.location[0]],[convoy.location[1]],color='b')
    plt.scatter([enemy.location[0]],[enemy.location[1]],color='r')
    plt.title('Convoy Simulation')
    plt.pause(settings.plotDelay)
#    plt.close()
    plt.gcf().clear() 
    
        
        
    
    

    



        

   