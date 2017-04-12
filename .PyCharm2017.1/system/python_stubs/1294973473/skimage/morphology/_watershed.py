# encoding: utf-8
# module skimage.morphology._watershed
# from C:\Users\austi\Anaconda3\lib\site-packages\skimage\morphology\_watershed.cp36-win_amd64.pyd
# by generator 1.145
"""
watershed.pyx - scithon implementation of guts of watershed

Originally part of CellProfiler, code licensed under both GPL and BSD licenses.
Website: http://www.cellprofiler.org

Copyright (c) 2003-2009 Massachusetts Institute of Technology
Copyright (c) 2009-2011 Broad Institute
All rights reserved.

Original author: Lee Kamentsky
"""

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import numpy as np # C:\Users\austi\Anaconda3\lib\site-packages\numpy\__init__.py

# functions

def watershed(*args, **kwargs): # real signature unknown
    """
    Do heavy lifting of watershed algorithm
    
        Parameters
        ----------
    
        image - the flattened image pixels, converted to rank-order
        pq    - the priority queue, starts with the marked pixels
                the first element in each row is the image intensity
                the second element is the age at entry into the queue
                the third element is the index into the flattened image or labels
                the remaining elements are the coordinates of the point
        age   - the next age to assign to a pixel
        structure - a numpy int32 array containing the structuring elements
                    that define nearest neighbors. For each row, the first
                    element is the stride from the point to its neighbor
                    in a flattened array. The remaining elements are the
                    offsets from the point to its neighbor in the various
                    dimensions
        mask  - numpy boolean (char) array indicating which pixels to consider
                and which to ignore. Also flattened.
        output - put the image labels in here
    """
    pass

# classes

class DTYPE_BOOL(int):
    """
    bool(x) -> bool
    
    Returns True when the argument x is true, False otherwise.
    The builtins True and False are the only two instances of the class bool.
    The class bool is a subclass of the class int, and cannot be subclassed.
    """
    def __and__(self, *args, **kwargs): # real signature unknown
        """ Return self&value. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __or__(self, *args, **kwargs): # real signature unknown
        """ Return self|value. """
        pass

    def __rand__(self, *args, **kwargs): # real signature unknown
        """ Return value&self. """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __ror__(self, *args, **kwargs): # real signature unknown
        """ Return value|self. """
        pass

    def __rxor__(self, *args, **kwargs): # real signature unknown
        """ Return value^self. """
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass

    def __xor__(self, *args, **kwargs): # real signature unknown
        """ Return self^value. """
        pass


# variables with complex values

__loader__ = None # (!) real value is ''

__spec__ = None # (!) real value is ''

__test__ = {}

