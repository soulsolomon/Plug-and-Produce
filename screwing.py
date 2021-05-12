# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'screwing.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui
import FreeCAD, Part 
import json, GetCoordinates, GetCoordinates2, CoValueCreation
import math

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(613, 538)
        self.screwingOperation = QtGui.QLabel(Dialog)
        self.screwingOperation.setGeometry(QtCore.QRect(150, 0, 311, 71))
        self.screwingOperation.setObjectName("screwingOperation")
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(120, 150, 121, 41))
        self.label.setObjectName("label")
        self.PositionX = QtGui.QLabel(Dialog)
        self.PositionX.setGeometry(QtCore.QRect(10, 210, 81, 41))
        self.PositionX.setObjectName("PositionX")
        self.PositionY = QtGui.QLabel(Dialog)
        self.PositionY.setGeometry(QtCore.QRect(10, 260, 91, 31))
        self.PositionY.setObjectName("PositionY")
        self.PositionZ = QtGui.QLabel(Dialog)
        self.PositionZ.setGeometry(QtCore.QRect(10, 300, 91, 31))
        self.PositionZ.setObjectName("PositionZ")
        self.coordinateX = QtGui.QLineEdit(Dialog)
        self.coordinateX.setGeometry(QtCore.QRect(140, 220, 113, 22))
        self.coordinateX.setObjectName("coordinateX")
        self.coordinateY = QtGui.QLineEdit(Dialog)
        self.coordinateY.setGeometry(QtCore.QRect(140, 260, 113, 22))
        self.coordinateY.setObjectName("coordinateY")
        self.coordinateZ = QtGui.QLineEdit(Dialog)
        self.coordinateZ.setGeometry(QtCore.QRect(140, 300, 113, 22))
        self.coordinateZ.setObjectName("coordinateZ")
        self.distanceInmm = QtGui.QLineEdit(Dialog)
        self.distanceInmm.setGeometry(QtCore.QRect(300, 160, 113, 22))
        self.distanceInmm.setObjectName("distanceInmm")
        self.pushButton = QtGui.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(260, 490, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.xfinal = QtGui.QLabel(Dialog)
        self.xfinal.setGeometry(QtCore.QRect(350, 210, 71, 21))
        self.xfinal.setObjectName("xfinal")
        self.yfinal = QtGui.QLabel(Dialog)
        self.yfinal.setGeometry(QtCore.QRect(350, 250, 71, 21))
        self.yfinal.setObjectName("yfinal")
        self.zfinal = QtGui.QLabel(Dialog)
        self.zfinal.setGeometry(QtCore.QRect(350, 290, 61, 21))
        self.zfinal.setObjectName("zfinal")
        self.eX = QtGui.QLineEdit(Dialog)
        self.eX.setGeometry(QtCore.QRect(460, 210, 113, 22))
        self.eX.setObjectName("eX")
        self.eY = QtGui.QLineEdit(Dialog)
        self.eY.setGeometry(QtCore.QRect(460, 250, 113, 22))
        self.eY.setObjectName("eY")
        self.eZ = QtGui.QLineEdit(Dialog)
        self.eZ.setGeometry(QtCore.QRect(460, 290, 113, 22))
        self.eZ.setObjectName("eZ")
        self.SrotX = QtGui.QLabel(Dialog)
        self.SrotX.setGeometry(QtCore.QRect(10, 350, 81, 16))
        font = QtGui.QFont()
        font.setItalic(True)
        self.SrotX.setFont(font)
        self.SrotX.setObjectName("SrotX")
        self.SrotY = QtGui.QLabel(Dialog)
        self.SrotY.setGeometry(QtCore.QRect(10, 390, 71, 16))
        self.SrotY.setObjectName("SrotY")
        self.SrotZ = QtGui.QLabel(Dialog)
        self.SrotZ.setGeometry(QtCore.QRect(10, 430, 71, 16))
        self.SrotZ.setObjectName("SrotZ")
        self.rX = QtGui.QLineEdit(Dialog)
        self.rX.setGeometry(QtCore.QRect(140, 340, 113, 22))
        self.rX.setObjectName("rX")
        self.rY = QtGui.QLineEdit(Dialog)
        self.rY.setGeometry(QtCore.QRect(140, 380, 113, 22))
        self.rY.setObjectName("rY")
        self.rZ = QtGui.QLineEdit(Dialog)
        self.rZ.setGeometry(QtCore.QRect(140, 420, 113, 22))
        self.rZ.setObjectName("rZ")
        self.ErotX = QtGui.QLabel(Dialog)
        self.ErotX.setGeometry(QtCore.QRect(350, 340, 81, 16))
        font = QtGui.QFont()
        font.setItalic(True)
        self.ErotX.setFont(font)
        self.ErotX.setObjectName("ErotX")
        self.ErotY = QtGui.QLabel(Dialog)
        self.ErotY.setGeometry(QtCore.QRect(350, 380, 71, 16))
        self.ErotY.setObjectName("ErotY")
        self.ErotZ = QtGui.QLabel(Dialog)
        self.ErotZ.setGeometry(QtCore.QRect(350, 420, 71, 16))
        self.ErotZ.setObjectName("ErotZ")
        self.erX = QtGui.QLineEdit(Dialog)
        self.erX.setGeometry(QtCore.QRect(460, 340, 113, 22))
        self.erX.setObjectName("erX")
        self.erY = QtGui.QLineEdit(Dialog)
        self.erY.setGeometry(QtCore.QRect(460, 380, 113, 22))
        self.erY.setObjectName("erY")
        self.erZ = QtGui.QLineEdit(Dialog)
        self.erZ.setGeometry(QtCore.QRect(460, 420, 113, 22))
        self.erZ.setObjectName("erZ")
        self.informBox = QtGui.QPushButton(Dialog)
        self.informBox.setGeometry(QtCore.QRect(44, 105, 91, 31))
        self.informBox.setObjectName("informBox")
        self.informLevel = QtGui.QLabel(Dialog)
        self.informLevel.setGeometry(QtCore.QRect(170, 100, 361, 31))
        self.informLevel.setObjectName("informLevel")

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.informBox,QtCore.SIGNAL("pressed()"),self.extractInf)
        QtCore.QObject.connect(self.pushButton,QtCore.SIGNAL("pressed()"),self.export2Jason)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.screwingOperation.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:18pt; font-weight:600; color:#0000ff;\">Screwing Operation</span></p></body></html>"))
        self.label.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-weight:600; color:#aa007f;\">Distance Apart</span></p></body></html>"))
        self.PositionX.setText(_translate("Dialog", "StartPosX"))
        self.PositionY.setText(_translate("Dialog", "StartPosY"))
        self.PositionZ.setText(_translate("Dialog", "StartPosZ"))
        self.pushButton.setText(_translate("Dialog", "Make Screw"))
        self.xfinal.setText(_translate("Dialog", "EndPosX"))
        self.yfinal.setText(_translate("Dialog", "EndPosY"))
        self.zfinal.setText(_translate("Dialog", "EndPosZ"))
        self.SrotX.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-style:italic; color:#005500;\">StartRot_X</span></p></body></html>"))
        self.SrotY.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-style:italic; color:#005500;\">StartRot_Y</span></p></body></html>"))
        self.SrotZ.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-style:italic; color:#005500;\">StartRot_Z</span></p></body></html>"))
        self.ErotX.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-style:italic; color:#005500;\">EndRot_X</span></p></body></html>"))
        self.ErotY.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-style:italic; color:#005500;\">EndRot_Y</span></p></body></html>"))
        self.ErotZ.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-style:italic; color:#005500;\">EndRot_Z</span></p></body></html>"))
        self.informBox.setText(_translate("Dialog", "Information"))
        self.informLevel.setText(_translate("Dialog", "Information from CAD"))
        
        # manually set all the values to zero at the beginning
        
        # Position coordinates of the start of the screw by default zero
        self.coordinateX.setText(_translate("Dialog", str(0), None))
        self.coordinateY.setText(_translate("Dialog", str(0), None))
        self.coordinateZ.setText(_translate("Dialog", str(0), None))
        
        # Position coordinates of the end of the screw set to zero by default
        
        self.eX.setText(_translate("Dialog", str(0), None))
        self.eY.setText(_translate("Dialog", str(0), None))
        self.eZ.setText(_translate("Dialog", str(0), None))
        
        # Rotation is set to zero by deafalt
        self.erX.setText(_translate("Dialog", str(0), None))
        self.erY.setText(_translate("Dialog", str(0), None))
        self.erZ.setText(_translate("Dialog", str(0), None))
        self.rX.setText(_translate("Dialog", str(0), None))
        self.rY.setText(_translate("Dialog", str(0), None))
        self.rZ.setText(_translate("Dialog", str(0), None))
        
        # Set the distance between screw to 300 by default
        
        self.distanceInmm.setText(_translate("Dialog", str(300), None))
        
    def extractInf(self):
        _translate = QtCore.QCoreApplication.translate
        # import information from external file
        FreeCAD.Console.PrintMessage("Waiting for the information to import   ")
        
        # Extract Information for the first screw operation
        obj1 = GetCoordinates.InformCoordinates('b_screw_001_010')
        obj1 = obj1.giveInform()
        
        FreeCAD.Console.PrintMessage(str(obj1))
        #Extract information to the dialog line-edit box
        self.coordinateX.setText(_translate("Dialog", str(obj1[0]), None))
        self.coordinateY.setText(_translate("Dialog", str(obj1[1]), None))
        self.coordinateZ.setText(_translate("Dialog", str(obj1[2]), None))
        self.rX.setText(_translate("Dialog", str(obj1[3]), None))
        self.rY.setText(_translate("Dialog", str(obj1[4]), None))
        self.rZ.setText(_translate("Dialog", str(obj1[5]), None))
      
        ob1 = "Pos ["+str(obj1[0])+" "+ str(obj1[1])+ " " + str(obj1[2]) + "]"+ " " +"Rot [" + str(obj1[3]) + " " + str(obj1[4]) + " " + str(obj1[5]) +"]"
        FreeCAD.Console.PrintMessage(ob1)
        # self.informCAD.setText(_translate("Dialog",ob))
        
        # Extract information for the last screw operation
        obj2 = GetCoordinates2.InformCoordinates('b_screw_001_011')
        obj2 = obj2.giveInform()
        
        FreeCAD.Console.PrintMessage(str(obj2))
        #Extract information to the dialog line-edit box
        self.eX.setText(_translate("Dialog", str(obj2[0]), None))
        self.eY.setText(_translate("Dialog", str(obj2[1]), None))
        self.eZ.setText(_translate("Dialog", str(obj2[2]), None))
        self.erX.setText(_translate("Dialog", str(obj2[3]), None))
        self.erY.setText(_translate("Dialog", str(obj2[4]), None))
        self.erZ.setText(_translate("Dialog", str(obj2[5]), None))
      
        ob2 = "Pos ["+str(obj2[0])+" "+ str(obj2[1])+ " " + str(obj2[2]) + "]"+ " " +"Rot [" + str(obj2[3]) + " " + str(obj2[4]) + " " + str(obj2[5]) +"]"
        FreeCAD.Console.PrintMessage(ob2)
        self.informLevel.setText(_translate("Dialog","Successfully Imported DATA from CAD"))
        
        
    def export2Jason(self):
        _translate = QtCore.QCoreApplication.translate
        try:
            
            # Enter the screw distance
            d = float(self.distanceInmm.text())
            
            # input of the first screw
            sx = float(self.coordinateX.text())
            sy = float(self.coordinateY.text())
            sz = float(self.coordinateZ.text())
            
            # input of the last screw
            ex = float(self.eX.text())
            ey = float(self.eY.text())
            ez = float(self.eZ.text())
            
            # rotation of the first screw
            ax1 = float(self.rX.text())
            ay1 = float(self.rY.text())
            az1 = float(self.rZ.text())
            
            # rotation of the last screw
            ax2 = float(self.erX.text())
            ay2 = float(self.erY.text())
            az2 = float(self.erZ.text())
           
        except ValueError:
           print("Error! values must be valid numbers!")
        else:
             # print("The positions are successfully imported")
            FreeCAD.Console.PrintMessage("The positions are successfully imported")
            f = open("C:/Users/Mashiur/Music/JasonFiles/screws.JSON",mode='w',encoding='utf-8')
            #FreeCAD.Console.PrintMessage("distance apart is " + str(d))
            # objective is to create coordinates based on the distnace apart between screws
            # using pythagorous formula           
            xdist = ex - sx
            #FreeCAD.Console.PrintMessage("x distance value " + str(xdist))
            ydist = ey - sy
            #FreeCAD.Console.PrintMessage("y distance value " + str(ydist))
            # number of screws
            nsqrt = (xdist**2+ydist**2) / d**2
            n = math.sqrt(nsqrt)+ 1 # considering the first screw operation as well
            # n provides the floating value, so the number should be converted to int
            n = int(n)
            FreeCAD.Console.PrintMessage(" Number of screws are : "+ str(n))
      
            # calling seperate funstion to get the coordinate value
            arrValue = CoValueCreation.ValueCreate(sx,ex,d,n)
            arrX = arrValue.valueArray()
            FreeCAD.Console.PrintMessage("  X positions are" + str(arrX))
            
            arrValue = CoValueCreation.ValueCreate(sy,ey,d,n)
            arrY = arrValue.valueArray()
            FreeCAD.Console.PrintMessage("  Y positions are" + str(arrY))
            
            arrValue = CoValueCreation.ValueCreate(sz,ez,d,n)
            arrZ = arrValue.valueArray()
            FreeCAD.Console.PrintMessage("  Z positions are" + str(arrZ))
            
            # creating array object of rotation parameters
            RX_value = [ax1 for ar in range(0,n)]
            RY_value = [ay1 for ar in range(0,n)]
            RZ_value = [az1 for ar in range(0,n)]
           
            
            # Creating a dictionary object to import it in JSON
            arr = [0 for ar in range(0,n)]
            
            for ii in range(0,n):
                arr[ii] = {
                    "Name" : "Screw"+ str(ii+1), # to create name string value
                    "Type": "Locations",
                    "X": arrX[ii],
                    "Y": arrY[ii],
                    "Z": arrZ[ii],
                    "RX": RX_value[ii],
                    "RY": RY_value[ii],
                    "RZ": RZ_value[ii]
                    }
            # Creating JSON agent as library functions
            jsonagents = {"type": "Locations",
                    "DistanceScrew" : d, #  
                    "Locations": arr}
                    
            FreeCAD.Console.PrintMessage(" list dictionary " + str(jsonagents)) 
            # convert into JSON from python library:
            y = json.dumps(jsonagents,indent = 4)
            f.write(y)
            f.close()
            self.informLevel.setText(_translate("Dialog","JSON file is created"))
            FreeCAD.Console.PrintMessage("The JSON file is created")


class makejson():
  def __init__(self):
      self.d = QtGui.QWidget()
      self.ui = Ui_Dialog()
      self.ui.setupUi(self.d)
      self.d.show()