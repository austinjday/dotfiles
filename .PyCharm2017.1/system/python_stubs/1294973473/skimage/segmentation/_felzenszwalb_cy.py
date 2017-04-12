# encoding: utf-8
# module skimage.segmentation._felzenszwalb_cy
# from C:\Users\austi\Anaconda3\lib\site-packages\skimage\segmentation\_felzenszwalb_cy.cp36-win_amd64.pyd
# by generator 1.145
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import numpy as np # C:\Users\austi\Anaconda3\lib\site-packages\numpy\__init__.py
import scipy.ndimage as ndi # C:\Users\austi\Anaconda3\lib\site-packages\scipy\ndimage\__init__.py

# functions

def img_as_float(image, force_copy=False): # reliably restored by inspect
    """
    Convert an image to double-precision floating point format.
    
        Parameters
        ----------
        image : ndarray
            Input image.
        force_copy : bool
            Force a copy of the data, irrespective of its current dtype.
    
        Returns
        -------
        out : ndarray of float64
            Output image.
    
        Notes
        -----
        The range of a floating point image is [0.0, 1.0] or [-1.0, 1.0] when
        converting from unsigned or signed datatypes, respectively.
    """
    pass

def _felzenszwalb_grey(*args, **kwargs): # real signature unknown
    """
    Felzenszwalb's efficient graph based segmentation for a single channel.
    
        Produces an oversegmentation of a 2d image using a fast, minimum spanning
        tree based clustering on the image grid.
        The number of produced segments as well as their size can only be
        controlled indirectly through ``scale``. Segment size within an image can
        vary greatly depending on local contrast.
    
        Parameters
        ----------
        image: ndarray
            Input image.
        scale: float, optional (default 1)
            Sets the obervation level. Higher means larger clusters.
        sigma: float, optional (default 0.8)
            Width of Gaussian smoothing kernel used in preprocessing.
            Larger sigma gives smother segment boundaries.
        min_size: int, optional (default 20)
            Minimum component size. Enforced using postprocessing.
    
        Returns
        -------
        segment_mask: (height, width) ndarray
            Integer mask indicating segment labels.
    """
    pass

# no classes
# variables with complex values

__loader__ = None # (!) real value is ''

__spec__ = None # (!) real value is ''

__test__ = {}

