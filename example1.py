# -*- coding: utf-8 -*-
# Create by flachyjoe

from PySide import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)


class Ui_MainWindow(object):

     def __init__(self, MainWindow):
        self.window = MainWindow

        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(400, 300)
        self.centralWidget = QtGui.QWidget(MainWindow)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))

        self.pushButton = QtGui.QPushButton(self.centralWidget)
        self.pushButton.setGeometry(QtCore.QRect(30, 170, 93, 28))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton.clicked.connect(self.on_pushButton_clicked) #connection pushButton

        self.lineEdit = QtGui.QLineEdit(self.centralWidget)
        self.lineEdit.setGeometry(QtCore.QRect(30, 40, 211, 22))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.lineEdit.returnPressed.connect(self.on_lineEdit_clicked) #connection lineEdit

        self.checkBox = QtGui.QCheckBox(self.centralWidget)
        self.checkBox.setGeometry(QtCore.QRect(30, 90, 81, 20))
        self.checkBox.setChecked(True)
        self.checkBox.setObjectName(_fromUtf8("checkBoxON"))
        self.checkBox.clicked.connect(self.on_checkBox_clicked) #connection checkBox

        self.radioButton = QtGui.QRadioButton(self.centralWidget)
        self.radioButton.setGeometry(QtCore.QRect(30, 130, 95, 20))
        self.radioButton.setObjectName(_fromUtf8("radioButton"))
        self.radioButton.clicked.connect(self.on_radioButton_clicked) #connection radioButton

        MainWindow.setCentralWidget(self.centralWidget)

        self.menuBar = QtGui.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 400, 26))
        self.menuBar.setObjectName(_fromUtf8("menuBar"))
        MainWindow.setMenuBar(self.menuBar)

        self.mainToolBar = QtGui.QToolBar(MainWindow)
        self.mainToolBar.setObjectName(_fromUtf8("mainToolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)

        self.statusBar = QtGui.QStatusBar(MainWindow)
        self.statusBar.setObjectName(_fromUtf8("statusBar"))
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)

     def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.pushButton.setText(_translate("MainWindow", "OK", None))
        self.lineEdit.setText(_translate("MainWindow", str(0), None))
        self.checkBox.setText(_translate("MainWindow", "CheckBox", None))
        self.radioButton.setText(_translate("MainWindow", "RadioButton", None))

     def on_checkBox_clicked(self):
        if self.checkBox.checkState()==0:
            App.Console.PrintMessage(str(self.checkBox.checkState())+"  CheckBox KO\r\n")
        else:     
            App.Console.PrintMessage(str(self.checkBox.checkState())+" CheckBox OK\r\n")
#        App.Console.PrintMessage(str(self.lineEdit.setText("tititi"))+" LineEdit\r\n") #write text to the lineEdit window !
#        str(self.lineEdit.setText("tititi")) #écrit le texte dans la fenêtre lineEdit
        App.Console.PrintMessage(str(self.lineEdit.displayText())+" LineEdit\r\n")

     def on_radioButton_clicked(self):
        if self.radioButton.isChecked():
             App.Console.PrintMessage(str(self.radioButton.isChecked())+" Radio OK\r\n")
        else:
             App.Console.PrintMessage(str(self.radioButton.isChecked())+"  Radio KO\r\n")

     def on_lineEdit_clicked(self):
#        if self.lineEdit.textChanged():
             App.Console.PrintMessage(str(self.lineEdit.displayText())+" LineEdit Display\r\n")

     def on_pushButton_clicked(self):
        App.Console.PrintMessage("Terminé\r\n")
        self.window.hide()

MainWindow = QtGui.QMainWindow()
ui = Ui_MainWindow(MainWindow)
MainWindow.show()