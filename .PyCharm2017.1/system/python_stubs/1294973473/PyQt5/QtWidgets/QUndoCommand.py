# encoding: utf-8
# module PyQt5.QtWidgets
# from C:\Users\austi\Anaconda3\lib\site-packages\PyQt5\QtWidgets.pyd
# by generator 1.145
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import PyQt5.QtGui as __PyQt5_QtGui


class QUndoCommand(): # skipped bases: <class 'sip.wrapper'>
    """
    QUndoCommand(parent: QUndoCommand = None)
    QUndoCommand(str, parent: QUndoCommand = None)
    """
    def actionText(self): # real signature unknown; restored from __doc__
        """ actionText(self) -> str """
        return ""

    def child(self, p_int): # real signature unknown; restored from __doc__
        """ child(self, int) -> QUndoCommand """
        return QUndoCommand

    def childCount(self): # real signature unknown; restored from __doc__
        """ childCount(self) -> int """
        return 0

    def id(self): # real signature unknown; restored from __doc__
        """ id(self) -> int """
        return 0

    def mergeWith(self, QUndoCommand): # real signature unknown; restored from __doc__
        """ mergeWith(self, QUndoCommand) -> bool """
        return False

    def redo(self): # real signature unknown; restored from __doc__
        """ redo(self) """
        pass

    def setText(self, p_str): # real signature unknown; restored from __doc__
        """ setText(self, str) """
        pass

    def text(self): # real signature unknown; restored from __doc__
        """ text(self) -> str """
        return ""

    def undo(self): # real signature unknown; restored from __doc__
        """ undo(self) """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



