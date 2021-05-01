# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pickPlace.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui
import FreeCAD, Part 
import json

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(540, 467)
        self.title = QtGui.QLabel(Dialog)
        self.title.setGeometry(QtCore.QRect(140, 20, 221, 51))
        self.title.setObjectName("title")
        self.StartX = QtGui.QLabel(Dialog)
        self.StartX.setGeometry(QtCore.QRect(40, 100, 61, 16))
        self.StartX.setObjectName("StartX")
        self.StartY = QtGui.QLabel(Dialog)
        self.StartY.setGeometry(QtCore.QRect(40, 150, 71, 21))
        self.StartY.setObjectName("StartY")
        self.StartZ = QtGui.QLabel(Dialog)
        self.StartZ.setGeometry(QtCore.QRect(40, 210, 55, 16))
        self.StartZ.setObjectName("StartZ")
        self.EndX = QtGui.QLabel(Dialog)
        self.EndX.setGeometry(QtCore.QRect(274, 100, 61, 20))
        self.EndX.setObjectName("EndX")
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(274, 150, 61, 20))
        self.label.setObjectName("label")
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(274, 200, 61, 20))
        self.label_2.setObjectName("label_2")
        self.ppX = QtGui.QLineEdit(Dialog)
        self.ppX.setGeometry(QtCore.QRect(120, 100, 113, 22))
        self.ppX.setObjectName("ppX")
        self.ppY = QtGui.QLineEdit(Dialog)
        self.ppY.setGeometry(QtCore.QRect(120, 150, 113, 22))
        self.ppY.setObjectName("ppY")
        self.ppZ = QtGui.QLineEdit(Dialog)
        self.ppZ.setGeometry(QtCore.QRect(120, 200, 113, 22))
        self.ppZ.setObjectName("ppZ")
        self.plpX = QtGui.QLineEdit(Dialog)
        self.plpX.setGeometry(QtCore.QRect(370, 100, 113, 22))
        self.plpX.setObjectName("plpX")
        self.plpY = QtGui.QLineEdit(Dialog)
        self.plpY.setGeometry(QtCore.QRect(370, 150, 113, 22))
        self.plpY.setObjectName("plpY")
        self.plpZ = QtGui.QLineEdit(Dialog)
        self.plpZ.setGeometry(QtCore.QRect(370, 200, 113, 22))
        self.plpZ.setObjectName("plpZ")
        self.pickplacebuttom = QtGui.QPushButton(Dialog)
        self.pickplacebuttom.setGeometry(QtCore.QRect(180, 400, 161, 28))
        self.pickplacebuttom.setObjectName("pickplacebuttom")
        self.prx = QtGui.QLabel(Dialog)
        self.prx.setGeometry(QtCore.QRect(40, 260, 55, 16))
        self.prx.setObjectName("prx")
        self.prY = QtGui.QLabel(Dialog)
        self.prY.setGeometry(QtCore.QRect(40, 300, 55, 16))
        self.prY.setObjectName("prY")
        self.prZ = QtGui.QLabel(Dialog)
        self.prZ.setGeometry(QtCore.QRect(40, 340, 55, 16))
        self.prZ.setObjectName("prZ")
        self.plrX = QtGui.QLabel(Dialog)
        self.plrX.setGeometry(QtCore.QRect(264, 250, 81, 20))
        self.plrX.setObjectName("plrX")
        self.plrY = QtGui.QLabel(Dialog)
        self.plrY.setGeometry(QtCore.QRect(264, 290, 81, 20))
        self.plrY.setObjectName("plrY")
        self.plrZ = QtGui.QLabel(Dialog)
        self.plrZ.setGeometry(QtCore.QRect(264, 340, 81, 20))
        self.plrZ.setObjectName("plrZ")
        self.pickRX = QtGui.QLineEdit(Dialog)
        self.pickRX.setGeometry(QtCore.QRect(120, 260, 113, 22))
        self.pickRX.setObjectName("pickRX")
        self.pickRY = QtGui.QLineEdit(Dialog)
        self.pickRY.setGeometry(QtCore.QRect(120, 300, 113, 22))
        self.pickRY.setObjectName("pickRY")
        self.pickRZ = QtGui.QLineEdit(Dialog)
        self.pickRZ.setGeometry(QtCore.QRect(120, 340, 113, 22))
        self.pickRZ.setObjectName("pickRZ")
        self.placeRX = QtGui.QLineEdit(Dialog)
        self.placeRX.setGeometry(QtCore.QRect(370, 250, 113, 22))
        self.placeRX.setObjectName("placeRX")
        self.placeRY = QtGui.QLineEdit(Dialog)
        self.placeRY.setGeometry(QtCore.QRect(370, 290, 113, 22))
        self.placeRY.setObjectName("placeRY")
        self.placeRZ = QtGui.QLineEdit(Dialog)
        self.placeRZ.setGeometry(QtCore.QRect(370, 340, 113, 22))
        self.placeRZ.setObjectName("placeRZ")

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.pickplacebuttom,QtCore.SIGNAL("pressed()"),self.Import2Jason)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.title.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:18pt; font-weight:600; color:#0000ff;\">Pick &amp; Place</span></p></body></html>"))
        self.StartX.setText(_translate("Dialog", "PickPosX"))
        self.StartY.setText(_translate("Dialog", "PicPosY"))
        self.StartZ.setText(_translate("Dialog", "PicPosZ"))
        self.EndX.setText(_translate("Dialog", "PlacePosX"))
        self.label.setText(_translate("Dialog", "PlacePosY"))
        self.label_2.setText(_translate("Dialog", "PlacePosZ"))
        self.pickplacebuttom.setText(_translate("Dialog", "Pick&Place"))
        self.prx.setText(_translate("Dialog", "PicAngleX"))
        self.prY.setText(_translate("Dialog", "PicAngleY"))
        self.prZ.setText(_translate("Dialog", "PicAngleZ"))
        self.plrX.setText(_translate("Dialog", "PlaceAngleX"))
        self.plrY.setText(_translate("Dialog", "PlaceAngleY"))
        self.plrZ.setText(_translate("Dialog", "PlaceAngleZ"))
        
    def Import2Jason(self):
        try: 
            # pick position
            x1 = float(self.ppX.text())
            y1 = float(self.ppY.text())
            z1 = float(self.ppZ.text())
            
            # place position
            x2 = float(self.plpX.text())
            y2 = float(self.plpY.text())
            z2 = float(self.plpZ.text())
            
            # pick angles
            rx1 = float(self.pickRX.text())
            ry1 = float(self.pickRY.text())
            rz1 = float(self.pickRZ.text())
            
            # place angles
            rx2 = float(self.placeRX.text())
            ry2 = float(self.placeRY.text())
            rz2 = float(self.placeRZ.text())
        except ValueError:
           print("Error! values must be valid numbers!")
        else:
            '''arr = [0 for ar in range(0,n)]
            for i in range(0,n):
                posX = x
                posY = y + d * (i)
                posZ = z
                arr[i] = {"X": posX,
                    "Y": posY,
                    "Z": posZ,
                    "RX": 0,
                    "RY": 0,
                    "RZ": 0
                    }
            
            # converts number to nails of string value and concatenate to string value
            nail = [0 for a in range(0,n)]
            for j in range(1,n+1):
                strj = str(j)
                nail[j-1] = "nail"+strj


            persObject = {nail[a]:arr[a] for a in range(0,n)}'''
            
            # creating pick agent dictionary
            pickAgent = {'X': x1, 'Y':y1, 'Z': z1,"RX":rx1, "RY" : ry1, "RZ" : rz1}
            
            # creating place agent dictionary
            placeAgent = {'X': x2, 'Y':y2, 'Z': z2,"RX":rx2, "RY" : ry2, "RZ" : rz2}
            

    
            jsonagents = {"type": "agent-pickPlace",
                        "globalId": "ajskjk-mjasji-fatfts-ajihs",
                        "agents": {"Pick":pickAgent, "Place":placeAgent}}
            # needs to find out nail1: arr[0],nail2
            f = open("C:/Users/Mashiur/Music/JasonFiles/pickPlace.JSON",mode='w',encoding='utf-8')
            # a Python object (dictionary):
           
            # convert into JSON:
            y = json.dumps(jsonagents, indent = 2)
            f.write(y)
            f.close()
            
class makejson():
  def __init__(self):
      self.d = QtGui.QWidget()
      self.ui = Ui_Dialog()
      self.ui.setupUi(self.d)
      self.d.show()
