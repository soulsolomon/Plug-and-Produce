import PySide
from PySide import QtCore, QtGui
import FreeCAD
import FreeCADGui

import getAngles
import os

# Create a object oriented class model 

class InformCoordinates:
    ''' This class method is aimed to extract the information from CAD and send to the calling function'''
    
    def __init__(self, name):
        self.name = name
        
    def giveInform(self):
        # local address of getting the freeCAD drawing
        
        FreeCAD.openDocument('C:/Program Files/FreeCAD 0.19/Mod/Plug-and-Produce/ProjectTreeCell.FCStd')
        # Name of the drawing and respective drawing from the tree view,
        # Tree view name can be seen by simply clicking this drawing
        #FreeCADGui.Selection.addSelection('TreeCell','b_motor_001_')
        FreeCADGui.Selection.addSelection('ProjectTreeCell',self.name)
        FreeCAD.Console.PrintMessage("Selection is done")
        sel = FreeCADGui.Selection.getSelection()
        # returns a array of three coordinates of positions
        placeMotor = sel[0].Placement.Base
        FreeCAD.Console.PrintMessage("/n")
        FreeCAD.Console.PrintMessage(sel[0].Placement.Base)
        a = placeMotor[0]
        b = placeMotor[1]
        c = placeMotor[2]
        
        # returns homogeneus matrix from with elements naming A
        orientMotor = sel[0].Placement.Matrix
        # Print a freeCAD console message 
        FreeCAD.Console.PrintMessage(sel[0].Placement.Matrix)
        
        # getting the matrix information of angles from the CAD geometry
        r11 = orientMotor.A11
        r12 = orientMotor.A12
        r13 = orientMotor.A13
        r21 = orientMotor.A21
        r22 = orientMotor.A22
        r23 = orientMotor.A23
        r31 = orientMotor.A31
        r32 = orientMotor.A32
        r33 = orientMotor.A33
        
        matVal = getAngles.MatrixOperation(r11,r12,r13,r21,r22,r23,r31,r32,r33)
        # getting information from the external function
        rollPitchYaw = matVal.createMatrix()
        rx = rollPitchYaw[0]
        ry = rollPitchYaw[1]
        rz = rollPitchYaw[2]
        
        return [a,b,c,rx,ry,rz]
        #return "Pos ["+str(a)+" "+ str(b)+ " " + str(c) + "]"+ " " +"Rot [" + str(rx) + " " + str(ry) + " " + str(rz) +"]"
            
