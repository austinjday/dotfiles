# encoding: utf-8
# module skimage._shared.interpolation
# from C:\Users\austi\Anaconda3\lib\site-packages\skimage\_shared\interpolation.cp36-win_amd64.pyd
# by generator 1.145
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import numpy as np # C:\Users\austi\Anaconda3\lib\site-packages\numpy\__init__.py

# functions

def coord_map_py(*args, **kwargs): # real signature unknown
    """ Python wrapper for `interpolation.coord_map`. """
    pass

def extend_image(*args, **kwargs): # real signature unknown
    """
    Pad a 2D image by `pad` pixels on each side.
    
        Parameters
        ----------
        image : ndarray
            Input image.
        pad : int, optional
            The number of pixels to pad around the border
        mode : {'constant', 'edge', 'symmetric', 'reflect', 'wrap'}, optional
            Points outside the boundaries of the input are filled according
            to the given mode.
        cval : float, optional
            Used in conjunction with mode 'constant', the value outside
            the image boundaries.
    
        Returns
        -------
        extended : ndarray
            The extended version of the input image.
    
        Notes
        -----
        For image padding, `skimage.util.pad` should be used instead.  This
        function is intended only for testing `get_pixel2d` and demonstrating the
        coordinate mapping modes implemented in `coord_map`.
    """
    pass

def _mode_deprecations(mode): # reliably restored by inspect
    """
    Used to update deprecated mode names in
        `skimage._shared.interpolation.pyx`.
    """
    pass

# no classes
# variables with complex values

__loader__ = None # (!) real value is ''

__spec__ = None # (!) real value is ''

__test__ = {}

