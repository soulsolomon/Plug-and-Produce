# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'nail.ui'
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
        Dialog.resize(525, 539)
        self.title =QtGui.QLabel(Dialog)
        self.title.setGeometry(QtCore.QRect(140, 20, 221, 51))
        self.title.setObjectName("title")
        self.nailNumbers =QtGui.QLabel(Dialog)
        self.nailNumbers.setGeometry(QtCore.QRect(30, 90, 101, 41))
        self.nailNumbers.setObjectName("nailNumbers")
        self.Distance =QtGui.QLabel(Dialog)
        self.Distance.setGeometry(QtCore.QRect(290, 100, 121, 21))
        self.Distance.setObjectName("Distance")
        self.StartX =QtGui.QLabel(Dialog)
        self.StartX.setGeometry(QtCore.QRect(30, 180, 61, 16))
        self.StartX.setObjectName("StartX")
        self.StartY =QtGui.QLabel(Dialog)
        self.StartY.setGeometry(QtCore.QRect(30, 230, 71, 21))
        self.StartY.setObjectName("StartY")
        self.StartZ =QtGui.QLabel(Dialog)
        self.StartZ.setGeometry(QtCore.QRect(30, 290, 55, 16))
        self.StartZ.setObjectName("StartZ")
        self.EndX =QtGui.QLabel(Dialog)
        self.EndX.setGeometry(QtCore.QRect(290, 180, 55, 16))
        self.EndX.setObjectName("EndX")
        self.label =QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(290, 230, 55, 16))
        self.label.setObjectName("label")
        self.label_2 =QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(290, 290, 55, 16))
        self.label_2.setObjectName("label_2")
        self.spX =QtGui.QLineEdit(Dialog)
        self.spX.setGeometry(QtCore.QRect(120, 180, 113, 22))
        self.spX.setObjectName("spX")
        self.spY =QtGui.QLineEdit(Dialog)
        self.spY.setGeometry(QtCore.QRect(120, 230, 113, 22))
        self.spY.setObjectName("spY")
        self.spZ =QtGui.QLineEdit(Dialog)
        self.spZ.setGeometry(QtCore.QRect(120, 290, 113, 22))
        self.spZ.setObjectName("spZ")
        self.numberNails =QtGui.QLineEdit(Dialog)
        self.numberNails.setGeometry(QtCore.QRect(140, 100, 113, 22))
        self.numberNails.setObjectName("numberNails")
        self.distanceNails =QtGui.QLineEdit(Dialog)
        self.distanceNails.setGeometry(QtCore.QRect(390, 100, 113, 22))
        self.distanceNails.setObjectName("distanceNails")
        self.epX =QtGui.QLineEdit(Dialog)
        self.epX.setGeometry(QtCore.QRect(390, 180, 113, 22))
        self.epX.setObjectName("epX")
        self.epY =QtGui.QLineEdit(Dialog)
        self.epY.setGeometry(QtCore.QRect(390, 230, 113, 22))
        self.epY.setObjectName("epY")
        self.epZ =QtGui.QLineEdit(Dialog)
        self.epZ.setGeometry(QtCore.QRect(390, 290, 113, 22))
        self.epZ.setObjectName("epZ")
        self.MakeNail =QtGui.QPushButton(Dialog)
        self.MakeNail.setGeometry(QtCore.QRect(170, 490, 161, 28))
        self.MakeNail.setObjectName("MakeNail")
        self.rX =QtGui.QLabel(Dialog)
        self.rX.setGeometry(QtCore.QRect(160, 350, 55, 16))
        self.rX.setObjectName("rX")
        self.rY =QtGui.QLabel(Dialog)
        self.rY.setGeometry(QtCore.QRect(160, 400, 55, 16))
        self.rY.setObjectName("rY")
        self.rZ =QtGui.QLabel(Dialog)
        self.rZ.setGeometry(QtCore.QRect(160, 450, 55, 16))
        self.rZ.setObjectName("rZ")
        self.rotX =QtGui.QLineEdit(Dialog)
        self.rotX.setGeometry(QtCore.QRect(260, 350, 113, 22))
        self.rotX.setObjectName("rotX")
        self.rotY =QtGui.QLineEdit(Dialog)
        self.rotY.setGeometry(QtCore.QRect(260, 390, 113, 22))
        self.rotY.setObjectName("rotY")
        self.rotZ =QtGui.QLineEdit(Dialog)
        self.rotZ.setGeometry(QtCore.QRect(260, 440, 113, 22))
        self.rotZ.setObjectName("rotZ")

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.MakeNail,QtCore.SIGNAL("pressed()"),self.Import2Jason)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.title.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:18pt; font-weight:600; color:#0000ff;\">Nail Operation</span></p></body></html>"))
        self.nailNumbers.setText(_translate("Dialog", "Number of Nails"))
        self.Distance.setText(_translate("Dialog", "Distance Apart"))
        self.StartX.setText(_translate("Dialog", "StartPosX"))
        self.StartY.setText(_translate("Dialog", "StartPosY"))
        self.StartZ.setText(_translate("Dialog", "StartPosZ"))
        self.EndX.setText(_translate("Dialog", "EndPosX"))
        self.label.setText(_translate("Dialog", "EndPosY"))
        self.label_2.setText(_translate("Dialog", "EndPosZ"))
        self.MakeNail.setText(_translate("Dialog", "StartNailOperation"))
        self.rX.setText(_translate("Dialog", "RotX"))
        self.rY.setText(_translate("Dialog", "RotY"))
        self.rZ.setText(_translate("Dialog", "RotZ"))
        
        
    def Import2Jason(self):
        try:
            # Enter the number of nails
            n = int(self.numberNails.text())
            
            # Enter the nailing distance
            d = float(self.distanceNails.text())
            
            # input of the first neiling position
            x = float(self.spX.text())
            y = float(self.spY.text())
            z = float(self.spZ.text())
            
            # end position of nails
            ex = float(self.epX.text())
            ey = float(self.epY.text())
            ez = float(self.epZ.text())
            
            # rotation of nails
            ax = float(self.rotX.text())
            ay = float(self.rotY.text())
            az = float(self.rotZ.text())
        except ValueError:
           print("Error! values must be valid numbers!")
        else:
            arr = [0 for ar in range(0,n)]
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


            persObject = {nail[a]:arr[a] for a in range(0,n)}

    
            jsonagents = {"type": "agent_nail",
                        "globalId": "ajskjk-mjasji-fatfts-ajihs",
                        "agents": persObject}
            # needs to find out nail1: arr[0],nail2
            f = open("C:/Users/Mashiur/Music/JasonFiles/nails.JSON",mode='w',encoding='utf-8')
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
