# encoding: utf-8
# module astropy.stats.lombscargle.implementations.cython_impl
# from C:\Users\austi\Anaconda3\lib\site-packages\astropy\stats\lombscargle\implementations\cython_impl.cp36-win_amd64.pyd
# by generator 1.145
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import numpy as np # C:\Users\austi\Anaconda3\lib\site-packages\numpy\__init__.py
import numpy as __numpy


# functions

def lombscargle_cython(*args, **kwargs): # real signature unknown
    """
    Lomb-Scargle Periodogram
    
        This is a pure-python implementation of the original Lomb-Scargle formalism
        (e.g. [1]_, [2]_), with the addition of the floating mean (e.g. [3]_)
    
        Parameters
        ----------
        t, y, dy : array_like  (NOT astropy.Quantities)
            times, values, and errors of the data points. These should be
            broadcastable to the same shape.
        frequency : array_like
            frequencies (not angular frequencies) at which to calculate periodogram
        normalization : string (optional, default='standard')
            Normalization to use for the periodogram.
            Options are 'standard', 'model', 'log', or 'psd'.
        fit_mean : bool (optional, default=True)
            if True, include a constant offset as part of the model at each
            frequency. This can lead to more accurate results, especially in the
            case of incomplete phase coverage.
        center_data : bool (optional, default=True)
            if True, pre-center the data by subtracting the weighted mean
            of the input data. This is especially important if ``fit_mean = False``
    
        Returns
        -------
        power : array_like
            Lomb-Scargle power associated with each frequency.
            Units of the result depend on the normalization.
    
        References
        ----------
        .. [1] W. Press et al, Numerical Recipies in C (2002)
        .. [2] Scargle, J.D. 1982, ApJ 263:835-853
        .. [3] M. Zechmeister and M. Kurster, A&A 496, 577-584 (2009)
    """
    pass

# classes

class DTYPE(__numpy.floating, float):
    """ 64-bit floating-point number. Character code 'd'. Python float compatible. """
    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
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

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass

    __hash__ = None


class ITYPE(__numpy.signedinteger):
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


# variables with complex values

__loader__ = None # (!) real value is ''

__spec__ = None # (!) real value is ''

__test__ = {}

