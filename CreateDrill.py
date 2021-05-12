# -*- coding: utf-8 -*-
"""
Created on Tue Apr 27 22:30:55 2021

@author: Mashiur
"""

import FreeCAD, Part
from PySide import QtCore, QtGui
import GetCoordinates
import json

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(766, 479)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        Dialog.setFont(font)
        self.heading = QtGui.QLabel(Dialog)
        self.heading.setGeometry(QtCore.QRect(230, -10, 411, 61))
        self.heading.setObjectName("heading")
        self.drillX = QtGui.QLabel(Dialog)
        self.drillX.setGeometry(QtCore.QRect(80, 260, 101, 20))
        self.drillX.setObjectName("drillX")
        self.drillY = QtGui.QLabel(Dialog)
        self.drillY.setGeometry(QtCore.QRect(80, 310, 101, 20))
        self.drillY.setObjectName("drillY")
        self.drillZ = QtGui.QLabel(Dialog)
        self.drillZ.setGeometry(QtCore.QRect(80, 360, 101, 20))
        self.drillZ.setObjectName("drillZ")
        self.drillAngleX = QtGui.QLabel(Dialog)
        self.drillAngleX.setGeometry(QtCore.QRect(440, 270, 91, 16))
        self.drillAngleX.setObjectName("drillAngleX")
        self.drillAngleY = QtGui.QLabel(Dialog)
        self.drillAngleY.setGeometry(QtCore.QRect(440, 310, 91, 21))
        self.drillAngleY.setObjectName("drillAngleY")
        self.drillAngleZ = QtGui.QLabel(Dialog)
        self.drillAngleZ.setGeometry(QtCore.QRect(440, 360, 81, 16))
        self.drillAngleZ.setObjectName("drillAngleZ")
        self.drillDiameter = QtGui.QLabel(Dialog)
        self.drillDiameter.setGeometry(QtCore.QRect(110, 140, 211, 31))
        self.drillDiameter.setObjectName("drillDiameter")
        self.posX = QtGui.QLineEdit(Dialog)
        self.posX.setGeometry(QtCore.QRect(210, 260, 113, 22))
        self.posX.setObjectName("posX")
        self.posY = QtGui.QLineEdit(Dialog)
        self.posY.setGeometry(QtCore.QRect(210, 310, 113, 22))
        self.posY.setObjectName("posY")
        self.posZ = QtGui.QLineEdit(Dialog)
        self.posZ.setGeometry(QtCore.QRect(210, 360, 113, 22))
        self.posZ.setObjectName("posZ")
        self.angX = QtGui.QLineEdit(Dialog)
        self.angX.setGeometry(QtCore.QRect(560, 270, 113, 22))
        self.angX.setObjectName("angX")
        self.angY = QtGui.QLineEdit(Dialog)
        self.angY.setGeometry(QtCore.QRect(560, 310, 113, 22))
        self.angY.setObjectName("angY")
        self.angZ = QtGui.QLineEdit(Dialog)
        self.angZ.setGeometry(QtCore.QRect(560, 360, 113, 22))
        self.angZ.setObjectName("angZ")
        self.diam = QtGui.QLineEdit(Dialog)
        self.diam.setGeometry(QtCore.QRect(370, 150, 113, 22))
        self.diam.setObjectName("diam")
        self.pushButton = QtGui.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(350, 400, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.drillID = QtGui.QLabel(Dialog)
        self.drillID.setGeometry(QtCore.QRect(110, 180, 101, 41))
        self.drillID.setObjectName("drillID")
        self.DrillIDLevel = QtGui.QLineEdit(Dialog)
        self.DrillIDLevel.setGeometry(QtCore.QRect(370, 190, 113, 22))
        self.DrillIDLevel.setObjectName("DrillIDLevel")
        self.informCAD = QtGui.QLabel(Dialog)
        self.informCAD.setGeometry(QtCore.QRect(230, 60, 431, 41))
        self.informCAD.setObjectName("informCAD")
        self.pushInform = QtGui.QPushButton(Dialog)
        self.pushInform.setGeometry(QtCore.QRect(40, 70, 131, 31))
        self.pushInform.setObjectName("pushInform")

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.pushInform,QtCore.SIGNAL("pressed()"),self.extractInf)
        QtCore.QObject.connect(self.pushButton,QtCore.SIGNAL("pressed()"),self.Import2Jason)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.heading.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600; color:#ff007f;\">Drilling Opearation</span></p></body></html>"))
        self.drillX.setText(_translate("Dialog", "Drill Position X"))
        self.drillY.setText(_translate("Dialog", "Drill Position Y"))
        self.drillZ.setText(_translate("Dialog", "Drill Position Z"))
        self.drillAngleX.setText(_translate("Dialog", "Drill Angle X"))
        self.drillAngleY.setText(_translate("Dialog", "Drill Angle Y"))
        self.drillAngleZ.setText(_translate("Dialog", "Drill Angle Z"))
        # setting default value 0 all to the line edit box
        self.posX.setText(_translate("Dialog", str(0), None))
        self.posY.setText(_translate("Dialog", str(0), None))
        self.posZ.setText(_translate("Dialog", str(0), None))
        self.angX.setText(_translate("Dialog", str(0), None))
        self.angY.setText(_translate("Dialog", str(0), None))
        self.angZ.setText(_translate("Dialog", str(0), None))
        self.DrillIDLevel.setText(_translate("Dialog", str(0), None))
        self.diam.setText(_translate("Dialog", str(0), None))
        
        self.drillDiameter.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600; color:#005500;\">Drilling Diameter</span></p></body></html>"))
        self.pushButton.setText(_translate("Dialog", "CreateDrill"))
        self.drillID.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#5500ff;\">Drill ID</span></p></body></html>"))
        self.informCAD.setText(_translate("Dialog", "Information to the user"))
        self.pushInform.setText(_translate("Dialog", "Information"))
        
    def extractInf(self):
        _translate = QtCore.QCoreApplication.translate
        # import information from external file
        FreeCAD.Console.PrintMessage("Waiting for the information to import   ")
        obj1 = GetCoordinates.InformCoordinates('b_motor_001_001')
        obj1 = obj1.giveInform()
        
        FreeCAD.Console.PrintMessage(str(obj1))
        #Extract information to the dialog line-edit box
        self.posX.setText(_translate("Dialog", str(obj1[0]), None))
        self.posY.setText(_translate("Dialog", str(obj1[1]), None))
        self.posZ.setText(_translate("Dialog", str(obj1[2]), None))
        self.angX.setText(_translate("Dialog", str(obj1[3]), None))
        self.angY.setText(_translate("Dialog", str(obj1[4]), None))
        self.angZ.setText(_translate("Dialog", str(obj1[5]), None))
      
        ob = "Pos ["+str(obj1[0])+" "+ str(obj1[1])+ " " + str(obj1[2]) + "]"+ " " +"Rot [" + str(obj1[3]) + " " + str(obj1[4]) + " " + str(obj1[5]) +"]"
        FreeCAD.Console.PrintMessage(ob)
        self.informCAD.setText(_translate("Dialog",ob))
    
    def Import2Jason(self):
        _translate = QtCore.QCoreApplication.translate
        FreeCAD.Console.PrintMessage("Please insert the coordinates value")
        try:
            #obj1 = selectMotor.giveInform()
            x = float(self.posX.text())
            y = float(self.posY.text())
            z = float(self.posZ.text())
            
            # angle of drill to the object
            ax = float(self.angX.text())
            ay = float(self.angX.text())
            az = float(self.angX.text())
            
            #  drilling diameter
            di = float(self.diam.text())
            
            # drill id
            
            drID = float(self.DrillIDLevel.text())
            
        except ValueError:
           #FreeCAD.Console.PrintMessage("Error! values must be valid numbers!")
           self.informCAD.setText(_translate("Dialog","Error! Values must be valid numbers"))
        else:
           # print("The positions are successfully imported")
            FreeCAD.Console.PrintMessage("The positions are successfully imported \n")
            f = open("C:/Users/Mashiur/Music/JasonFiles/drillingPosition.JSON",mode='w',encoding='utf-8')
            # a Python object (dictionary):
            persingObject = {
                "Name" : "DrillLocation",
                #"globalId": "ss",
                "Type" : "Location",
                #"drillId" : "Some Local Address",
                "X": x,
                "Y": y,
                "Z": z,
                "RX": ax,
                "RY": ay,
                "RZ": az
            }
            # convert into JSON:
            y = json.dumps(persingObject, indent = 4)
            f.write(y)
            f.close()
            self.informCAD.setText(_translate("Dialog","JSON file is created"))
            FreeCAD.Console.PrintMessage("The JSON file is created")


class makejson():
  def __init__(self):
      self.d = QtGui.QWidget()
      self.ui = Ui_Dialog()
      self.ui.setupUi(self.d)
      self.d.show()
