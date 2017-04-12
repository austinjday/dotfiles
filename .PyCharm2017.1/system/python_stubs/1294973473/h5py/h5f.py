# encoding: utf-8
# module h5py.h5f
# from C:\Users\austi\Anaconda3\lib\site-packages\h5py\h5f.cp36-win_amd64.pyd
# by generator 1.145
""" Low-level operations on HDF5 file objects. """

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import h5py._objects as _objects # C:\Users\austi\Anaconda3\lib\site-packages\h5py\_objects.cp36-win_amd64.pyd
import h5py.h5fd as h5fd # C:\Users\austi\Anaconda3\lib\site-packages\h5py\h5fd.cp36-win_amd64.pyd
from h5py._objects import (create, flush, get_name, get_obj_count, 
    get_obj_ids, is_hdf5, mount, open, unmount, with_phil)

import h5py.h5g as __h5py_h5g


# Variables with simple values

ACC_EXCL = 4
ACC_RDONLY = 0
ACC_RDWR = 1
ACC_TRUNC = 2

CLOSE_DEFAULT = 0
CLOSE_SEMI = 2
CLOSE_STRONG = 3
CLOSE_WEAK = 1

LIBVER_EARLIEST = 0
LIBVER_LATEST = 1

OBJ_ALL = 31
OBJ_ATTR = 16
OBJ_DATASET = 2
OBJ_DATATYPE = 8
OBJ_FILE = 1
OBJ_GROUP = 4
OBJ_LOCAL = 32

SCOPE_GLOBAL = 1
SCOPE_LOCAL = 0

# no functions
# classes

class FileID(__h5py_h5g.GroupID):
    """
    Represents an HDF5 file identifier.
    
            These objects wrap a small portion of the H5F interface; all the
            H5F functions which can take arbitrary objects in addition to
            file identifiers are provided as functions in the h5f module.
    
            Properties:
    
            * name:   File name on disk
    
            Behavior:
    
            * Hashable: Yes, unique to the file (but not the access mode)
            * Equality: Hash comparison
    """
    def close(self, *args, **kwargs): # real signature unknown
        """
        ()
        
                Terminate access through this identifier.  Note that depending on
                what property list settings were used to open the file, the
                physical file might not be closed until all remaining open
                identifiers are freed.
        """
        pass

    def get_access_plist(self, *args, **kwargs): # real signature unknown
        """
        () => PropFAID
        
                Retrieve a copy of the file access property list which manages access
                to this file.
        """
        pass

    def get_create_plist(self, *args, **kwargs): # real signature unknown
        """
        () => PropFCID
        
                Retrieve a copy of the file creation property list used to
                create this file.
        """
        pass

    def get_filesize(self, *args, **kwargs): # real signature unknown
        """
        () => LONG size
        
                Determine the total size (in bytes) of the HDF5 file,
                including any user block.
        """
        pass

    def get_freespace(self, *args, **kwargs): # real signature unknown
        """
        () => LONG freespace
        
                Determine the amount of free space in this file.  Note that this
                only tracks free space until the file is closed.
        """
        pass

    def get_intent(self, *args, **kwargs): # real signature unknown
        """
        () => INT
        
                Determine the file's write intent, either of:
                - H5F_ACC_RDONLY
                - H5F_ACC_RDWR
        """
        pass

    def get_mdc_config(self, *args, **kwargs): # real signature unknown
        """
        () => CacheConfig
                Returns an object that stores all the information about the meta-data cache
                configuration
        """
        pass

    def get_mdc_hit_rate(self, *args, **kwargs): # real signature unknown
        """
        () => DOUBLE
        
                Retrieve the cache hit rate
        """
        pass

    def get_mdc_size(self, *args, **kwargs): # real signature unknown
        """
        () => (max_size, min_clean_size, cur_size, cur_num_entries) [SIZE_T, SIZE_T, SIZE_T, INT]
        
                Obtain current metadata cache size data for specified file.
        """
        pass

    def get_vfd_handle(self, *args, **kwargs): # real signature unknown
        """
        () => INT
        
                Retrieve the file handle used by the virtual file driver.
        
                This method is only functional when the the SEC2 driver is used.
        """
        pass

    def reopen(self, *args, **kwargs): # real signature unknown
        """
        () => FileID
        
                Retrieve another identifier for a file (which must still be open).
                The new identifier is guaranteed to neither be mounted nor contain
                a mounted file.
        """
        pass

    def reset_mdc_hit_rate_stats(self, *args, **kwargs): # real signature unknown
        """
        no return
        
                rests the hit-rate statistics
        """
        pass

    def set_mdc_config(self, *args, **kwargs): # real signature unknown
        """
        (CacheConfig) => None
                Returns an object that stores all the information about the meta-data cache
                configuration
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """ File name on disk (according to h5f.get_name()) """



# variables with complex values

phil = _objects.phil

__loader__ = None # (!) real value is ''

__spec__ = None # (!) real value is ''

__test__ = {}

