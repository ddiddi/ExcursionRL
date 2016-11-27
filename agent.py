# -*- coding: utf-8 -*-
"""
Created on Sun Nov 13 11:23:23 2016
This contains Objects, that is, the convoy and patrol agents as well as various functions associated with them
@author: Anay
"""
import numpy as np
import math
import settings
class agent(object):
    
    def __init__(self,x=None, y=None, kind=None, detected=None):
        self.direction= 0       #Angle in 0-360. Standard counter clockwise measurement. Executed after move is called
        self.x = x				# X Position
        self.y = y				# Y Position
        self.kind=kind;
        self.detected=detected;
        
    def setAction(self,numAction, new_direction):
        if numAction == 0:
            self.direction = 'stay'
        elif new_direction >=0 and new_direction < 360:
            self.direction = new_direction
        else:
            self.direction = 'error'
            
    def move(self):
        new_x = self.x + math.cos(math.radians(self.direction))
        new_y = self.y + math.sin(math.radians(self.direction))

        #TODO: Set Grid boundaries in global instead of locally here
        if new_x > 0 and new_x < 10:
        	self.x = new_x
        if new_y > 0 and new_y < 10:
        	self.y = new_y
              
                    
                
                
           
            
                
            
        
        
    