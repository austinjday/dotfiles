# encoding: utf-8
# module h5py.h5o
# from C:\Users\austi\Anaconda3\lib\site-packages\h5py\h5o.cp36-win_amd64.pyd
# by generator 1.145
""" Module for HDF5 "H5O" functions. """

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
from h5py._objects import (copy, get_comment, get_info, link, open, 
    set_comment, visit, with_phil)


# Variables with simple values

COPY_EXPAND_EXT_LINK_FLAG = 4

COPY_EXPAND_REFERENCE_FLAG = 8

COPY_EXPAND_SOFT_LINK_FLAG = 2

COPY_PRESERVE_NULL_FLAG = 32

COPY_SHALLOW_HIERARCHY_FLAG = 1

COPY_WITHOUT_ATTR_FLAG = 16

TYPE_DATASET = 1
TYPE_GROUP = 0

TYPE_NAMED_DATATYPE = 2

# no functions
# classes

class _ObjInfoBase(object):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass


class _ObjInfo(_ObjInfoBase):
    # no doc
    def _hash(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    addr = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    fileno = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    rc = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class ObjInfo(_ObjInfo):
    """ Represents the H5O_info_t structure """
    def __copy__(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    hdr = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class _ObjectVisitor(object):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass


class _OHdr(_ObjInfoBase):
    # no doc
    def _hash(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    mesg = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    nmesgs = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    space = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    version = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class _OHdrMesg(_ObjInfoBase):
    # no doc
    def _hash(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    present = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    shared = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class _OHdrSpace(_ObjInfoBase):
    # no doc
    def _hash(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    free = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    mesg = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    meta = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    total = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



# variables with complex values

phil = None # (!) real value is ''

__loader__ = None # (!) real value is ''

__spec__ = None # (!) real value is ''

__test__ = {}

