# encoding: utf-8
# module h5py._objects
# from C:\Users\austi\Anaconda3\lib\site-packages\h5py\_objects.cp36-win_amd64.pyd
# by generator 1.145
""" Implements ObjectID base class. """

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import weakref as weakref # C:\Users\austi\Anaconda3\lib\weakref.py
import warnings as warnings # C:\Users\austi\Anaconda3\lib\warnings.py

# functions

def nonlocal_close(*args, **kwargs): # real signature unknown
    """ Find dead ObjectIDs and set their integer identifiers to 0. """
    pass

def print_reg(*args, **kwargs): # real signature unknown
    pass

def with_phil(*args, **kwargs): # real signature unknown
    """ Locking decorator """
    pass

# classes

class BogoLock(object):
    # no doc
    def __enter__(self, *args, **kwargs): # real signature unknown
        pass

    def __exit__(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass


class FastRLock(object):
    """
    Fast, re-entrant locking.
    
        Under uncongested conditions, the lock is never acquired but only
        counted.  Only when a second thread comes in and notices that the
        lock is needed, it acquires the lock and notifies the first thread
        to release it when it's done.  This is all made possible by the
        wonderful GIL.
    """
    def acquire(self, *args, **kwargs): # real signature unknown
        pass

    def release(self, *args, **kwargs): # real signature unknown
        pass

    def _is_owned(self, *args, **kwargs): # real signature unknown
        pass

    def __enter__(self, *args, **kwargs): # real signature unknown
        pass

    def __exit__(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass


class ObjectID(object):
    """ Represents an HDF5 identifier. """
    def close(self, *args, **kwargs): # real signature unknown
        """ Close this identifier. """
        pass

    def _close(self, *args, **kwargs): # real signature unknown
        """ Manually close this object. """
        pass

    def __bool__(self, *args, **kwargs): # real signature unknown
        """ self != 0 """
        pass

    def __copy__(self, *args, **kwargs): # real signature unknown
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __hash__(self, *args, **kwargs): # real signature unknown
        """
        Default hashing mechanism for HDF5 objects
        
                Default hashing strategy:
                1. Try to hash based on the object's fileno and objno records
                2. If (1) succeeds, cache the resulting value
                3. If (1) fails, raise TypeError
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    fileno = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    locked = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    valid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



# variables with complex values

phil = None # (!) real value is ''

__loader__ = None # (!) real value is ''

__pyx_capi__ = {
    'pdefault': None, # (!) real value is ''
}

__spec__ = None # (!) real value is ''

__test__ = {}

