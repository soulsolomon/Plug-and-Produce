# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'makedrill.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

import FreeCAD, Part
from PySide import QtCore, QtGui
import selectMotor
import json

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(741, 440)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        Dialog.setFont(font)
        self.heading = QtGui.QLabel(Dialog)
        self.heading.setGeometry(QtCore.QRect(230, -10, 411, 61))
        self.heading.setObjectName("heading")
        self.numberDrills = QtGui.QLabel(Dialog)
        self.numberDrills.setGeometry(QtCore.QRect(60, 140, 181, 41))
        self.numberDrills.setObjectName("numberDrills")
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
        self.drillDiameter.setGeometry(QtCore.QRect(400, 140, 211, 31))
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
        self.diam.setGeometry(QtCore.QRect(620, 150, 113, 22))
        self.diam.setObjectName("diam")
        self.noDrills = QtGui.QLineEdit(Dialog)
        self.noDrills.setGeometry(QtCore.QRect(250, 150, 113, 22))
        self.noDrills.setObjectName("noDrills")
        self.pushButton = QtGui.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(350, 400, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.DistanceDrill = QtGui.QLabel(Dialog)
        self.DistanceDrill.setGeometry(QtCore.QRect(60, 190, 161, 41))
        self.DistanceDrill.setObjectName("DistanceDrill")
        self.DistanceBetweenDrills = QtGui.QLineEdit(Dialog)
        self.DistanceBetweenDrills.setGeometry(QtCore.QRect(250, 200, 113, 22))
        self.DistanceBetweenDrills.setObjectName("DistanceBetweenDrills")
        self.drillID = QtGui.QLabel(Dialog)
        self.drillID.setGeometry(QtCore.QRect(430, 190, 101, 41))
        self.drillID.setObjectName("drillID")
        self.DrillIDLevel = QtGui.QLineEdit(Dialog)
        self.DrillIDLevel.setGeometry(QtCore.QRect(560, 200, 113, 22))
        self.DrillIDLevel.setObjectName("DrillIDLevel")
        self.informCAD = QtGui.QLabel(Dialog)
        self.informCAD.setGeometry(QtCore.QRect(230, 60, 431, 41))
        self.informCAD.setObjectName("informCAD")
        #self.informCAD = QtGui.QLineEdit(Dialog)
        #self.informCAD.setGeometry(QtCore.QRect(230, 60, 431, 41))
        #self.informCAD.setObjectName("informCAD")
        
        self.pushInform = QtGui.QPushButton(Dialog)
        self.pushInform.setGeometry(QtCore.QRect(40, 70, 131, 31))
        self.pushInform.setObjectName("pushInform")

        self.retranslateUi(Dialog)
        #QtCore.QObject.connect(self.pushInform.clicked.connect(self.extractInformationFromCAD))
        QtCore.QObject.connect(self.pushInform,QtCore.SIGNAL("pressed()"),self.extractInf)
        QtCore.QObject.connect(self.pushButton,QtCore.SIGNAL("pressed()"),self.Import2Jason)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.heading.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600; color:#ff007f;\">Drilling Opearation</span></p></body></html>"))
        self.numberDrills.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#5500ff;\">Number of drills</span></p></body></html>"))
        self.drillX.setText(_translate("Dialog", "Drill Position X"))
        self.drillY.setText(_translate("Dialog", "Drill Position Y"))
        self.drillZ.setText(_translate("Dialog", "Drill Position Z"))
        self.drillAngleX.setText(_translate("Dialog", "Drill Angle X"))
        self.drillAngleY.setText(_translate("Dialog", "Drill Angle Y"))
        self.drillAngleZ.setText(_translate("Dialog", "Drill Angle Z"))
        self.drillDiameter.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600; color:#005500;\">Drilling Diameter</span></p></body></html>"))
        self.pushButton.setText(_translate("Dialog", "CreateDrill"))
        self.DistanceDrill.setText(_translate("Dialog", "Distance Between Drills"))
        self.drillID.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#5500ff;\">Drill ID</span></p></body></html>"))
        self.informCAD.setText(_translate("Dialog", "Waiting for the information from CAD"))
        self.pushInform.setText(_translate("Dialog", "GetInformation"))
        
    def extractInf(self):
        _translate = QtCore.QCoreApplication.translate
        ob = selectMotor.giveInform()
        #ob = str(ob)
        FreeCAD.Console.PrintMessage(ob)
        self.informCAD.setText(_translate("Dialog",str(ob)))
    def Import2Jason(self):
        try:
            
            x = float(self.posX.text())
            y = float(self.posY.text())
            z = float(self.posZ.text())
            
            # angle of drill to the object
            ax = float(self.angX.text())
            ax = float(self.angX.text())
            ax = float(self.angX.text())
            
            # Number of drill
            num = int(self.noDrills.text())
            
            #  drilling diameter
            di = float(self.diam.text())
            
            # drill id
            
            drID = float(self.DrillIDLevel.text())
            
            # drill distance
            disDis = float(self.DistanceBetweenDrills.text())
            
        except ValueError:
           print("Error! values must be valid numbers!")
        else:
           # print("The positions are successfully imported")
            App.Console.PrintMessage("The positions are successfully imported \n")
            f = open("C:/Users/Mashiur/Music/JasonFiles/drillingPosition.JSON",mode='w',encoding='utf-8')
            # a Python object (dictionary):
            persingObject = {
                "type" : "Drilling Operation",
                "globalId": "ss",
                "name" : "First Drill Position",
                "drillId" : "Some Local Address",
                "PositionX": x,
                "PositionY": y,
                "PositionZ": z
            }
            # convert into JSON:
            y = json.dumps(persingObject, indent = 4)
            f.write(y)
            f.close()
            
    
# if __name__ == "__main__":
    # import sys
    # app = QtGui.QApplication(sys.argv)
    # Dialog = QtGui.QDialog()
    # ui = Ui_Dialog()
    # ui.setupUi(Dialog)
    # Dialog.show()
    # sys.exit(app.exec_())
    
'''class SumOf2():
	def __init__(self, a, b):
		self.a = a
		self.b = b
	
	def getSum(self):
		return self.a + self. b'''
		
    
class makejson():
  def __init__(self):
      self.d = QtGui.QWidget()
      self.ui = Ui_Dialog()
      self.ui.setupUi(self.d)
      self.d.show()

