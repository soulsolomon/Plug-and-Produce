import PySide
from PySide import QtCore, QtGui
import FreeCAD
import FreeCADGui
import nail, drillingOperation, screwing, pickPlace, makedrill
import os

class SelectCADPart:
	def __init__(self):
		pass
        
	def giveInform():
        FreeCAD.openDocument('C:/Users/Mashiur/Desktop/ThesisCAD/TreeCell.FCStd')
        FreeCADGui.Selection.addSelection('TreeCell','b_motor_001_')
        sel = FreeCADGui.Selection.getSelection()
        placeMotor = sel[0].Placement.Base
        FreeCAD.Console.PrintMessage(sel[0].Placement.Base)
        a = placeMotor[0]
        return a
    '''b = placeMotor[1]
    c = placeMotor[2]
    pos = [a,b,c]
        
    placeMotorOrient = sel[0].Placement.Rotation
    #FreeCAD.Console.PrintMessage(sel[0].Placement.Rotation)
    rx = placeMotorOrient[0]
    ry = placeMotorOrient[1]
    rz = placeMotorOrient[2]
    rot = [rx,ry,rz]
    pose = "Pos [" + str(pos) + "Rot" + str(rot)
    print(a)'''
		