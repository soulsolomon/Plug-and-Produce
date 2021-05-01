# -*- coding: utf-8 -*-
"""
Created on Wed Apr 21 01:48:02 2021

@author: Mashiur
"""

import numpy as np
import math

# Creating a matrix

class MatrixOperation:
    ''' This generates the roll-pitch-yaw angles from a rotational matrix'''
    def __init__(self,a11,a12,a13,a21,a22,a23,a31,a32,a33):
        ''' Constructor of the class '''
        self.a11 = a11
        self.a12 = a12
        self.a13 = a13
        self.a21 = a21
        self.a22 = a22
        self.a23 = a23
        self.a31 = a31
        self.a32 = a32
        self.a33 = a33

    def createMatrix(self):
        # creation of a matrix from the external input
        mat = np.array([[self.a11, self.a12, self.a13],
                        [self.a21, self.a22, self.a23],
                        [self.a31, self.a32, self.a33]])
        # calculation of a parameter that is needed to create pitch angles
        sqt = math.sqrt(mat[2,1]*mat[2,1] + mat[2,2]**2)
        # creating angles from matrix 
        roll = math.atan2(mat[1,0],mat[0,0]) # rotation around z axis
        pitch = math.atan(-mat[2,0]/sqt)    # rotation around y axis
        yaw = math.atan2(mat[2,1],mat[2,0]) # rotation around x axis
        # creation of array to output the solution
        roll_pitch_yaw = [roll, pitch, yaw]
        return roll_pitch_yaw