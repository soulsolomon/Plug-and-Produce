# -*- coding: utf-8 -*-

"""
Created on Tue Apr 27 21:05:10 2021

@author: Mashiur
"""

import FreeCAD, FreeCADGui
from PySide import QtCore, QtGui
import GetCoordinates, selectMotor, GetCoordinates2, CoValueCreation
import json, math

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(563, 613)
        self.title = QtGui.QLabel(Dialog)
        self.title.setGeometry(QtCore.QRect(140, 20, 221, 51))
        self.title.setObjectName("title")
        self.distAppartNail = QtGui.QLabel(Dialog)
        self.distAppartNail.setGeometry(QtCore.QRect(30, 190, 101, 41))
        self.distAppartNail.setObjectName("distance")
        self.StartX = QtGui.QLabel(Dialog)
        self.StartX.setGeometry(QtCore.QRect(40, 280, 61, 16))
        self.StartX.setObjectName("StartX")
        self.StartY = QtGui.QLabel(Dialog)
        self.StartY.setGeometry(QtCore.QRect(40, 320, 71, 21))
        self.StartY.setObjectName("StartY")
        self.StartZ = QtGui.QLabel(Dialog)
        self.StartZ.setGeometry(QtCore.QRect(40, 370, 55, 16))
        self.StartZ.setObjectName("StartZ")
        self.EndX = QtGui.QLabel(Dialog)
        self.EndX.setGeometry(QtCore.QRect(290, 280, 55, 16))
        self.EndX.setObjectName("EndX")
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(290, 330, 55, 16))
        self.label.setObjectName("label")
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(290, 370, 55, 16))
        self.label_2.setObjectName("label_2")
        self.spX = QtGui.QLineEdit(Dialog)
        self.spX.setGeometry(QtCore.QRect(120, 280, 113, 22))
        self.spX.setObjectName("spX")
        self.spY = QtGui.QLineEdit(Dialog)
        self.spY.setGeometry(QtCore.QRect(120, 320, 113, 22))
        self.spY.setObjectName("spY")
        self.spZ = QtGui.QLineEdit(Dialog)
        self.spZ.setGeometry(QtCore.QRect(120, 370, 113, 22))
        self.spZ.setObjectName("spZ")
        self.distNails = QtGui.QLineEdit(Dialog)
        self.distNails.setGeometry(QtCore.QRect(140, 200, 113, 22))
        self.distNails.setObjectName("distNails")
        self.epX = QtGui.QLineEdit(Dialog)
        self.epX.setGeometry(QtCore.QRect(380, 270, 113, 22))
        self.epX.setObjectName("epX")
        self.epY = QtGui.QLineEdit(Dialog)
        self.epY.setGeometry(QtCore.QRect(380, 320, 113, 22))
        self.epY.setObjectName("epY")
        self.epZ = QtGui.QLineEdit(Dialog)
        self.epZ.setGeometry(QtCore.QRect(380, 370, 113, 22))
        self.epZ.setObjectName("epZ")
        self.MakeNail = QtGui.QPushButton(Dialog)
        self.MakeNail.setGeometry(QtCore.QRect(210, 560, 161, 28))
        self.MakeNail.setObjectName("MakeNail")
        self.rX = QtGui.QLabel(Dialog)
        self.rX.setGeometry(QtCore.QRect(40, 420, 61, 16))
        self.rX.setObjectName("rX")
        self.rY = QtGui.QLabel(Dialog)
        self.rY.setGeometry(QtCore.QRect(40, 460, 55, 16))
        self.rY.setObjectName("rY")
        self.rZ = QtGui.QLabel(Dialog)
        self.rZ.setGeometry(QtCore.QRect(40, 510, 61, 16))
        self.rZ.setObjectName("rZ")
        self.rotX = QtGui.QLineEdit(Dialog)
        self.rotX.setGeometry(QtCore.QRect(120, 420, 113, 22))
        self.rotX.setObjectName("rotX")
        self.rotY = QtGui.QLineEdit(Dialog)
        self.rotY.setGeometry(QtCore.QRect(120, 460, 113, 22))
        self.rotY.setObjectName("rotY")
        self.rotZ = QtGui.QLineEdit(Dialog)
        self.rotZ.setGeometry(QtCore.QRect(120, 500, 113, 22))
        self.rotZ.setObjectName("rotZ")
        self.rotZ_2 = QtGui.QLineEdit(Dialog)
        self.rotZ_2.setGeometry(QtCore.QRect(380, 500, 113, 22))
        self.rotZ_2.setObjectName("rotZ_2")
        self.rotX_2 = QtGui.QLineEdit(Dialog)
        self.rotX_2.setGeometry(QtCore.QRect(380, 420, 113, 22))
        self.rotX_2.setObjectName("rotX_2")
        self.rotY_2 = QtGui.QLineEdit(Dialog)
        self.rotY_2.setGeometry(QtCore.QRect(380, 460, 113, 22))
        self.rotY_2.setObjectName("rotY_2")
        self.rZ_2 = QtGui.QLabel(Dialog)
        self.rZ_2.setGeometry(QtCore.QRect(290, 500, 61, 16))
        self.rZ_2.setObjectName("rZ_2")
        self.rX_2 = QtGui.QLabel(Dialog)
        self.rX_2.setGeometry(QtCore.QRect(290, 420, 61, 16))
        self.rX_2.setObjectName("rX_2")
        self.rY_2 = QtGui.QLabel(Dialog)
        self.rY_2.setGeometry(QtCore.QRect(290, 460, 55, 16))
        self.rY_2.setObjectName("rY_2")
        self.Nailid = QtGui.QLabel(Dialog)
        self.Nailid.setGeometry(QtCore.QRect(300, 190, 71, 31))
        self.Nailid.setObjectName("Nailid")
        self.nailidValue = QtGui.QLineEdit(Dialog)
        self.nailidValue.setGeometry(QtCore.QRect(380, 200, 113, 22))
        self.nailidValue.setObjectName("nailidValue")
        
        self.pushInform = QtGui.QPushButton(Dialog)
        self.pushInform.setGeometry(QtCore.QRect(50, 120, 81, 21))
        self.pushInform.setObjectName("pushInform")
        
        # self.inform = QtGui.QLabel(Dialog)
        # self.inform.setGeometry(QtCore.QRect(50, 120, 81, 21))
        # self.inform.setObjectName("inform")
        self.informMessage = QtGui.QLabel(Dialog)
        self.informMessage.setGeometry(QtCore.QRect(170, 120, 331, 21))
        self.informMessage.setObjectName("informMessage")

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.pushInform,QtCore.SIGNAL("pressed()"),self.extractInf)
        QtCore.QObject.connect(self.MakeNail,QtCore.SIGNAL("pressed()"),self.export2Jason)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.title.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:18pt; font-weight:600; color:#0000ff;\">Nail Operation</span></p></body></html>"))
        self.distAppartNail.setText(_translate("Dialog", "DistanceNails"))
        self.StartX.setText(_translate("Dialog", "StartPosX"))
        self.StartY.setText(_translate("Dialog", "StartPosY"))
        self.StartZ.setText(_translate("Dialog", "StartPosZ"))
        self.EndX.setText(_translate("Dialog", "EndPosX"))
        self.label.setText(_translate("Dialog", "EndPosY"))
        self.label_2.setText(_translate("Dialog", "EndPosZ"))
        # making default value to zero in the positional dialog box
        self.spX.setText(_translate("Dialog", str(0), None))
        self.spY.setText(_translate("Dialog", str(0), None))
        self.spZ.setText(_translate("Dialog", str(0), None))
        self.epX.setText(_translate("Dialog", str(0), None))
        self.epY.setText(_translate("Dialog", str(0), None))
        self.epZ.setText(_translate("Dialog", str(0), None))
        # making default value to zero for orientational dialogue box
        self.rotX.setText(_translate("Dialog", str(0), None))
        self.rotX_2.setText(_translate("Dialog", str(0), None))
        self.rotY.setText(_translate("Dialog", str(0), None))
        self.rotY_2.setText(_translate("Dialog", str(0), None))
        self.rotZ.setText(_translate("Dialog", str(0), None))
        self.rotZ_2.setText(_translate("Dialog", str(0), None))
        # default value of the distance of nails 100, user can later change this in the dialogue box
        self.distNails.setText(_translate("Dialog", str(100), None))
        self.nailidValue.setText(_translate("Dialog", str(0), None))
        
        self.MakeNail.setText(_translate("Dialog", "StartNailOperation"))
        self.rX.setText(_translate("Dialog", "StartRotX"))
        self.rY.setText(_translate("Dialog", "StartRotY"))
        self.rZ.setText(_translate("Dialog", "StartRotZ"))
        self.rZ_2.setText(_translate("Dialog", "EndRotZ"))
        self.rX_2.setText(_translate("Dialog", "EndRotX"))
        self.rY_2.setText(_translate("Dialog", "EndRotY"))
        self.Nailid.setText(_translate("Dialog", "Nail_ID"))
        self.pushInform.setText(_translate("Dialog","Information"))
  
        self.informMessage.setText(_translate("Dialog", "Information Message to the user"))

    def extractInf(self):
        _translate = QtCore.QCoreApplication.translate
        # import information from external file
        
        # nail1 value needs to be imported manually here
        # The nail1 value can be seen in the CAD tree view, and the python console in FreeCAD provides the information 
        # as Gui.Selection.addSelection('TreeCell','b_screw_001_004')
        obj1 = GetCoordinates.InformCoordinates('b_screw_001_004') # Calling seperate python file class and send the string as input
        obj1 = obj1.giveInform()
        FreeCAD.Console.PrintMessage("First Nail location is successfully imported")
        ob1 = "Nail1: Pos ["+str(obj1[0])+" "+ str(obj1[1])+ " " + str(obj1[2]) + "]"+ " " +"Rot [" + str(obj1[3]) + " " + str(obj1[4]) + " " + str(obj1[5]) +"]"
        FreeCAD.Console.PrintMessage(ob1)
        #Extract information for the first nail position to the dialog line-edit box
        self.spX.setText(_translate("Dialog", str(obj1[0]), None))
        self.spY.setText(_translate("Dialog", str(obj1[1]), None))
        self.spZ.setText(_translate("Dialog", str(obj1[2]), None))
        self.rotX.setText(_translate("Dialog", str(obj1[3]), None))
        self.rotY.setText(_translate("Dialog", str(obj1[4]), None))
        self.rotZ.setText(_translate("Dialog", str(obj1[5]), None))
        
        # Extract information for the last nail position to the dialogue box
        # same 
        obj2 = GetCoordinates2.InformCoordinates('b_screw_001_')
        obj2 = obj2.giveInform()
        # Extract information from the CAD and set in the dialogue box
        self.epX.setText(_translate("Dialog", str(obj2[0]), None))
        self.epY.setText(_translate("Dialog", str(obj2[1]), None))
        self.epZ.setText(_translate("Dialog", str(obj2[2]), None))
        self.rotX_2.setText(_translate("Dialog", str(obj2[3]), None))
        self.rotY_2.setText(_translate("Dialog", str(obj2[4]), None))
        self.rotZ_2.setText(_translate("Dialog", str(obj2[5]), None))
        FreeCAD.Console.PrintMessage("Last Nail Location is successfully Imported")
        ob2 = "NailEnd: Pos ["+str(obj2[0])+" "+ str(obj2[1])+ " " + str(obj2[2]) + "]"+ " " +"Rot [" + str(obj2[3]) + " " + str(obj2[4]) + " " + str(obj2[5]) +"]"
        FreeCAD.Console.PrintMessage(ob2)
        self.informMessage.setText(_translate("Dialog","Successfully Imported"))
        # clear the selection for next operation
        FreeCADGui.Selection.ClearSelection()
    
    def export2Jason(self):
        ''' This function is aimed to send the extracted information to JSON format in local hardrive'''
        _translate = QtCore.QCoreApplication.translate
        FreeCAD.Console.PrintMessage("Please insert the coordinates value")
        try:
            # Position of the first nail
            x_s = float(self.spX.text())
            y_s = float(self.spY.text())
            z_s = float(self.spZ.text())
            
            
            # angle of the first nail
            ax_s = float(self.rotX.text())
            ay_s = float(self.rotY.text())
            az_s = float(self.rotZ.text())
            
            
            # Position of the last nail
            x_e = float(self.epX.text())
            y_e = float(self.epY.text())
            z_e = float(self.epZ.text())
            
            
            # angle of the last nail
            ax_e = float(self.rotX_2.text())
            ay_e = float(self.rotY_2.text())
            az_e = float(self.rotZ_2.text())
            
            # distance between nails
            d = int(self.distNails.text())
            
            # enter the nail id
            nid = float(self.nailidValue.text())
            
            
        except ValueError:
           #FreeCAD.Console.PrintMessage("Error! values must be valid numbers!")
           self.informMessage.setText(_translate("Dialog","Error! Values must be valid numbers"))
        else:
            # print("The positions are successfully imported")
            FreeCAD.Console.PrintMessage("The positions are successfully imported")
            f = open("C:/Users/Mashiur/Music/JasonFiles/nails.JSON",mode='w',encoding='utf-8')
            #FreeCAD.Console.PrintMessage("distance apart is " + str(d))
            # objective is to create coordinates based on the distnace apart between nails
            # using pythagorous formula           
            xdist = x_e - x_s
            #FreeCAD.Console.PrintMessage("x distance value " + str(xdist))
            ydist = y_e - y_s
            #FreeCAD.Console.PrintMessage("y distance value " + str(ydist))
            # number of nails
            nsqrt = (xdist**2+ydist**2) / d**2
            n = math.sqrt(nsqrt)+ 1 # considering the first nail operation as well
            # n provides the floating value, so the number should be converted to int
            n = int(n)
            FreeCAD.Console.PrintMessage(" Number of nails are : "+ str(n))
      
            # calling seperate funstion to get the coordinate value
            arrValue = CoValueCreation.ValueCreate(x_s,x_e,d,n)
            arrX = arrValue.valueArray()
            FreeCAD.Console.PrintMessage("  X positions are" + str(arrX))
            
            arrValue = CoValueCreation.ValueCreate(y_s,y_e,d,n)
            arrY = arrValue.valueArray()
            FreeCAD.Console.PrintMessage("  Y positions are" + str(arrY))
            
            arrValue = CoValueCreation.ValueCreate(z_s,z_e,d,n)
            arrZ = arrValue.valueArray()
            FreeCAD.Console.PrintMessage("  Z positions are" + str(arrZ))
            
            # creating array object of rotation parameters
            RX_value = [ax_s for ar in range(0,n)]
            RY_value = [ay_s for ar in range(0,n)]
            RZ_value = [az_s for ar in range(0,n)]
           
            
            # Creating a dictionary object to import it in JSON
            arr = [0 for ar in range(0,n)]
            
            for ii in range(0,n):
                arr[ii] = {
                    "Name" : "Nail"+ str(ii+1), # to create name string value
                    "Type": "Location",
                    "X": arrX[ii],
                    "Y": arrY[ii],
                    "Z": arrZ[ii],
                    "RX": RX_value[ii],
                    "RY": RY_value[ii],
                    "RZ": RZ_value[ii]
                    }
            # Creating JSON agent as library functions
            jsonagents = {"type": "Locations",
                    "ID" : nid, # Nail id 
                    "Locations": arr}
                    
            FreeCAD.Console.PrintMessage(" list dictionary " + str(jsonagents)) 
            # convert into JSON from python library:
            y = json.dumps(jsonagents,indent = 4)
            f.write(y)
            f.close()
            self.informMessage.setText(_translate("Dialog","JSON file is created"))
            FreeCAD.Console.PrintMessage("The JSON file is created")

class makejson():
  def __init__(self):
      self.d = QtGui.QWidget()
      self.ui = Ui_Dialog()
      self.ui.setupUi(self.d)
      self.d.show()

