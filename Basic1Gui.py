import PySide
from PySide import QtCore, QtGui
import FreeCAD
import FreeCADGui
import os

__dir__ = os.path.dirname(__file__)

# FreeCAD Command made with a Python script
def MakeBox():
    doc = FreeCAD.ActiveDocument
    box =  doc.addObject("Part::Box",'box')
    box.Length = 1
    box.Width  = 1
    box.Height = 1

# GUI command that links the Python script
class _MakeBoxCmd:
    """Command to create a box"""
    
    def Activated(self):
        # what is done when the command is clicked
        MakeBox()

    def GetResources(self):
        # icon and command information
        MenuText = QtCore.QT_TRANSLATE_NOOP(
            'Basic1_Box',
            'Box')
        ToolTip = QtCore.QT_TRANSLATE_NOOP(
            'Basic1_Box',
            'Creates a new box')
        return {
            'Pixmap': __dir__ + '/icons/settings.svg',
            'MenuText': MenuText,
            'ToolTip': ToolTip}

    def IsActive(self):
        # The command will be active if there is an active document
        return not FreeCAD.ActiveDocument is None

FreeCADGui.addCommand('Basic1_MakeBox', _MakeBoxCmd())