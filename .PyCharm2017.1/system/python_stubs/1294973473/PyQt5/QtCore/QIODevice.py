# encoding: utf-8
# module PyQt5.QtCore
# from C:\Users\austi\Anaconda3\lib\site-packages\PyQt5\QtCore.pyd
# by generator 1.145
# no doc

# imports
import sip as __sip


from .QObject import QObject

class QIODevice(QObject):
    """
    QIODevice()
    QIODevice(QObject)
    """
    def aboutToClose(self): # real signature unknown; restored from __doc__
        """ aboutToClose(self) [signal] """
        pass

    def atEnd(self): # real signature unknown; restored from __doc__
        """ atEnd(self) -> bool """
        return False

    def bytesAvailable(self): # real signature unknown; restored from __doc__
        """ bytesAvailable(self) -> int """
        return 0

    def bytesToWrite(self): # real signature unknown; restored from __doc__
        """ bytesToWrite(self) -> int """
        return 0

    def bytesWritten(self, p_int): # real signature unknown; restored from __doc__
        """ bytesWritten(self, int) [signal] """
        pass

    def canReadLine(self): # real signature unknown; restored from __doc__
        """ canReadLine(self) -> bool """
        return False

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def close(self): # real signature unknown; restored from __doc__
        """ close(self) """
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def errorString(self): # real signature unknown; restored from __doc__
        """ errorString(self) -> str """
        return ""

    def getChar(self): # real signature unknown; restored from __doc__
        """ getChar(self) -> Tuple[bool, str] """
        pass

    def isOpen(self): # real signature unknown; restored from __doc__
        """ isOpen(self) -> bool """
        return False

    def isReadable(self): # real signature unknown; restored from __doc__
        """ isReadable(self) -> bool """
        return False

    def isSequential(self): # real signature unknown; restored from __doc__
        """ isSequential(self) -> bool """
        return False

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def isTextModeEnabled(self): # real signature unknown; restored from __doc__
        """ isTextModeEnabled(self) -> bool """
        return False

    def isWritable(self): # real signature unknown; restored from __doc__
        """ isWritable(self) -> bool """
        return False

    def open(self, Union, QIODevice_OpenMode=None, QIODevice_OpenModeFlag=None): # real signature unknown; restored from __doc__
        """ open(self, Union[QIODevice.OpenMode, QIODevice.OpenModeFlag]) -> bool """
        return False

    def openMode(self): # real signature unknown; restored from __doc__
        """ openMode(self) -> QIODevice.OpenMode """
        pass

    def peek(self, p_int): # real signature unknown; restored from __doc__
        """ peek(self, int) -> QByteArray """
        return QByteArray

    def pos(self): # real signature unknown; restored from __doc__
        """ pos(self) -> int """
        return 0

    def putChar(self, p_str): # real signature unknown; restored from __doc__
        """ putChar(self, str) -> bool """
        return False

    def read(self, p_int): # real signature unknown; restored from __doc__
        """ read(self, int) -> bytes """
        return b""

    def readAll(self): # real signature unknown; restored from __doc__
        """ readAll(self) -> QByteArray """
        return QByteArray

    def readChannelFinished(self): # real signature unknown; restored from __doc__
        """ readChannelFinished(self) [signal] """
        pass

    def readData(self, p_int): # real signature unknown; restored from __doc__
        """ readData(self, int) -> bytes """
        return b""

    def readLine(self, maxlen=0): # real signature unknown; restored from __doc__
        """ readLine(self, maxlen: int = 0) -> bytes """
        return b""

    def readLineData(self, p_int): # real signature unknown; restored from __doc__
        """ readLineData(self, int) -> bytes """
        return b""

    def readyRead(self): # real signature unknown; restored from __doc__
        """ readyRead(self) [signal] """
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def reset(self): # real signature unknown; restored from __doc__
        """ reset(self) -> bool """
        return False

    def seek(self, p_int): # real signature unknown; restored from __doc__
        """ seek(self, int) -> bool """
        return False

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setErrorString(self, p_str): # real signature unknown; restored from __doc__
        """ setErrorString(self, str) """
        pass

    def setOpenMode(self, Union, QIODevice_OpenMode=None, QIODevice_OpenModeFlag=None): # real signature unknown; restored from __doc__
        """ setOpenMode(self, Union[QIODevice.OpenMode, QIODevice.OpenModeFlag]) """
        pass

    def setTextModeEnabled(self, bool): # real signature unknown; restored from __doc__
        """ setTextModeEnabled(self, bool) """
        pass

    def size(self): # real signature unknown; restored from __doc__
        """ size(self) -> int """
        return 0

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def ungetChar(self, p_str): # real signature unknown; restored from __doc__
        """ ungetChar(self, str) """
        pass

    def waitForBytesWritten(self, p_int): # real signature unknown; restored from __doc__
        """ waitForBytesWritten(self, int) -> bool """
        return False

    def waitForReadyRead(self, p_int): # real signature unknown; restored from __doc__
        """ waitForReadyRead(self, int) -> bool """
        return False

    def write(self, Union, QByteArray=None, bytes=None, bytearray=None): # real signature unknown; restored from __doc__
        """ write(self, Union[QByteArray, bytes, bytearray]) -> int """
        return 0

    def writeData(self, bytes): # real signature unknown; restored from __doc__
        """ writeData(self, bytes) -> int """
        return 0

    def __init__(self, QObject=None): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    Append = 4
    NotOpen = 0
    ReadOnly = 1
    ReadWrite = 3
    Text = 16
    Truncate = 8
    Unbuffered = 32
    WriteOnly = 2


