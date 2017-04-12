# encoding: utf-8
# module h5py.h5r
# from C:\Users\austi\Anaconda3\lib\site-packages\h5py\h5r.cp36-win_amd64.pyd
# by generator 1.145
""" H5R API for object and region references. """

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
from h5py._objects import (create, dereference, get_name, get_obj_type, 
    get_region, with_phil)


# Variables with simple values

DATASET_REGION = 1

OBJECT = 0

# no functions
# classes

class Reference(object):
    """
    Opaque representation of an HDF5 reference.
    
            Objects of this class are created exclusively by the library and
            cannot be modified.  The read-only attribute "typecode" determines
            whether the reference is to an object in an HDF5 file (OBJECT)
            or a dataset region (DATASET_REGION).
    
            The object's truth value indicates whether it contains a nonzero
            reference.  This does not guarantee that is valid, but is useful
            for rejecting "background" elements in a dataset.
    """
    def __bool__(self, *args, **kwargs): # real signature unknown
        """ self != 0 """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    typecode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    typesize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class RegionReference(Reference):
    """
    Opaque representation of an HDF5 region reference.
    
            This is a subclass of Reference which exists mainly for programming
            convenience.
    """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass


# variables with complex values

phil = None # (!) real value is ''

__loader__ = None # (!) real value is ''

__spec__ = None # (!) real value is ''

__test__ = {}

