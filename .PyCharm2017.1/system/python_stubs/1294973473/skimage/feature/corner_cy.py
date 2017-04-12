# encoding: utf-8
# module skimage.feature.corner_cy
# from C:\Users\austi\Anaconda3\lib\site-packages\skimage\feature\corner_cy.cp36-win_amd64.pyd
# by generator 1.145
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import numpy as np # C:\Users\austi\Anaconda3\lib\site-packages\numpy\__init__.py

# functions

def corner_moravec(square): # real signature unknown; restored from __doc__
    """
    Compute Moravec corner measure response image.
    
        This is one of the simplest corner detectors and is comparatively fast but
        has several limitations (e.g. not rotation invariant).
    
        Parameters
        ----------
        image : ndarray
            Input image.
        window_size : int, optional (default 1)
            Window size.
    
        Returns
        -------
        response : ndarray
            Moravec response image.
    
        References
        ----------
        .. [1] http://kiwi.cs.dal.ca/~dparks/CornerDetection/moravec.htm
        .. [2] http://en.wikipedia.org/wiki/Corner_detection
    
        Examples
        --------
        >>> from skimage.feature import corner_moravec
        >>> square = np.zeros([7, 7])
        >>> square[3, 3] = 1
        >>> square.astype(int)
        array([[0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 1, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0]])
        >>> corner_moravec(square).astype(int)
        array([[0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0],
               [0, 0, 1, 1, 1, 0, 0],
               [0, 0, 1, 2, 1, 0, 0],
               [0, 0, 1, 1, 1, 0, 0],
               [0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0]])
    """
    pass

def corner_orientations(square, corners, octagon, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    Compute the orientation of corners.
    
        The orientation of corners is computed using the first order central moment
        i.e. the center of mass approach. The corner orientation is the angle of
        the vector from the corner coordinate to the intensity centroid in the
        local neighborhood around the corner calculated using first order central
        moment.
    
        Parameters
        ----------
        image : 2D array
            Input grayscale image.
        corners : (N, 2) array
            Corner coordinates as ``(row, col)``.
        mask : 2D array
            Mask defining the local neighborhood of the corner used for the
            calculation of the central moment.
    
        Returns
        -------
        orientations : (N, 1) array
            Orientations of corners in the range [-pi, pi].
    
        References
        ----------
        .. [1] Ethan Rublee, Vincent Rabaud, Kurt Konolige and Gary Bradski
              "ORB : An efficient alternative to SIFT and SURF"
              http://www.vision.cs.chubu.ac.jp/CV-R/pdf/Rublee_iccv2011.pdf
        .. [2] Paul L. Rosin, "Measuring Corner Properties"
              http://users.cs.cf.ac.uk/Paul.Rosin/corner2.pdf
    
        Examples
        --------
        >>> from skimage.morphology import octagon
        >>> from skimage.feature import (corner_fast, corner_peaks,
        ...                              corner_orientations)
        >>> square = np.zeros((12, 12))
        >>> square[3:9, 3:9] = 1
        >>> square.astype(int)
        array([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0],
               [0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0],
               [0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0],
               [0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0],
               [0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0],
               [0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])
        >>> corners = corner_peaks(corner_fast(square, 9), min_distance=1)
        >>> corners
        array([[3, 3],
               [3, 8],
               [8, 3],
               [8, 8]])
        >>> orientations = corner_orientations(square, corners, octagon(3, 2))
        >>> np.rad2deg(orientations)
        array([  45.,  135.,  -45., -135.])
    """
    pass

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

def pad(array, pad_width, mode=None, **kwargs): # reliably restored by inspect
    """
    Pads an array.
    
        Parameters
        ----------
        array : array_like of rank N
            Input array
        pad_width : {sequence, array_like, int}
            Number of values padded to the edges of each axis.
            ((before_1, after_1), ... (before_N, after_N)) unique pad widths
            for each axis.
            ((before, after),) yields same before and after pad for each axis.
            (pad,) or int is a shortcut for before = after = pad width for all
            axes.
        mode : str or function
            One of the following string values or a user supplied function.
    
            'constant'
                Pads with a constant value.
            'edge'
                Pads with the edge values of array.
            'linear_ramp'
                Pads with the linear ramp between end_value and the
                array edge value.
            'maximum'
                Pads with the maximum value of all or part of the
                vector along each axis.
            'mean'
                Pads with the mean value of all or part of the
                vector along each axis.
            'median'
                Pads with the median value of all or part of the
                vector along each axis.
            'minimum'
                Pads with the minimum value of all or part of the
                vector along each axis.
            'reflect'
                Pads with the reflection of the vector mirrored on
                the first and last values of the vector along each
                axis.
            'symmetric'
                Pads with the reflection of the vector mirrored
                along the edge of the array.
            'wrap'
                Pads with the wrap of the vector along the axis.
                The first values are used to pad the end and the
                end values are used to pad the beginning.
            <function>
                Padding function, see Notes.
        stat_length : sequence or int, optional
            Used in 'maximum', 'mean', 'median', and 'minimum'.  Number of
            values at edge of each axis used to calculate the statistic value.
    
            ((before_1, after_1), ... (before_N, after_N)) unique statistic
            lengths for each axis.
    
            ((before, after),) yields same before and after statistic lengths
            for each axis.
    
            (stat_length,) or int is a shortcut for before = after = statistic
            length for all axes.
    
            Default is ``None``, to use the entire axis.
        constant_values : sequence or int, optional
            Used in 'constant'.  The values to set the padded values for each
            axis.
    
            ((before_1, after_1), ... (before_N, after_N)) unique pad constants
            for each axis.
    
            ((before, after),) yields same before and after constants for each
            axis.
    
            (constant,) or int is a shortcut for before = after = constant for
            all axes.
    
            Default is 0.
        end_values : sequence or int, optional
            Used in 'linear_ramp'.  The values used for the ending value of the
            linear_ramp and that will form the edge of the padded array.
    
            ((before_1, after_1), ... (before_N, after_N)) unique end values
            for each axis.
    
            ((before, after),) yields same before and after end values for each
            axis.
    
            (constant,) or int is a shortcut for before = after = end value for
            all axes.
    
            Default is 0.
        reflect_type : {'even', 'odd'}, optional
            Used in 'reflect', and 'symmetric'.  The 'even' style is the
            default with an unaltered reflection around the edge value.  For
            the 'odd' style, the extented part of the array is created by
            subtracting the reflected values from two times the edge value.
    
        Returns
        -------
        pad : ndarray
            Padded array of rank equal to `array` with shape increased
            according to `pad_width`.
    
        Notes
        -----
        .. versionadded:: 1.7.0
    
        For an array with rank greater than 1, some of the padding of later
        axes is calculated from padding of previous axes.  This is easiest to
        think about with a rank 2 array where the corners of the padded array
        are calculated by using padded values from the first axis.
    
        The padding function, if used, should return a rank 1 array equal in
        length to the vector argument with padded values replaced. It has the
        following signature::
    
            padding_func(vector, iaxis_pad_width, iaxis, **kwargs)
    
        where
    
            vector : ndarray
                A rank 1 array already padded with zeros.  Padded values are
                vector[:pad_tuple[0]] and vector[-pad_tuple[1]:].
            iaxis_pad_width : tuple
                A 2-tuple of ints, iaxis_pad_width[0] represents the number of
                values padded at the beginning of vector where
                iaxis_pad_width[1] represents the number of values padded at
                the end of vector.
            iaxis : int
                The axis currently being calculated.
            kwargs : misc
                Any keyword arguments the function requires.
    
        Examples
        --------
        >>> from skimage.util import pad
        >>> a = [1, 2, 3, 4, 5]
        >>> pad(a, (2,3), 'constant', constant_values=(4, 6))
        array([4, 4, 1, 2, 3, 4, 5, 6, 6, 6])
    
        >>> pad(a, (2, 3), 'edge')
        array([1, 1, 1, 2, 3, 4, 5, 5, 5, 5])
    
        >>> pad(a, (2, 3), 'linear_ramp', end_values=(5, -4))
        array([ 5,  3,  1,  2,  3,  4,  5,  2, -1, -4])
    
        >>> pad(a, (2,), 'maximum')
        array([5, 5, 1, 2, 3, 4, 5, 5, 5])
    
        >>> pad(a, (2,), 'mean')
        array([3, 3, 1, 2, 3, 4, 5, 3, 3])
    
        >>> pad(a, (2,), 'median')
        array([3, 3, 1, 2, 3, 4, 5, 3, 3])
    
        >>> a = [[1, 2], [3, 4]]
        >>> pad(a, ((3, 2), (2, 3)), 'minimum')
        array([[1, 1, 1, 2, 1, 1, 1],
               [1, 1, 1, 2, 1, 1, 1],
               [1, 1, 1, 2, 1, 1, 1],
               [1, 1, 1, 2, 1, 1, 1],
               [3, 3, 3, 4, 3, 3, 3],
               [1, 1, 1, 2, 1, 1, 1],
               [1, 1, 1, 2, 1, 1, 1]])
    
        >>> a = [1, 2, 3, 4, 5]
        >>> pad(a, (2, 3), 'reflect')
        array([3, 2, 1, 2, 3, 4, 5, 4, 3, 2])
    
        >>> pad(a, (2, 3), 'reflect', reflect_type='odd')
        array([-1,  0,  1,  2,  3,  4,  5,  6,  7,  8])
    
        >>> pad(a, (2, 3), 'symmetric')
        array([2, 1, 1, 2, 3, 4, 5, 5, 4, 3])
    
        >>> pad(a, (2, 3), 'symmetric', reflect_type='odd')
        array([0, 1, 1, 2, 3, 4, 5, 5, 6, 7])
    
        >>> pad(a, (2, 3), 'wrap')
        array([4, 5, 1, 2, 3, 4, 5, 1, 2, 3])
    
        >>> def padwithtens(vector, pad_width, iaxis, kwargs):
        ...     vector[:pad_width[0]] = 10
        ...     vector[-pad_width[1]:] = 10
        ...     return vector
    
        >>> a = np.arange(6)
        >>> a = a.reshape((2, 3))
    
        >>> pad(a, 2, padwithtens)
        array([[10, 10, 10, 10, 10, 10, 10],
               [10, 10, 10, 10, 10, 10, 10],
               [10, 10,  0,  1,  2, 10, 10],
               [10, 10,  3,  4,  5, 10, 10],
               [10, 10, 10, 10, 10, 10, 10],
               [10, 10, 10, 10, 10, 10, 10]])
    """
    pass

def rgb2grey(rgb): # reliably restored by inspect
    """
    Compute luminance of an RGB image.
    
        Parameters
        ----------
        rgb : array_like
            The image in RGB format, in a 3-D array of shape ``(.., .., 3)``,
            or in RGBA format with shape ``(.., .., 4)``.
    
        Returns
        -------
        out : ndarray
            The luminance image, a 2-D array.
    
        Raises
        ------
        ValueError
            If `rgb2gray` is not a 3-D array of shape ``(.., .., 3)`` or
            ``(.., .., 4)``.
    
        References
        ----------
        .. [1] http://www.poynton.com/PDFs/ColorFAQ.pdf
    
        Notes
        -----
        The weights used in this conversion are calibrated for contemporary
        CRT phosphors::
    
            Y = 0.2125 R + 0.7154 G + 0.0721 B
    
        If there is an alpha channel present, it is ignored.
    
        Examples
        --------
        >>> from skimage.color import rgb2gray
        >>> from skimage import data
        >>> img = data.astronaut()
        >>> img_gray = rgb2gray(img)
    """
    pass

def _corner_fast(*args, **kwargs): # real signature unknown
    pass

def _prepare_grayscale_input_2D(image): # reliably restored by inspect
    # no doc
    pass

# no classes
# variables with complex values

__loader__ = None # (!) real value is ''

__spec__ = None # (!) real value is ''

__test__ = {
    'corner_moravec (line 16)': 'Compute Moravec corner measure response image.\n\n    This is one of the simplest corner detectors and is comparatively fast but\n    has several limitations (e.g. not rotation invariant).\n\n    Parameters\n    ----------\n    image : ndarray\n        Input image.\n    window_size : int, optional (default 1)\n        Window size.\n\n    Returns\n    -------\n    response : ndarray\n        Moravec response image.\n\n    References\n    ----------\n    .. [1] http://kiwi.cs.dal.ca/~dparks/CornerDetection/moravec.htm\n    .. [2] http://en.wikipedia.org/wiki/Corner_detection\n\n    Examples\n    --------\n    >>> from skimage.feature import corner_moravec\n    >>> square = np.zeros([7, 7])\n    >>> square[3, 3] = 1\n    >>> square.astype(int)\n    array([[0, 0, 0, 0, 0, 0, 0],\n           [0, 0, 0, 0, 0, 0, 0],\n           [0, 0, 0, 0, 0, 0, 0],\n           [0, 0, 0, 1, 0, 0, 0],\n           [0, 0, 0, 0, 0, 0, 0],\n           [0, 0, 0, 0, 0, 0, 0],\n           [0, 0, 0, 0, 0, 0, 0]])\n    >>> corner_moravec(square).astype(int)\n    array([[0, 0, 0, 0, 0, 0, 0],\n           [0, 0, 0, 0, 0, 0, 0],\n           [0, 0, 1, 1, 1, 0, 0],\n           [0, 0, 1, 2, 1, 0, 0],\n           [0, 0, 1, 1, 1, 0, 0],\n           [0, 0, 0, 0, 0, 0, 0],\n           [0, 0, 0, 0, 0, 0, 0]])\n    ',
    'corner_orientations (line 178)': 'Compute the orientation of corners.\n\n    The orientation of corners is computed using the first order central moment\n    i.e. the center of mass approach. The corner orientation is the angle of\n    the vector from the corner coordinate to the intensity centroid in the\n    local neighborhood around the corner calculated using first order central\n    moment.\n\n    Parameters\n    ----------\n    image : 2D array\n        Input grayscale image.\n    corners : (N, 2) array\n        Corner coordinates as ``(row, col)``.\n    mask : 2D array\n        Mask defining the local neighborhood of the corner used for the\n        calculation of the central moment.\n\n    Returns\n    -------\n    orientations : (N, 1) array\n        Orientations of corners in the range [-pi, pi].\n\n    References\n    ----------\n    .. [1] Ethan Rublee, Vincent Rabaud, Kurt Konolige and Gary Bradski\n          "ORB : An efficient alternative to SIFT and SURF"\n          http://www.vision.cs.chubu.ac.jp/CV-R/pdf/Rublee_iccv2011.pdf\n    .. [2] Paul L. Rosin, "Measuring Corner Properties"\n          http://users.cs.cf.ac.uk/Paul.Rosin/corner2.pdf\n\n    Examples\n    --------\n    >>> from skimage.morphology import octagon\n    >>> from skimage.feature import (corner_fast, corner_peaks,\n    ...                              corner_orientations)\n    >>> square = np.zeros((12, 12))\n    >>> square[3:9, 3:9] = 1\n    >>> square.astype(int)\n    array([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],\n           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],\n           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],\n           [0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0],\n           [0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0],\n           [0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0],\n           [0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0],\n           [0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0],\n           [0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0],\n           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],\n           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],\n           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])\n    >>> corners = corner_peaks(corner_fast(square, 9), min_distance=1)\n    >>> corners\n    array([[3, 3],\n           [3, 8],\n           [8, 3],\n           [8, 8]])\n    >>> orientations = corner_orientations(square, corners, octagon(3, 2))\n    >>> np.rad2deg(orientations)\n    array([  45.,  135.,  -45., -135.])\n\n    ',
}

