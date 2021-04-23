import PySide
from PySide import QtCore, QtGui
import FreeCAD
import FreeCADGui
import nail, drillingOperation, screwing, pickPlace, makedrill
import os

__dir__ = os.path.dirname(__file__)

'''
# FreeCAD Command made with a Python script
def MakeBox():
    doc = FreeCAD.ActiveDocument
    box =  doc.addObject("Part::Box",'box')
    box.Length = 1
    box.Width  = 1
    box.Height = 1
    #App.ActiveDocument = box
    #print(box.Length)'''
#FreeCAD.openDocument('C:/Users/Mashiur/Desktop/ThesisCAD/TreeCell.FCStd')
# open the Gui CAD drawing and make it as active
def getGuiDocument():

    FreeCAD.openDocument('C:/Users/Mashiur/Desktop/ThesisCAD/TreeCell.FCStd')
    # FreeCAD.activeDocument("TreeCell")
    # doc = FreeCAD.ActiveDocument
    # box =  doc.addObject("Part::Box",'box')
    # box.Length = 1
    # box.Width  = 1
    # box.Height = 1
    #App.ActiveDocument = box
    #print(box.Length)
# Class command for screw 
# GUI command that links the Python script
class BoxSimpleTaskScrew:
    def __init__(self,widget):
        self.form = widget
        self.form = screwing.makejson()

    # Ok and Cancel buttons are created by default in FreeCAD Task Panels
    # What is done when we click on the ok button.
    def accept(self):
        #MakeBox()
        #mywidget.plane()
        screwing.makejson()
        FreeCADGui.Control.closeDialog() #close the dialog

    # What is done when we click on the cancel button.
    # commented because this is the default behaviour
    #def reject(self):
    #   FreeCADGui.Control.closeDialog()

# GUI command that links the Python script

    
class _MakeScrew:
    """Command to create a screw dialog"""
    
    def Activated(self):
        # what is done when the command is clicked
        # creates a panel with a dialog
        baseWidget = QtGui.QWidget()
        #FreeCAD.openDocument('C:/Users/Mashiur/Desktop/ThesisCAD/TreeCell.FCStd')
        panel = BoxSimpleTaskScrew(baseWidget) 
        # having a panel with a widget in self.form and the accept and 
        # reject functions (if needed), we can open it:
        FreeCADGui.Control.showDialog(panel)
       # mydialogue = mywidget.plane()

    def GetResources(self):
        # icon and command information
        MenuText = QtCore.QT_TRANSLATE_NOOP(
            'Basic1_Box',
            'Box')
        ToolTip = QtCore.QT_TRANSLATE_NOOP(
            'Basic1_Box',
            'Select screw position')
        return {
            'Pixmap': __dir__ + '/icons/screw.svg',
            'MenuText': MenuText,
            'ToolTip': ToolTip}

    def IsActive(self):
        # The command will be active if there is an active document
        return not FreeCAD.ActiveDocument is None


#Adding the ScrewCMD to toolbar
FreeCADGui.addCommand('ScrewCMD', _MakeScrew())



# Class command for Nails 
# GUI command that links the Python script
class BoxSimpleTaskNail:
    def __init__(self,widget):
        self.form = widget
        self.form = nail.makejson()

    # Ok and Cancel buttons are created by default in FreeCAD Task Panels
    # What is done when we click on the ok button.
    def accept(self):
        #MakeBox()
        #mywidget.plane()
        nail.makejson()
        FreeCADGui.Control.closeDialog() #close the dialog

    # What is done when we click on the cancel button.
    # commented because this is the default behaviour
    #def reject(self):
    #   FreeCADGui.Control.closeDialog()

# GUI command that links the Python script

class _MakeNails:
    """Command to create a box"""
    
    def Activated(self):
        # what is done when the command is clicked
        # creates a panel with a dialog
        baseWidget = QtGui.QWidget()
        panel = BoxSimpleTaskNail(baseWidget) 
        # having a panel with a widget in self.form and the accept and 
        # reject functions (if needed), we can open it:
        FreeCADGui.Control.showDialog(panel)
       # mydialogue = mywidget.plane()

    def GetResources(self):
        # icon and command information
        MenuText = QtCore.QT_TRANSLATE_NOOP(
            'Basic1_Box',
            'Box')
        ToolTip = QtCore.QT_TRANSLATE_NOOP(
            'Basic1_Box',
            'Select nail position and relative distance')
        return {
            'Pixmap': __dir__ + '/icons/nail.svg',
            'MenuText': MenuText,
            'ToolTip': ToolTip}

    def IsActive(self):
        # The command will be active if there is an active document
        return not FreeCAD.ActiveDocument is None


#Adding the ScrewCMD to toolbar
FreeCADGui.addCommand('Basic1_MakeBox', _MakeNails())



# Class command for hole saw 
# GUI command that links the Python script
class BoxSimpleTaskDrill:
    def __init__(self,widget):
        self.form = widget
        self.form = makedrill.makejson()

    # Ok and Cancel buttons are created by default in FreeCAD Task Panels
    # What is done when we click on the ok button.
    def accept(self):
        #MakeBox()
        #mywidget.plane()
        makedrill.makejson()
        FreeCADGui.Control.closeDialog() #close the dialog

    # What is done when we click on the cancel button.
    # commented because this is the default behaviour
    #def reject(self):
    #   FreeCADGui.Control.closeDialog()

# GUI command that links the Python script

class _MakeHole:
    """Command to create a box"""
    
    def Activated(self):
       # what is done when the command is clicked
        # creates a panel with a dialog
        baseWidget = QtGui.QWidget()
        panel = BoxSimpleTaskDrill(baseWidget) 
        # having a panel with a widget in self.form and the accept and 
        # reject functions (if needed), we can open it:
        FreeCADGui.Control.showDialog(panel)
       # mydialogue = mywidget.plane()

    def GetResources(self):
        # icon and command information
        MenuText = QtCore.QT_TRANSLATE_NOOP(
            'Basic1_Box',
            'Box')
        ToolTip = QtCore.QT_TRANSLATE_NOOP(
            'Basic1_Box',
            'Select hole diameter and position')
        return {
            'Pixmap': __dir__ + '/icons/saw.svg',
            'MenuText': MenuText,
            'ToolTip': ToolTip}

    def IsActive(self):
        # The command will be active if there is an active document
        return not FreeCAD.ActiveDocument is None


#Adding the HoleCMDoleCmd to toolbar
FreeCADGui.addCommand('HoleCMD', _MakeHole())

# Class command for json 
# GUI command that links the Python script
class _MakeJson:
    """Command to create a box"""
    
    def Activated(self):
        # what is done when the command is clicked
        getGuiDocument()
        FreeCADGui.Selection.addSelection('TreeCell','b_motor_001_')
        sel = FreeCADGui.Selection.getSelection()
        placeMotor = sel[0].Placement.Base
        FreeCAD.Console.PrintMessage(placeMotor)
        p1 = placeMotor[0]
        p2 = placeMotor[1]
        P3 = placeMotor[2]
        
        FreeCAD.Console.PrintMessage(p1)
        #print(sel[0].Placement)

    def GetResources(self):
        # icon and command information
        MenuText = QtCore.QT_TRANSLATE_NOOP(
            'Basic1_Box',
            'Box')
        ToolTip = QtCore.QT_TRANSLATE_NOOP(
            'Basic1_Box',
            'Generate Json')
        return {
            'Pixmap': __dir__ + '/icons/json.svg',
            'MenuText': MenuText,
            'ToolTip': ToolTip}

    def IsActive(self):
        # The command will be active if there is an active document
        return not FreeCAD.ActiveDocument is None


#Adding the JsonCMD to toolbar
FreeCADGui.addCommand('JsonCmd', _MakeJson()) 





# Task Panel creation, the task panel has to have:
#   1. a widget called self.form
#   2. reject and accept methods (if needed)

class BoxSimpleTaskPanelPickPlace:
    def __init__(self,widget):
        self.form = widget
        self.form = pickPlace.makejson()

    # Ok and Cancel buttons are created by default in FreeCAD Task Panels
    # What is done when we click on the ok button.
    def accept(self):
        #MakeBox()
        #mywidget.plane()
        pickPlace.makejson()
        FreeCADGui.Control.closeDialog() #close the dialog

    # What is done when we click on the cancel button.
    # commented because this is the default behaviour
    #def reject(self):
    #   FreeCADGui.Control.closeDialog()

# GUI command that links the Python script
class _MakeBoxDialogCmd:
    """Command to create a box with a Ok Cancel buttons
    """

    def Activated(self):
       # what is done when the command is clicked
        # creates a panel with a dialog
        baseWidget = QtGui.QWidget()
        panel = BoxSimpleTaskPanelPickPlace(baseWidget) 
        # having a panel with a widget in self.form and the accept and 
        # reject functions (if needed), we can open it:
        FreeCADGui.Control.showDialog(panel)
       # mydialogue = mywidget.plane()

    def GetResources(self):
        # icon and command information
        MenuText = QtCore.QT_TRANSLATE_NOOP(
            'Basic2_DBox',
            'Box Dialog')
        ToolTip = QtCore.QT_TRANSLATE_NOOP(
            'Basic2_DBox',
            'Creates pick and place position using a task panel dialog')
        return {
            'Pixmap': __dir__ + '/icons/placeholder.svg',
            'MenuText': MenuText,
            'ToolTip': ToolTip}

    def IsActive(self):
        # The command will be active if there is an active document
        return not FreeCAD.ActiveDocument is None

FreeCADGui.addCommand('Basic2_MakeBoxDialog', _MakeBoxDialogCmd())