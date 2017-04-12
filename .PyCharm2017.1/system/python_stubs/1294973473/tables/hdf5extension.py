# encoding: utf-8
# module tables.hdf5extension
# from C:\Users\austi\Anaconda3\lib\site-packages\tables\hdf5extension.cp36-win_amd64.pyd
# by generator 1.145
"""
Cython interface between several PyTables classes and HDF5 library.

Classes (type extensions):

    File
    AttributeSet
    Node
    Leaf
    Group
    Array
    VLArray
    UnImplemented

Functions:

Misc variables:
"""

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import os as os # C:\Users\austi\Anaconda3\lib\os.py
import warnings as warnings # C:\Users\austi\Anaconda3\lib\warnings.py
import pickle as pickle # C:\Users\austi\Anaconda3\lib\pickle.py
import numpy as numpy # C:\Users\austi\Anaconda3\lib\site-packages\numpy\__init__.py
from tables.utilsextension import (atom_from_hdf5_type, atom_to_hdf5_type, 
    create_nested_type, encode_filename, hdf5_to_np_ext_type, 
    set_blosc_max_threads)

import numpy as __numpy


# Variables with simple values

HAVE_DIRECT_DRIVER = False

HAVE_WINDOWS_DRIVER = True

platform_byteorder = 0

# functions

def check_file_access(filename, mode=None): # reliably restored by inspect
    """
    Check for file access in the specified `mode`.
    
        `mode` is one of the modes supported by `File` objects.  If the file
        indicated by `filename` can be accessed using that `mode`, the
        function ends successfully.  Else, an ``IOError`` is raised
        explaining the reason of the failure.
    
        All this paraphernalia is used to avoid the lengthy and scaring HDF5
        messages produced when there are problems opening a file.  No
        changes are ever made to the file system.
    """
    pass

def correct_byteorder(ptype, byteorder): # reliably restored by inspect
    """ Fix the byteorder depending on the PyTables types. """
    pass

def descr_from_dtype(dtype_): # reliably restored by inspect
    """ Get a description instance and byteorder from a (nested) NumPy dtype. """
    pass

# Error generating skeleton for function namedtuple: Function has keyword-only parameters or annotations, use getfullargspec() API which can support them

def previous_api(obj): # reliably restored by inspect
    """ A decorator-like function for dealing with deprecations. """
    pass

# classes

class Node(object):
    # no doc
    def _get_obj_info(self, *args, **kwargs): # real signature unknown
        pass

    def _g_delete(self, *args, **kwargs): # real signature unknown
        pass

    def _g_new(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass


class Leaf(Node):
    # no doc
    def _get_storage_size(self, *args, **kwargs): # real signature unknown
        pass

    def _g_close(self, *args, **kwargs): # real signature unknown
        pass

    def _g_flush(self, *args, **kwargs): # real signature unknown
        pass

    def _g_new(self, *args, **kwargs): # real signature unknown
        pass

    def _g_truncate(self, *args, **kwargs): # real signature unknown
        """ Truncate a Leaf to `size` nrows. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    __pyx_vtable__ = None # (!) real value is ''


class Array(Leaf):
    # no doc
    def perform_selection(self, *args, **kwargs): # real signature unknown
        """
        Performs a selection using start/count/step in the given axis.
        
            All other axes have their full range selected.  The selection is
            added to the current `space_id` selection using the given mode.
        
            Note: This is a backport from the h5py project.
        """
        pass

    def _append(self, *args, **kwargs): # real signature unknown
        pass

    def _createArray(self, *args, **kwargs): # real signature unknown
        pass

    def _createCArray(self, *args, **kwargs): # real signature unknown
        pass

    def _create_array(self, *args, **kwargs): # real signature unknown
        pass

    def _create_carray(self, *args, **kwargs): # real signature unknown
        pass

    def _g_readCoords(self, *args, **kwargs): # real signature unknown
        """ Read coordinates in an already created NumPy array. """
        pass

    def _g_readSelection(self, *args, **kwargs): # real signature unknown
        """ Read a selection in an already created NumPy array. """
        pass

    def _g_readSlice(self, *args, **kwargs): # real signature unknown
        pass

    def _g_read_coords(self, *args, **kwargs): # real signature unknown
        """ Read coordinates in an already created NumPy array. """
        pass

    def _g_read_selection(self, *args, **kwargs): # real signature unknown
        """ Read a selection in an already created NumPy array. """
        pass

    def _g_read_slice(self, *args, **kwargs): # real signature unknown
        pass

    def _g_writeCoords(self, *args, **kwargs): # real signature unknown
        """ Write a selection in an already created NumPy array. """
        pass

    def _g_writeSelection(self, *args, **kwargs): # real signature unknown
        """ Write a selection in an already created NumPy array. """
        pass

    def _g_writeSlice(self, *args, **kwargs): # real signature unknown
        """ Write a slice in an already created NumPy array. """
        pass

    def _g_write_coords(self, *args, **kwargs): # real signature unknown
        """ Write a selection in an already created NumPy array. """
        pass

    def _g_write_selection(self, *args, **kwargs): # real signature unknown
        """ Write a selection in an already created NumPy array. """
        pass

    def _g_write_slice(self, *args, **kwargs): # real signature unknown
        """ Write a slice in an already created NumPy array. """
        pass

    def _openArray(self, *args, **kwargs): # real signature unknown
        pass

    def _open_array(self, *args, **kwargs): # real signature unknown
        pass

    def _readArray(self, *args, **kwargs): # real signature unknown
        pass

    def _read_array(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    __pyx_vtable__ = None # (!) real value is ''


class Atom(object):
    """
    Defines the type of atomic cells stored in a dataset.
    
        The meaning of *atomic* is that individual elements of a cell can
        not be extracted directly by indexing (i.e.  __getitem__()) the
        dataset; e.g. if a dataset has shape (2, 2) and its atoms have
        shape (3,), to get the third element of the cell at (1, 0) one
        should use dataset[1,0][2] instead of dataset[1,0,2].
    
        The Atom class is meant to declare the different properties of the
        *base element* (also known as *atom*) of CArray, EArray and
        VLArray datasets, although they are also used to describe the base
        elements of Array datasets. Atoms have the property that their
        length is always the same.  However, you can grow datasets along
        the extensible dimension in the case of EArray or put a variable
        number of them on a VLArray row. Moreover, they are not restricted
        to scalar values, and they can be *fully multidimensional
        objects*.
    
        Parameters
        ----------
        itemsize : int
            For types with a non-fixed size, this sets the size in
            bytes of individual items in the atom.
        shape : tuple
            Sets the shape of the atom. An integer shape of
            N is equivalent to the tuple (N,).
        dflt
            Sets the default value for the atom.
    
        The following are the public methods and attributes of the Atom class.
    
        Notes
        -----
        A series of descendant classes are offered in order to make the
        use of these element descriptions easier. You should use a
        particular Atom descendant class whenever you know the exact type
        you will need when writing your code. Otherwise, you may use one
        of the Atom.from_*() factory Methods.
    
        .. rubric:: Atom attributes
    
        .. attribute:: dflt
    
            The default value of the atom.
    
            If the user does not supply a value for an element while
            filling a dataset, this default value will be written to disk.
            If the user supplies a scalar value for a multidimensional
            atom, this value is automatically *broadcast* to all the items
            in the atom cell. If dflt is not supplied, an appropriate zero
            value (or *null* string) will be chosen by default.  Please
            note that default values are kept internally as NumPy objects.
    
        .. attribute:: dtype
    
            The NumPy dtype that most closely matches this atom.
    
        .. attribute:: itemsize
    
            Size in bytes of a single item in the atom.
            Specially useful for atoms of the string kind.
    
        .. attribute:: kind
    
            The PyTables kind of the atom (a string).
    
        .. attribute:: shape
    
            The shape of the atom (a tuple for scalar atoms).
    
        .. attribute:: type
    
            The PyTables type of the atom (a string).
    
            Atoms can be compared with atoms and other objects for
            strict (in)equality without having to compare individual
            attributes::
    
                >>> atom1 = StringAtom(itemsize=10)  # same as ``atom2``
                >>> atom2 = Atom.from_kind('string', 10)  # same as ``atom1``
                >>> atom3 = IntAtom()
                >>> atom1 == 'foo'
                False
                >>> atom1 == atom2
                True
                >>> atom2 != atom1
                False
                >>> atom1 == atom3
                False
                >>> atom3 != atom2
                True
    """
    def copy(self, **override): # reliably restored by inspect
        """
        Get a copy of the atom, possibly overriding some arguments.
        
                Constructor arguments to be overridden must be passed as
                keyword arguments::
        
                    >>> atom1 = Int32Atom(shape=12)
                    >>> atom2 = atom1.copy()
                    >>> print(atom1)
                    Int32Atom(shape=(12,), dflt=0)
                    >>> print(atom2)
                    Int32Atom(shape=(12,), dflt=0)
                    >>> atom1 is atom2
                    False
                    >>> atom3 = atom1.copy(shape=(2, 2))
                    >>> print(atom3)
                    Int32Atom(shape=(2, 2), dflt=0)
                    >>> atom1.copy(foobar=42)
                    Traceback (most recent call last):
                    ...
                    TypeError: __init__() got an unexpected keyword argument 'foobar'
        """
        pass

    @classmethod
    def from_dtype(cls, numpy_dtype, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        Create an Atom from a NumPy dtype.
        
                An optional default value may be specified as the dflt
                argument. Information in the dtype not represented in an Atom is
                ignored::
        
                    >>> import numpy
                    >>> Atom.from_dtype(numpy.dtype((numpy.int16, (2, 2))))
                    Int16Atom(shape=(2, 2), dflt=0)
                    >>> Atom.from_dtype(numpy.dtype('Float64'))
                    Float64Atom(shape=(), dflt=0.0)
        """
        pass

    @classmethod
    def from_kind(cls, p_int, itemsize=2, shape=22): # real signature unknown; restored from __doc__
        """
        Create an Atom from a PyTables kind.
        
                Optional item size, shape and default value may be
                specified as the itemsize, shape and dflt
                arguments, respectively. Bear in mind that not all atoms support
                a default item size::
        
                    >>> Atom.from_kind('int', itemsize=2, shape=(2, 2))
                    Int16Atom(shape=(2, 2), dflt=0)
                    >>> Atom.from_kind('int', shape=(2, 2))
                    Int32Atom(shape=(2, 2), dflt=0)
                    >>> Atom.from_kind('int', shape=1)
                    Int32Atom(shape=(1,), dflt=0)
                    >>> Atom.from_kind('string', dflt=b'hello')
                    Traceback (most recent call last):
                    ...
                    ValueError: no default item size for kind ``string``
                    >>> Atom.from_kind('Float')
                    Traceback (most recent call last):
                    ...
                    ValueError: unknown kind: 'Float'
        
                Moreover, some kinds with atypical constructor signatures
                are not supported; you need to use the proper
                constructor::
        
                    >>> Atom.from_kind('enum') #doctest: +ELLIPSIS
                    Traceback (most recent call last):
                    ...
                    ValueError: the ``enum`` kind is not supported...
        """
        pass

    @classmethod
    def from_sctype(cls, numpy_int16, shape=22): # real signature unknown; restored from __doc__
        """
        Create an Atom from a NumPy scalar type sctype.
        
                Optional shape and default value may be specified as the
                shape and dflt
                arguments, respectively. Information in the
                sctype not represented in an Atom is ignored::
        
                    >>> import numpy
                    >>> Atom.from_sctype(numpy.int16, shape=(2, 2))
                    Int16Atom(shape=(2, 2), dflt=0)
                    >>> Atom.from_sctype('S5', dflt='hello')
                    Traceback (most recent call last):
                    ...
                    ValueError: unknown NumPy scalar type: 'S5'
                    >>> Atom.from_sctype('Float64')
                    Float64Atom(shape=(), dflt=0.0)
        """
        pass

    @classmethod
    def from_type(cls, bool): # real signature unknown; restored from __doc__
        """
        Create an Atom from a PyTables type.
        
                Optional shape and default value may be specified as the
                shape and dflt arguments, respectively::
        
                    >>> Atom.from_type('bool')
                    BoolAtom(shape=(), dflt=False)
                    >>> Atom.from_type('int16', shape=(2, 2))
                    Int16Atom(shape=(2, 2), dflt=0)
                    >>> Atom.from_type('string40', dflt='hello')
                    Traceback (most recent call last):
                    ...
                    ValueError: unknown type: 'string40'
                    >>> Atom.from_type('Float64')
                    Traceback (most recent call last):
                    ...
                    ValueError: unknown type: 'Float64'
        """
        pass

    @classmethod
    def prefix(cls, *args, **kwargs): # real signature unknown
        """ Return the atom class prefix. """
        pass

    def _get_init_args(self): # reliably restored by inspect
        """
        Get a dictionary of instance constructor arguments.
        
                This implementation works on classes which use the same names
                for both constructor arguments and instance attributes.
        """
        pass

    def _is_equal_to_atom(self, atom): # reliably restored by inspect
        """ Is this object equal to the given `atom`? """
        pass

    def __eq__(self, other): # reliably restored by inspect
        # no doc
        pass

    def __init__(self, nptype, shape, dflt): # reliably restored by inspect
        # no doc
        pass

    def __ne__(self, other): # reliably restored by inspect
        # no doc
        pass

    def __repr__(self): # reliably restored by inspect
        # no doc
        pass

    ndim = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The number of dimensions of the atom.

        .. versionadded:: 2.4"""

    recarrtype = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """String type to be used in numpy.rec.array()."""

    size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Total size in bytes of the atom."""

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __dict__ = None # (!) real value is ''
    __hash__ = None


class AttributeSet(object):
    # no doc
    def _g_getattr(self, *args, **kwargs): # real signature unknown
        """
        Get HDF5 attributes and retrieve them as NumPy objects.
        
            H5T_SCALAR types will be retrieved as scalar NumPy.
            H5T_ARRAY types will be retrieved as ndarray NumPy objects.
        """
        pass

    def _g_getAttr(self, *args, **kwargs): # real signature unknown
        """
        Get HDF5 attributes and retrieve them as NumPy objects.
        
            H5T_SCALAR types will be retrieved as scalar NumPy.
            H5T_ARRAY types will be retrieved as ndarray NumPy objects.
        """
        pass

    def _g_listAttr(self, *args, **kwargs): # real signature unknown
        """ Return a tuple with the attribute list """
        pass

    def _g_list_attr(self, *args, **kwargs): # real signature unknown
        """ Return a tuple with the attribute list """
        pass

    def _g_new(self, *args, **kwargs): # real signature unknown
        pass

    def _g_remove(self, *args, **kwargs): # real signature unknown
        pass

    def _g_setattr(self, *args, **kwargs): # real signature unknown
        """
        Save Python or NumPy objects as HDF5 attributes.
        
            Scalar Python objects, scalar NumPy & 0-dim NumPy objects will all be
            saved as H5T_SCALAR type.  N-dim NumPy objects will be saved as H5T_ARRAY
            type.
        """
        pass

    def _g_setAttr(self, *args, **kwargs): # real signature unknown
        """
        Save Python or NumPy objects as HDF5 attributes.
        
            Scalar Python objects, scalar NumPy & 0-dim NumPy objects will all be
            saved as H5T_SCALAR type.  N-dim NumPy objects will be saved as H5T_ARRAY
            type.
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass


class DataTypeWarning(Warning):
    """
    Unsupported data type.
    
        This warning is issued when an unsupported HDF5 data type is found
        (normally in a file created with other tool than PyTables).
    """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class File(object):
    # no doc
    def fileno(self, *args, **kwargs): # real signature unknown
        """
        Return the underlying OS integer file descriptor.
        
            This is needed for lower-level file interfaces, such as the ``fcntl``
            module.
        """
        pass

    def get_filesize(self, *args, **kwargs): # real signature unknown
        """
        Returns the size of an HDF5 file.
        
            The returned size is that of the entire file, as opposed to only
            the HDF5 portion of the file. I.e., size includes the user block,
            if any, the HDF5 portion of the file, and any data that may have
            been appended beyond the data written through the HDF5 Library.
        
            .. versionadded:: 3.0
        """
        pass

    def get_file_image(self, *args, **kwargs): # real signature unknown
        """
        Retrieves an in-memory image of an existing, open HDF5 file.
        
            .. note:: this method requires HDF5 >= 1.8.9.
        
            .. versionadded:: 3.0
        """
        pass

    def get_userblock_size(self, *args, **kwargs): # real signature unknown
        """
        Retrieves the size of a user block.
        
            .. versionadded:: 3.0
        """
        pass

    def _closeFile(self, *args, **kwargs): # real signature unknown
        pass

    def _close_file(self, *args, **kwargs): # real signature unknown
        pass

    def _flushFile(self, *args, **kwargs): # real signature unknown
        pass

    def _flush_file(self, *args, **kwargs): # real signature unknown
        pass

    def _getFileId(self, *args, **kwargs): # real signature unknown
        pass

    def _get_file_id(self, *args, **kwargs): # real signature unknown
        pass

    def _g_new(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass


class Group(Node):
    # no doc
    def _g_closeGroup(self, *args, **kwargs): # real signature unknown
        pass

    def _g_close_group(self, *args, **kwargs): # real signature unknown
        pass

    def _g_create(self, *args, **kwargs): # real signature unknown
        pass

    def _g_flushGroup(self, *args, **kwargs): # real signature unknown
        pass

    def _g_flush_group(self, *args, **kwargs): # real signature unknown
        pass

    def _g_getGChildAttr(self, *args, **kwargs): # real signature unknown
        """
        Return an attribute of a child `Group`.
        
            If the attribute does not exist, ``None`` is returned.
        """
        pass

    def _g_getLChildAttr(self, *args, **kwargs): # real signature unknown
        """
        Return an attribute of a child `Leaf`.
        
            If the attribute does not exist, ``None`` is returned.
        """
        pass

    def _g_get_gchild_attr(self, *args, **kwargs): # real signature unknown
        """
        Return an attribute of a child `Group`.
        
            If the attribute does not exist, ``None`` is returned.
        """
        pass

    def _g_get_lchild_attr(self, *args, **kwargs): # real signature unknown
        """
        Return an attribute of a child `Leaf`.
        
            If the attribute does not exist, ``None`` is returned.
        """
        pass

    def _g_get_objinfo(self, *args, **kwargs): # real signature unknown
        """ Check whether 'name' is a children of 'self' and return its type. """
        pass

    def _g_listGroup(self, *args, **kwargs): # real signature unknown
        """ Return a tuple with the groups and the leaves hanging from self. """
        pass

    def _g_list_group(self, *args, **kwargs): # real signature unknown
        """ Return a tuple with the groups and the leaves hanging from self. """
        pass

    def _g_moveNode(self, *args, **kwargs): # real signature unknown
        pass

    def _g_move_node(self, *args, **kwargs): # real signature unknown
        pass

    def _g_open(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass


class HDF5ExtError(RuntimeError):
    """
    A low level HDF5 operation failed.
    
        This exception is raised the low level PyTables components used for
        accessing HDF5 files.  It usually signals that something is not
        going well in the HDF5 library or even at the Input/Output level.
    
        Errors in the HDF5 C library may be accompanied by an extensive
        HDF5 back trace on standard error (see also
        :func:`tables.silence_hdf5_messages`).
    
        .. versionchanged:: 2.4
    
        Parameters
        ----------
        message
            error message
        h5bt
            This parameter (keyword only) controls the HDF5 back trace
            handling. Any keyword arguments other than h5bt is ignored.
    
            * if set to False the HDF5 back trace is ignored and the
              :attr:`HDF5ExtError.h5backtrace` attribute is set to None
            * if set to True the back trace is retrieved from the HDF5
              library and stored in the :attr:`HDF5ExtError.h5backtrace`
              attribute as a list of tuples
            * if set to "VERBOSE" (default) the HDF5 back trace is
              stored in the :attr:`HDF5ExtError.h5backtrace` attribute
              and also included in the string representation of the
              exception
            * if not set (or set to None) the default policy is used
              (see :attr:`HDF5ExtError.DEFAULT_H5_BACKTRACE_POLICY`)
    """
    def format_h5_backtrace(self, backtrace=None): # reliably restored by inspect
        """
        Convert the HDF5 trace back represented as a list of tuples.
                (see :attr:`HDF5ExtError.h5backtrace`) into a string.
        
                .. versionadded:: 2.4
        """
        pass

    @classmethod
    def set_policy_from_env(cls, *args, **kwargs): # real signature unknown
        pass

    def _dump_h5_backtrace(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def __str__(self): # reliably restored by inspect
        """
        Returns a sting representation of the exception.
        
                The actual result depends on policy set in the initializer
                :meth:`HDF5ExtError.__init__`.
        
                .. versionadded:: 2.4
        """
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    DEFAULT_H5_BACKTRACE_POLICY = 'VERBOSE'


class ObjInfo(tuple):
    """ ObjInfo(addr, rc) """
    def _asdict(self): # reliably restored by inspect
        """ Return a new OrderedDict which maps field names to their values. """
        pass

    @classmethod
    def _make(cls, *args, **kwargs): # real signature unknown
        """ Make a new ObjInfo object from a sequence or iterable """
        pass

    def _replace(_self, **kwds): # reliably restored by inspect
        """ Return a new ObjInfo object replacing specified fields with new values """
        pass

    def __getnewargs__(self): # reliably restored by inspect
        """ Return self as a plain tuple.  Used by copy and pickle. """
        pass

    def __init__(self, addr, rc): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(_cls, addr, rc): # reliably restored by inspect
        """ Create new instance of ObjInfo(addr, rc) """
        pass

    def __repr__(self): # reliably restored by inspect
        """ Return a nicely formatted representation string """
        pass

    addr = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Alias for field number 0"""

    rc = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Alias for field number 1"""


    _fields = (
        'addr',
        'rc',
    )
    _source = "from builtins import property as _property, tuple as _tuple\nfrom operator import itemgetter as _itemgetter\nfrom collections import OrderedDict\n\nclass ObjInfo(tuple):\n    'ObjInfo(addr, rc)'\n\n    __slots__ = ()\n\n    _fields = ('addr', 'rc')\n\n    def __new__(_cls, addr, rc):\n        'Create new instance of ObjInfo(addr, rc)'\n        return _tuple.__new__(_cls, (addr, rc))\n\n    @classmethod\n    def _make(cls, iterable, new=tuple.__new__, len=len):\n        'Make a new ObjInfo object from a sequence or iterable'\n        result = new(cls, iterable)\n        if len(result) != 2:\n            raise TypeError('Expected 2 arguments, got %d' % len(result))\n        return result\n\n    def _replace(_self, **kwds):\n        'Return a new ObjInfo object replacing specified fields with new values'\n        result = _self._make(map(kwds.pop, ('addr', 'rc'), _self))\n        if kwds:\n            raise ValueError('Got unexpected field names: %r' % list(kwds))\n        return result\n\n    def __repr__(self):\n        'Return a nicely formatted representation string'\n        return self.__class__.__name__ + '(addr=%r, rc=%r)' % self\n\n    def _asdict(self):\n        'Return a new OrderedDict which maps field names to their values.'\n        return OrderedDict(zip(self._fields, self))\n\n    def __getnewargs__(self):\n        'Return self as a plain tuple.  Used by copy and pickle.'\n        return tuple(self)\n\n    addr = _property(_itemgetter(0), doc='Alias for field number 0')\n\n    rc = _property(_itemgetter(1), doc='Alias for field number 1')\n\n"
    __slots__ = ()


class SizeType(__numpy.signedinteger):
    """ 64-bit integer. Character code 'l'. Python int compatible. """
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
        """ Return hash(self). """
        pass

    def __index__(self, *args, **kwargs): # real signature unknown
        """ Return self converted to an integer, if self is suitable for use as an index into a list. """
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


class UnImplemented(Leaf):
    # no doc
    def _g_close(self, *args, **kwargs): # real signature unknown
        pass

    def _open_unimplemented(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    __pyx_vtable__ = None # (!) real value is ''


class VLArray(Leaf):
    # no doc
    def get_row_size(self, *args, **kwargs): # real signature unknown
        """ Return the total size in bytes of all the elements contained in a given row. """
        pass

    def _append(self, *args, **kwargs): # real signature unknown
        pass

    def _createArray(self, *args, **kwargs): # real signature unknown
        pass

    def _create_array(self, *args, **kwargs): # real signature unknown
        pass

    def _get_memory_size(self, *args, **kwargs): # real signature unknown
        pass

    def _modify(self, *args, **kwargs): # real signature unknown
        pass

    def _openArray(self, *args, **kwargs): # real signature unknown
        pass

    def _open_array(self, *args, **kwargs): # real signature unknown
        pass

    def _readArray(self, *args, **kwargs): # real signature unknown
        pass

    def _read_array(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    __pyx_vtable__ = None # (!) real value is ''


# variables with complex values

byteorders = {
    '<': 'little',
    '=': 'little',
    '>': 'big',
    '|': 'irrelevant',
}

hdf5_class_to_string = {
    -1: 'H5T_NO_CLASS',
    0: 'H5T_INTEGER',
    1: 'H5T_FLOAT',
    2: 'H5T_TIME',
    3: 'H5T_STRING',
    4: 'H5T_BITFIELD',
    5: 'H5T_OPAQUE',
    6: 'H5T_COMPOUND',
    7: 'H5T_REFERENCE',
    8: 'H5T_ENUM',
    9: 'H5T_VLEN',
    10: 'H5T_ARRAY',
}

npext_prefixes_to_ptkinds = {
    'S': 'string',
    'b': 'bool',
    'c': 'complex',
    'e': 'enum',
    'f': 'float',
    'i': 'int',
    't': 'time',
    'u': 'uint',
}

pttype_to_hdf5 = {
    'float128': 50331692,
    'float32': 50331702,
    'float64': 50331704,
    'float96': 50331692,
    'int16': 50331710,
    'int32': 50331712,
    'int64': 50331714,
    'int8': 50331708,
    'time32': 50331732,
    'time64': 50331734,
    'uint16': 50331718,
    'uint32': 50331720,
    'uint64': 50331722,
    'uint8': 50331716,
}

pt_special_kinds = [
    'complex',
    'string',
    'enum',
    'bool',
]

_supported_drivers = (
    'H5FD_SEC2',
    'H5FD_DIRECT',
    'H5FD_WINDOWS',
    'H5FD_STDIO',
    'H5FD_CORE',
    'H5FD_SPLIT',
)

__loader__ = None # (!) real value is ''

__spec__ = None # (!) real value is ''

__test__ = {}

