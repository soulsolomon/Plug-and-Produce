# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'screwing.ui'
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
        Dialog.resize(610, 480)
        self.screwingOperation = QtGui.QLabel(Dialog)
        self.screwingOperation.setGeometry(QtCore.QRect(190, 20, 311, 71))
        self.screwingOperation.setObjectName("screwingOperation")
        self.noScrew = QtGui.QLabel(Dialog)
        self.noScrew.setGeometry(QtCore.QRect(10, 100, 131, 31))
        self.noScrew.setObjectName("noScrew")
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(340, 90, 91, 41))
        self.label.setObjectName("label")
        self.PositionX = QtGui.QLabel(Dialog)
        self.PositionX.setGeometry(QtCore.QRect(10, 150, 81, 41))
        self.PositionX.setObjectName("PositionX")
        self.PositionY = QtGui.QLabel(Dialog)
        self.PositionY.setGeometry(QtCore.QRect(10, 200, 91, 31))
        self.PositionY.setObjectName("PositionY")
        self.PositionZ = QtGui.QLabel(Dialog)
        self.PositionZ.setGeometry(QtCore.QRect(10, 240, 91, 31))
        self.PositionZ.setObjectName("PositionZ")
        self.ScrewNumber = QtGui.QLineEdit(Dialog)
        self.ScrewNumber.setGeometry(QtCore.QRect(140, 110, 113, 22))
        self.ScrewNumber.setObjectName("ScrewNumber")
        self.coordinateX = QtGui.QLineEdit(Dialog)
        self.coordinateX.setGeometry(QtCore.QRect(140, 160, 113, 22))
        self.coordinateX.setObjectName("coordinateX")
        self.coordinateY = QtGui.QLineEdit(Dialog)
        self.coordinateY.setGeometry(QtCore.QRect(140, 200, 113, 22))
        self.coordinateY.setObjectName("coordinateY")
        self.coordinateZ = QtGui.QLineEdit(Dialog)
        self.coordinateZ.setGeometry(QtCore.QRect(140, 240, 113, 22))
        self.coordinateZ.setObjectName("coordinateZ")
        self.distanceInmm = QtGui.QLineEdit(Dialog)
        self.distanceInmm.setGeometry(QtCore.QRect(460, 100, 113, 22))
        self.distanceInmm.setObjectName("distanceInmm")
        self.pushButton = QtGui.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(260, 430, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.xfinal = QtGui.QLabel(Dialog)
        self.xfinal.setGeometry(QtCore.QRect(350, 140, 111, 31))
        self.xfinal.setObjectName("xfinal")
        self.yfinal = QtGui.QLabel(Dialog)
        self.yfinal.setGeometry(QtCore.QRect(350, 190, 111, 21))
        self.yfinal.setObjectName("yfinal")
        self.zfinal = QtGui.QLabel(Dialog)
        self.zfinal.setGeometry(QtCore.QRect(350, 240, 91, 21))
        self.zfinal.setObjectName("zfinal")
        self.endX = QtGui.QLineEdit(Dialog)
        self.endX.setGeometry(QtCore.QRect(460, 140, 113, 22))
        self.endX.setObjectName("endX")
        self.endY = QtGui.QLineEdit(Dialog)
        self.endY.setGeometry(QtCore.QRect(460, 190, 113, 22))
        self.endY.setObjectName("endY")
        self.endZ = QtGui.QLineEdit(Dialog)
        self.endZ.setGeometry(QtCore.QRect(460, 240, 113, 22))
        self.endZ.setObjectName("endZ")
        self.rotX = QtGui.QLabel(Dialog)
        self.rotX.setGeometry(QtCore.QRect(170, 300, 55, 16))
        self.rotX.setObjectName("rotX")
        self.rotY = QtGui.QLabel(Dialog)
        self.rotY.setGeometry(QtCore.QRect(170, 340, 55, 16))
        self.rotY.setObjectName("rotY")
        self.rotZ = QtGui.QLabel(Dialog)
        self.rotZ.setGeometry(QtCore.QRect(170, 380, 55, 16))
        self.rotZ.setObjectName("rotZ")
        self.rX = QtGui.QLineEdit(Dialog)
        self.rX.setGeometry(QtCore.QRect(260, 300, 113, 22))
        self.rX.setObjectName("rX")
        self.rY = QtGui.QLineEdit(Dialog)
        self.rY.setGeometry(QtCore.QRect(260, 340, 113, 22))
        self.rY.setObjectName("rY")
        self.rZ = QtGui.QLineEdit(Dialog)
        self.rZ.setGeometry(QtCore.QRect(260, 380, 113, 22))
        self.rZ.setObjectName("rZ")

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.pushButton,QtCore.SIGNAL("pressed()"),self.Import2Jason)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.screwingOperation.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:18pt; font-weight:600; color:#0000ff;\">Screwing Operation</span></p></body></html>"))
        self.noScrew.setText(_translate("Dialog", "Number of screws"))
        self.label.setText(_translate("Dialog", "Distance Apart"))
        self.PositionX.setText(_translate("Dialog", "StartPosX"))
        self.PositionY.setText(_translate("Dialog", "StartPosY"))
        self.PositionZ.setText(_translate("Dialog", "StartPosZ"))
        self.pushButton.setText(_translate("Dialog", "Make Screw"))
        self.xfinal.setText(_translate("Dialog", "EndPosX"))
        self.yfinal.setText(_translate("Dialog", "EndPosY"))
        self.zfinal.setText(_translate("Dialog", "EndPosZ"))
        self.rotX.setText(_translate("Dialog", "RotX"))
        self.rotY.setText(_translate("Dialog", "RotY"))
        self.rotZ.setText(_translate("Dialog", "RotZ"))
        
    def Import2Jason(self):
        try:
            # Enter the number of screws
            n = int(self.ScrewNumber.text())
            
            # Enter the screw distance
            d = float(self.distanceInmm.text())
            
            # input of the first screw
            x = float(self.coordinateX.text())
            y = float(self.coordinateY.text())
            z = float(self.coordinateZ.text())
            
            # end position of nails
            ex = float(self.endX.text())
            ey = float(self.endY.text())
            ez = float(self.endZ.text())
            
            # rotation of nails
            ax = float(self.rX.text())
            ay = float(self.rY.text())
            az = float(self.rZ.text())
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
                    "RX": ax,
                    "RY": ay,
                    "RZ": az
                    }
            
            # converts number to screws of string value and concatenate to string value
            screw = [0 for a in range(0,n)]
            for j in range(1,n+1):
                strj = str(j)
                screw[j-1] = "screw"+strj


            persObject = {screw[a]:arr[a] for a in range(0,n)}

    
            jsonagents = {"type": "agent_screw",
                        "globalId": "ajskjk-mjasji-fatfts-ajihs",
                        "agents": persObject}
            # needs to find out screws: arr[0],nail2
            f = open("C:/Users/Mashiur/Music/JasonFiles/screw.JSON",mode='w',encoding='utf-8')
           
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