# encoding: utf-8
# module skimage.transform._hough_transform
# from C:\Users\austi\Anaconda3\lib\site-packages\skimage\transform\_hough_transform.cp36-win_amd64.pyd
# by generator 1.145
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import numpy as np # C:\Users\austi\Anaconda3\lib\site-packages\numpy\__init__.py
from skimage.draw._draw import circle_perimeter


# functions

def hough_ellipse(img, threshold=8): # real signature unknown; restored from __doc__
    """
    Perform an elliptical Hough transform.
    
        Parameters
        ----------
        img : (M, N) ndarray
            Input image with nonzero values representing edges.
        threshold: int, optional (default 4)
            Accumulator threshold value.
        accuracy : double, optional (default 1)
            Bin size on the minor axis used in the accumulator.
        min_size : int, optional (default 4)
            Minimal major axis length.
        max_size : int, optional
            Maximal minor axis length. (default None)
            If None, the value is set to the half of the smaller
            image dimension.
    
        Returns
        -------
        result : ndarray with fields [(accumulator, y0, x0, a, b, orientation)]
              Where ``(yc, xc)`` is the center, ``(a, b)`` the major and minor
              axes, respectively. The `orientation` value follows
              `skimage.draw.ellipse_perimeter` convention.
    
        Examples
        --------
        >>> img = np.zeros((25, 25), dtype=np.uint8)
        >>> rr, cc = ellipse_perimeter(10, 10, 6, 8)
        >>> img[cc, rr] = 1
        >>> result = hough_ellipse(img, threshold=8)
        [(10, 10.0, 8.0, 6.0, 0.0, 10.0)]
    
        Notes
        -----
        The accuracy must be chosen to produce a peak in the accumulator
        distribution. In other words, a flat accumulator distribution with low
        values may be caused by a too low bin size.
    
        References
        ----------
        .. [1] Xie, Yonghong, and Qiang Ji. "A new efficient ellipse detection
               method." Pattern Recognition, 2002. Proceedings. 16th International
               Conference on. Vol. 2. IEEE, 2002
    """
    pass

def hough_line(img): # real signature unknown; restored from __doc__
    """
    Perform a straight line Hough transform.
    
        Parameters
        ----------
        img : (M, N) ndarray
            Input image with nonzero values representing edges.
        theta : 1D ndarray of double
            Angles at which to compute the transform, in radians.
            Defaults to -pi/2 .. pi/2
    
        Returns
        -------
        H : 2-D ndarray of uint64
            Hough transform accumulator.
        theta : ndarray
            Angles at which the transform was computed, in radians.
        distances : ndarray
            Distance values.
    
        Notes
        -----
        The origin is the top left corner of the original image.
        X and Y axis are horizontal and vertical edges respectively.
        The distance is the minimal algebraic distance from the origin
        to the detected line.
    
        Examples
        --------
        Generate a test image:
    
        >>> img = np.zeros((100, 150), dtype=bool)
        >>> img[30, :] = 1
        >>> img[:, 65] = 1
        >>> img[35:45, 35:50] = 1
        >>> for i in range(90):
        ...     img[i, i] = 1
        >>> img += np.random.random(img.shape) > 0.95
    
        Apply the Hough transform:
    
        >>> out, angles, d = hough_line(img)
    
        .. plot:: hough_tf.py
    """
    pass

def probabilistic_hough_line(*args, **kwargs): # real signature unknown
    """
    Return lines from a progressive probabilistic line Hough transform.
    
        Parameters
        ----------
        img : (M, N) ndarray
            Input image with nonzero values representing edges.
        threshold : int, optional (default 10)
            Threshold
        line_length : int, optional (default 50)
            Minimum accepted length of detected lines.
            Increase the parameter to extract longer lines.
        line_gap : int, optional, (default 10)
            Maximum gap between pixels to still form a line.
            Increase the parameter to merge broken lines more aggresively.
        theta : 1D ndarray, dtype=double, optional, default (-pi/2 .. pi/2)
            Angles at which to compute the transform, in radians.
    
        Returns
        -------
        lines : list
          List of lines identified, lines in format ((x0, y0), (x1, y0)),
          indicating line start and end.
    
        References
        ----------
        .. [1] C. Galamhos, J. Matas and J. Kittler, "Progressive probabilistic
               Hough transform for line detection", in IEEE Computer Society
               Conference on Computer Vision and Pattern Recognition, 1999.
    """
    pass

def _hough_circle(*args, **kwargs): # real signature unknown
    """
    Perform a circular Hough transform.
    
        Parameters
        ----------
        img : (M, N) ndarray
            Input image with nonzero values representing edges.
        radius : ndarray
            Radii at which to compute the Hough transform.
        normalize : boolean, optional (default True)
            Normalize the accumulator with the number
            of pixels used to draw the radius.
        full_output : boolean, optional (default False)
            Extend the output size by twice the largest
            radius in order to detect centers outside the
            input picture.
    
        Returns
        -------
        H : 3D ndarray (radius index, (M + 2R, N + 2R) ndarray)
            Hough transform accumulator for each radius.
            R designates the larger radius if full_output is True.
            Otherwise, R = 0.
    """
    pass

# no classes
# variables with complex values

__loader__ = None # (!) real value is ''

__spec__ = None # (!) real value is ''

__test__ = {
    'hough_ellipse (line 101)': 'Perform an elliptical Hough transform.\n\n    Parameters\n    ----------\n    img : (M, N) ndarray\n        Input image with nonzero values representing edges.\n    threshold: int, optional (default 4)\n        Accumulator threshold value.\n    accuracy : double, optional (default 1)\n        Bin size on the minor axis used in the accumulator.\n    min_size : int, optional (default 4)\n        Minimal major axis length.\n    max_size : int, optional\n        Maximal minor axis length. (default None)\n        If None, the value is set to the half of the smaller\n        image dimension.\n\n    Returns\n    -------\n    result : ndarray with fields [(accumulator, y0, x0, a, b, orientation)]\n          Where ``(yc, xc)`` is the center, ``(a, b)`` the major and minor\n          axes, respectively. The `orientation` value follows\n          `skimage.draw.ellipse_perimeter` convention.\n\n    Examples\n    --------\n    >>> img = np.zeros((25, 25), dtype=np.uint8)\n    >>> rr, cc = ellipse_perimeter(10, 10, 6, 8)\n    >>> img[cc, rr] = 1\n    >>> result = hough_ellipse(img, threshold=8)\n    [(10, 10.0, 8.0, 6.0, 0.0, 10.0)]\n\n    Notes\n    -----\n    The accuracy must be chosen to produce a peak in the accumulator\n    distribution. In other words, a flat accumulator distribution with low\n    values may be caused by a too low bin size.\n\n    References\n    ----------\n    .. [1] Xie, Yonghong, and Qiang Ji. "A new efficient ellipse detection\n           method." Pattern Recognition, 2002. Proceedings. 16th International\n           Conference on. Vol. 2. IEEE, 2002\n    ',
    'hough_line (line 231)': 'Perform a straight line Hough transform.\n\n    Parameters\n    ----------\n    img : (M, N) ndarray\n        Input image with nonzero values representing edges.\n    theta : 1D ndarray of double\n        Angles at which to compute the transform, in radians.\n        Defaults to -pi/2 .. pi/2\n\n    Returns\n    -------\n    H : 2-D ndarray of uint64\n        Hough transform accumulator.\n    theta : ndarray\n        Angles at which the transform was computed, in radians.\n    distances : ndarray\n        Distance values.\n\n    Notes\n    -----\n    The origin is the top left corner of the original image.\n    X and Y axis are horizontal and vertical edges respectively.\n    The distance is the minimal algebraic distance from the origin\n    to the detected line.\n\n    Examples\n    --------\n    Generate a test image:\n\n    >>> img = np.zeros((100, 150), dtype=bool)\n    >>> img[30, :] = 1\n    >>> img[:, 65] = 1\n    >>> img[35:45, 35:50] = 1\n    >>> for i in range(90):\n    ...     img[i, i] = 1\n    >>> img += np.random.random(img.shape) > 0.95\n\n    Apply the Hough transform:\n\n    >>> out, angles, d = hough_line(img)\n\n    .. plot:: hough_tf.py\n\n    ',
}

