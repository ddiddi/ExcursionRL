# -*- coding: utf-8 -*-
"""
Created on Sun Nov 13 11:23:23 2016
This contains Objects, that is, the convoy and patrol agents as well as various functions associated with them
@author: Anay
"""
import numpy as np
import settings
class agent(object):
    
    def __init__(self,location, kind, detected):
        self.direction= 'left';
        self.location=location;
        self.kind=kind;
        self.detected=detected;
        
    def setAction(self,numAction):
        if numAction == 0:
            self.direction = 'stay'
        elif numAction == 1:
#            print'hey,told to move up'
            self.direction = 'up'
#            print self.direction
        elif numAction == 2:
            self.direction = 'down'
        elif numAction == 3:
            self.direction = 'left'
        elif numAction == 4:
            self.direction = 'right'
        else:
            self.direction = 'error'
            
    def move(self):
        GRID_SIZE=settings.gridSize
            
        if self.kind == 'convoy':
            if self.direction == 'left':
                if self.location[0] > 0:
                    self.location[0] = self.location[0] - 1
                    
            elif self.direction == 'right':
                if self.location[0] < GRID_SIZE[0]-1:
                        self.location[0] = self.location[0] + 1
                    
            elif self.direction == 'down':
                if self.location[1] > 0:
                    self.location[1] = self.location[1] - 1
                    
            elif self.direction == 'up':
#                print'hey,moved up'
                if self.location[1] < GRID_SIZE[1]-1:
                    self.location[1] = self.location[1]+ 1
        
                    
                
        else: #It is a patrol
            if self.direction == 'left':
                if self.location[0] > 0:                    
                    self.location[0] = self.location[0] - 1
                     
                else:
                    self.direction = 'right'
                    
                    
            elif self.direction == 'right':
                if self.location[0] < GRID_SIZE[0]-1:
                    self.location[0] = self.location[0] + 1
                else:
                    self.direction = 'left'
                   
                    
                
                
           
            
                
            
        
        
    