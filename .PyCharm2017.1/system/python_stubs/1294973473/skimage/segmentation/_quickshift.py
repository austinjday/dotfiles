# encoding: utf-8
# module skimage.segmentation._quickshift
# from C:\Users\austi\Anaconda3\lib\site-packages\skimage\segmentation\_quickshift.cp36-win_amd64.pyd
# by generator 1.145
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import numpy as np # C:\Users\austi\Anaconda3\lib\site-packages\numpy\__init__.py
import scipy.ndimage as ndi # C:\Users\austi\Anaconda3\lib\site-packages\scipy\ndimage\__init__.py
from itertools import product


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

def quickshift(*args, **kwargs): # real signature unknown
    """
    Segments image using quickshift clustering in Color-(x,y) space.
    
        Produces an oversegmentation of the image using the quickshift mode-seeking
        algorithm.
    
        Parameters
        ----------
        image : (width, height, channels) ndarray
            Input image.
        ratio : float, optional, between 0 and 1 (default 1).
            Balances color-space proximity and image-space proximity.
            Higher values give more weight to color-space.
        kernel_size : float, optional (default 5)
            Width of Gaussian kernel used in smoothing the
            sample density. Higher means fewer clusters.
        max_dist : float, optional (default 10)
            Cut-off point for data distances.
            Higher means fewer clusters.
        return_tree : bool, optional (default False)
            Whether to return the full segmentation hierarchy tree and distances.
        sigma : float, optional (default 0)
            Width for Gaussian smoothing as preprocessing. Zero means no smoothing.
        convert2lab : bool, optional (default True)
            Whether the input should be converted to Lab colorspace prior to
            segmentation. For this purpose, the input is assumed to be RGB.
        random_seed : None (default) or int, optional
            Random seed used for breaking ties.
    
        Returns
        -------
        segment_mask : (width, height) ndarray
            Integer mask indicating segment labels.
    
        Notes
        -----
        The authors advocate to convert the image to Lab color space prior to
        segmentation, though this is not strictly necessary. For this to work, the
        image must be given in RGB format.
    
        References
        ----------
        .. [1] Quick shift and kernel methods for mode seeking,
               Vedaldi, A. and Soatto, S.
               European Conference on Computer Vision, 2008
    """
    pass

def rgb2lab(rgb): # reliably restored by inspect
    """
    RGB to lab color space conversion.
    
        Parameters
        ----------
        rgb : array_like
            The image in RGB format, in a 3- or 4-D array of shape
            ``(.., ..,[ ..,] 3)``.
    
        Returns
        -------
        out : ndarray
            The image in Lab format, in a 3- or 4-D array of shape
            ``(.., ..,[ ..,] 3)``.
    
        Raises
        ------
        ValueError
            If `rgb` is not a 3- or 4-D array of shape ``(.., ..,[ ..,] 3)``.
    
        Notes
        -----
        This function uses rgb2xyz and xyz2lab.
    """
    pass

# no classes
# variables with complex values

__loader__ = None # (!) real value is ''

__spec__ = None # (!) real value is ''

__test__ = {}

