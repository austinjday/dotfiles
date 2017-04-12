# encoding: utf-8
# module h5py.h5
# from C:\Users\austi\Anaconda3\lib\site-packages\h5py\h5.cp36-win_amd64.pyd
# by generator 1.145
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
from h5py._objects import get_libversion, with_phil


# Variables with simple values

INDEX_CRT_ORDER = 1

INDEX_NAME = 0

ITER_DEC = 1
ITER_INC = 0
ITER_NATIVE = 2

# functions

def get_config(*args, **kwargs): # real signature unknown
    """
    () => H5PYConfig
    
        Get a reference to the global library configuration object.
    """
    pass

# classes

class ByteStringContext(object):
    # no doc
    def __bool__(self, *args, **kwargs): # real signature unknown
        pass

    def __enter__(self, *args, **kwargs): # real signature unknown
        pass

    def __exit__(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __nonzero__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __dict__ = None # (!) real value is ''


class H5PYConfig(object):
    """
    Provides runtime access to global library settings.  You retrieve the
            master copy of this object by calling h5py.get_config().
    
            complex_names (tuple, r/w)
                Settable 2-tuple controlling how complex numbers are saved.
                Defaults to ('r','i').
    
            bool_names (tuple, r/w)
                Settable 2-tuple controlling the HDF5 enum names used for boolean
                values.  Defaults to ('FALSE', 'TRUE') for values 0 and 1.
    """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    API_16 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    API_18 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    bool_names = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """ Settable 2-tuple controlling HDF5 ENUM names for boolean types.

        Format is (false_name, real_name), defaulting to ('FALSE', 'TRUE').
        """

    complex_names = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """ Settable 2-tuple controlling how complex numbers are saved.

        Format is (real_name, imag_name), defaulting to ('r','i').
        """

    mpi = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """ Boolean indicating if Parallel HDF5 is available """

    read_byte_strings = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """ Returns a context manager which forces all strings to be returned
        as byte strings. """

    swmr_min_hdf5_version = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """ Tuple indicating the minimum HDF5 version required for SWMR features"""

    vds_min_hdf5_version = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Tuple indicating the minimum HDF5 version required for virtual dataset (VDS) features"""

    _bytestrings = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _f_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _i_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _r_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _t_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



# variables with complex values

phil = None # (!) real value is ''

__loader__ = None # (!) real value is ''

__pyx_capi__ = {
    'get_config': None, # (!) real value is ''
}

__spec__ = None # (!) real value is ''

__test__ = {}

