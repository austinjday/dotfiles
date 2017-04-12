# encoding: utf-8
# module skimage.draw._draw
# from C:\Users\austi\Anaconda3\lib\site-packages\skimage\draw\_draw.cp36-win_amd64.pyd
# by generator 1.145
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import math as math # <module 'math' (built-in)>
import numpy as np # C:\Users\austi\Anaconda3\lib\site-packages\numpy\__init__.py

# functions

def bezier_curve(*args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    Generate Bezier curve coordinates.
    
        Parameters
        ----------
        y0, x0 : int
            Coordinates of the first control point.
        y1, x1 : int
            Coordinates of the middle control point.
        y2, x2 : int
            Coordinates of the last control point.
        weight : double
            Middle control point weight, it describes the line tension.
        shape : tuple, optional
            Image shape which is used to determine the maximum extent of output
            pixel coordinates. This is useful for curves which exceed the image
            size. By default the full extent of the curve are used.
    
        Returns
        -------
        rr, cc : (N,) ndarray of int
            Indices of pixels that belong to the Bezier curve.
            May be used to directly index into an array, e.g.
            ``img[rr, cc] = 1``.
    
        Notes
        -----
        The algorithm is the rational quadratic algorithm presented in
        reference [1]_.
    
        References
        ----------
        .. [1] A Rasterizing Algorithm for Drawing Curves, A. Zingl, 2012
               http://members.chello.at/easyfilter/Bresenham.pdf
    
        Examples
        --------
        >>> import numpy as np
        >>> from skimage.draw import bezier_curve
        >>> img = np.zeros((10, 10), dtype=np.uint8)
        >>> rr, cc = bezier_curve(1, 5, 5, -2, 8, 8, 2)
        >>> img[rr, cc] = 1
        >>> img
        array([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
               [0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
               [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
               [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 1, 1, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]], dtype=uint8)
    """
    pass

def circle_perimeter(*args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    Generate circle perimeter coordinates.
    
        Parameters
        ----------
        cy, cx : int
            Centre coordinate of circle.
        radius: int
            Radius of circle.
        method : {'bresenham', 'andres'}, optional
            bresenham : Bresenham method (default)
            andres : Andres method
        shape : tuple, optional
            Image shape which is used to determine the maximum extent of output pixel
            coordinates. This is useful for circles which exceed the image size.
            By default the full extent of the circle are used.
    
        Returns
        -------
        rr, cc : (N,) ndarray of int
            Bresenham and Andres' method:
            Indices of pixels that belong to the circle perimeter.
            May be used to directly index into an array, e.g.
            ``img[rr, cc] = 1``.
    
        Notes
        -----
        Andres method presents the advantage that concentric
        circles create a disc whereas Bresenham can make holes. There
        is also less distortions when Andres circles are rotated.
        Bresenham method is also known as midpoint circle algorithm.
        Anti-aliased circle generator is available with `circle_perimeter_aa`.
    
        References
        ----------
        .. [1] J.E. Bresenham, "Algorithm for computer control of a digital
               plotter", IBM Systems journal, 4 (1965) 25-30.
        .. [2] E. Andres, "Discrete circles, rings and spheres", Computers &
               Graphics, 18 (1994) 695-706.
    
        Examples
        --------
        >>> from skimage.draw import circle_perimeter
        >>> img = np.zeros((10, 10), dtype=np.uint8)
        >>> rr, cc = circle_perimeter(4, 4, 3)
        >>> img[rr, cc] = 1
        >>> img
        array([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
               [0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
               [0, 1, 0, 0, 0, 0, 0, 1, 0, 0],
               [0, 1, 0, 0, 0, 0, 0, 1, 0, 0],
               [0, 1, 0, 0, 0, 0, 0, 1, 0, 0],
               [0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
               [0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]], dtype=uint8)
    """
    pass

def circle_perimeter_aa(*args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    Generate anti-aliased circle perimeter coordinates.
    
        Parameters
        ----------
        cy, cx : int
            Centre coordinate of circle.
        radius: int
            Radius of circle.
        shape : tuple, optional
            Image shape which is used to determine the maximum extent of output pixel
            coordinates. This is useful for circles which exceed the image size.
            By default the full extent of the circle are used.
    
        Returns
        -------
        rr, cc, val : (N,) ndarray (int, int, float)
            Indices of pixels (`rr`, `cc`) and intensity values (`val`).
            ``img[rr, cc] = val``.
    
        Notes
        -----
        Wu's method draws anti-aliased circle. This implementation doesn't use
        lookup table optimization.
    
        References
        ----------
        .. [1] X. Wu, "An efficient antialiasing technique", In ACM SIGGRAPH
               Computer Graphics, 25 (1991) 143-152.
    
        Examples
        --------
        >>> from skimage.draw import circle_perimeter_aa
        >>> img = np.zeros((10, 10), dtype=np.uint8)
        >>> rr, cc, val = circle_perimeter_aa(4, 4, 3)
        >>> img[rr, cc] = val * 255
        >>> img
        array([[  0,   0,   0,   0,   0,   0,   0,   0,   0,   0],
               [  0,   0,  60, 211, 255, 211,  60,   0,   0,   0],
               [  0,  60, 194,  43,   0,  43, 194,  60,   0,   0],
               [  0, 211,  43,   0,   0,   0,  43, 211,   0,   0],
               [  0, 255,   0,   0,   0,   0,   0, 255,   0,   0],
               [  0, 211,  43,   0,   0,   0,  43, 211,   0,   0],
               [  0,  60, 194,  43,   0,  43, 194,  60,   0,   0],
               [  0,   0,  60, 211, 255, 211,  60,   0,   0,   0],
               [  0,   0,   0,   0,   0,   0,   0,   0,   0,   0],
               [  0,   0,   0,   0,   0,   0,   0,   0,   0,   0]], dtype=uint8)
    """
    pass

def ellipse_perimeter(*args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    Generate ellipse perimeter coordinates.
    
        Parameters
        ----------
        cy, cx : int
            Centre coordinate of ellipse.
        yradius, xradius : int
            Minor and major semi-axes. ``(x/xradius)**2 + (y/yradius)**2 = 1``.
        orientation : double, optional (default 0)
            Major axis orientation in clockwise direction as radians.
        shape : tuple, optional
            Image shape which is used to determine the maximum extent of output pixel
            coordinates. This is useful for ellipses which exceed the image size.
            By default the full extent of the ellipse are used.
    
        Returns
        -------
        rr, cc : (N,) ndarray of int
            Indices of pixels that belong to the ellipse perimeter.
            May be used to directly index into an array, e.g.
            ``img[rr, cc] = 1``.
    
        References
        ----------
        .. [1] A Rasterizing Algorithm for Drawing Curves, A. Zingl, 2012
               http://members.chello.at/easyfilter/Bresenham.pdf
    
        Examples
        --------
        >>> from skimage.draw import ellipse_perimeter
        >>> img = np.zeros((10, 10), dtype=np.uint8)
        >>> rr, cc = ellipse_perimeter(5, 5, 3, 4)
        >>> img[rr, cc] = 1
        >>> img
        array([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 1, 1, 1, 1, 1, 0, 0],
               [0, 0, 1, 0, 0, 0, 0, 0, 1, 0],
               [0, 1, 0, 0, 0, 0, 0, 0, 0, 1],
               [0, 1, 0, 0, 0, 0, 0, 0, 0, 1],
               [0, 1, 0, 0, 0, 0, 0, 0, 0, 1],
               [0, 0, 1, 0, 0, 0, 0, 0, 1, 0],
               [0, 0, 0, 1, 1, 1, 1, 1, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]], dtype=uint8)
    """
    pass

def line(*args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    Generate line pixel coordinates.
    
        Parameters
        ----------
        y0, x0 : int
            Starting position (row, column).
        y1, x1 : int
            End position (row, column).
    
        Returns
        -------
        rr, cc : (N,) ndarray of int
            Indices of pixels that belong to the line.
            May be used to directly index into an array, e.g.
            ``img[rr, cc] = 1``.
    
        See Also
        --------
        line_aa : Anti-aliased line generator
    
        Examples
        --------
        >>> from skimage.draw import line
        >>> img = np.zeros((10, 10), dtype=np.uint8)
        >>> rr, cc = line(1, 1, 8, 8)
        >>> img[rr, cc] = 1
        >>> img
        array([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]], dtype=uint8)
    """
    pass

def line_aa(*args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    Generate anti-aliased line pixel coordinates.
    
        Parameters
        ----------
        y0, x0 : int
            Starting position (row, column).
        y1, x1 : int
            End position (row, column).
    
        Returns
        -------
        rr, cc, val : (N,) ndarray (int, int, float)
            Indices of pixels (`rr`, `cc`) and intensity values (`val`).
            ``img[rr, cc] = val``.
    
        References
        ----------
        .. [1] A Rasterizing Algorithm for Drawing Curves, A. Zingl, 2012
               http://members.chello.at/easyfilter/Bresenham.pdf
    
        Examples
        --------
        >>> from skimage.draw import line_aa
        >>> img = np.zeros((10, 10), dtype=np.uint8)
        >>> rr, cc, val = line_aa(1, 1, 8, 8)
        >>> img[rr, cc] = val * 255
        >>> img
        array([[  0,   0,   0,   0,   0,   0,   0,   0,   0,   0],
               [  0, 255,  56,   0,   0,   0,   0,   0,   0,   0],
               [  0,  56, 255,  56,   0,   0,   0,   0,   0,   0],
               [  0,   0,  56, 255,  56,   0,   0,   0,   0,   0],
               [  0,   0,   0,  56, 255,  56,   0,   0,   0,   0],
               [  0,   0,   0,   0,  56, 255,  56,   0,   0,   0],
               [  0,   0,   0,   0,   0,  56, 255,  56,   0,   0],
               [  0,   0,   0,   0,   0,   0,  56, 255,  56,   0],
               [  0,   0,   0,   0,   0,   0,   0,  56, 255,   0],
               [  0,   0,   0,   0,   0,   0,   0,   0,   0,   0]], dtype=uint8)
    """
    pass

def polygon(y, x): # real signature unknown; restored from __doc__
    """
    Generate coordinates of pixels within polygon.
    
        Parameters
        ----------
        y : (N,) ndarray
            Y-coordinates of vertices of polygon.
        x : (N,) ndarray
            X-coordinates of vertices of polygon.
        shape : tuple, optional
            Image shape which is used to determine the maximum extent of output
            pixel coordinates. This is useful for polygons which exceed the image
            size. By default the full extent of the polygon are used.
    
        Returns
        -------
        rr, cc : ndarray of int
            Pixel coordinates of polygon.
            May be used to directly index into an array, e.g.
            ``img[rr, cc] = 1``.
    
        Examples
        --------
        >>> from skimage.draw import polygon
        >>> img = np.zeros((10, 10), dtype=np.uint8)
        >>> x = np.array([1, 7, 4, 1])
        >>> y = np.array([1, 2, 8, 1])
        >>> rr, cc = polygon(y, x)
        >>> img[rr, cc] = 1
        >>> img
        array([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 1, 1, 1, 1, 1, 0, 0, 0],
               [0, 0, 1, 1, 1, 1, 1, 0, 0, 0],
               [0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
               [0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
               [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]], dtype=uint8)
    """
    pass

def _bezier_segment(*args, **kwargs): # real signature unknown
    """
    Generate Bezier segment coordinates.
    
        Parameters
        ----------
        y0, x0 : int
            Coordinates of the first control point.
        y1, x1 : int
            Coordinates of the middle control point.
        y2, x2 : int
            Coordinates of the last control point.
        weight : double
            Middle control point weight, it describes the line tension.
    
        Returns
        -------
        rr, cc : (N,) ndarray of int
            Indices of pixels that belong to the Bezier curve.
            May be used to directly index into an array, e.g.
            ``img[rr, cc] = 1``.
    
        Notes
        -----
        The algorithm is the rational quadratic algorithm presented in
        reference [1]_.
    
        References
        ----------
        .. [1] A Rasterizing Algorithm for Drawing Curves, A. Zingl, 2012
               http://members.chello.at/easyfilter/Bresenham.pdf
    """
    pass

def _coords_inside_image(*args, **kwargs): # real signature unknown
    """
    Return the coordinates inside an image of a given shape.
    
        Parameters
        ----------
        rr, cc : (N,) ndarray of int
            Indices of pixels.
        shape : tuple
            Image shape which is used to determine the maximum extent of output
            pixel coordinates.
        val : (N, D) ndarray of float, optional
            Values of pixels at coordinates ``[rr, cc]``.
    
        Returns
        -------
        rr, cc : (M,) array of int
            Row and column indices of valid pixels (i.e. those inside `shape`).
        val : (M, D) array of float, optional
            Values at `rr, cc`. Returned only if `val` is given as input.
    """
    pass

# no classes
# variables with complex values

__loader__ = None # (!) real value is ''

__spec__ = None # (!) real value is ''

__test__ = {
    'bezier_curve (line 776)': 'Generate Bezier curve coordinates.\n\n    Parameters\n    ----------\n    y0, x0 : int\n        Coordinates of the first control point.\n    y1, x1 : int\n        Coordinates of the middle control point.\n    y2, x2 : int\n        Coordinates of the last control point.\n    weight : double\n        Middle control point weight, it describes the line tension.\n    shape : tuple, optional\n        Image shape which is used to determine the maximum extent of output\n        pixel coordinates. This is useful for curves which exceed the image\n        size. By default the full extent of the curve are used.\n\n    Returns\n    -------\n    rr, cc : (N,) ndarray of int\n        Indices of pixels that belong to the Bezier curve.\n        May be used to directly index into an array, e.g.\n        ``img[rr, cc] = 1``.\n\n    Notes\n    -----\n    The algorithm is the rational quadratic algorithm presented in\n    reference [1]_.\n\n    References\n    ----------\n    .. [1] A Rasterizing Algorithm for Drawing Curves, A. Zingl, 2012\n           http://members.chello.at/easyfilter/Bresenham.pdf\n\n    Examples\n    --------\n    >>> import numpy as np\n    >>> from skimage.draw import bezier_curve\n    >>> img = np.zeros((10, 10), dtype=np.uint8)\n    >>> rr, cc = bezier_curve(1, 5, 5, -2, 8, 8, 2)\n    >>> img[rr, cc] = 1\n    >>> img\n    array([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],\n           [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],\n           [0, 0, 0, 1, 1, 0, 0, 0, 0, 0],\n           [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],\n           [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],\n           [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],\n           [0, 0, 1, 1, 0, 0, 0, 0, 0, 0],\n           [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],\n           [0, 0, 0, 0, 0, 0, 0, 1, 1, 0],\n           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]], dtype=uint8)\n    ',
    'circle_perimeter (line 308)': 'Generate circle perimeter coordinates.\n\n    Parameters\n    ----------\n    cy, cx : int\n        Centre coordinate of circle.\n    radius: int\n        Radius of circle.\n    method : {\'bresenham\', \'andres\'}, optional\n        bresenham : Bresenham method (default)\n        andres : Andres method\n    shape : tuple, optional\n        Image shape which is used to determine the maximum extent of output pixel\n        coordinates. This is useful for circles which exceed the image size.\n        By default the full extent of the circle are used.\n\n    Returns\n    -------\n    rr, cc : (N,) ndarray of int\n        Bresenham and Andres\' method:\n        Indices of pixels that belong to the circle perimeter.\n        May be used to directly index into an array, e.g.\n        ``img[rr, cc] = 1``.\n\n    Notes\n    -----\n    Andres method presents the advantage that concentric\n    circles create a disc whereas Bresenham can make holes. There\n    is also less distortions when Andres circles are rotated.\n    Bresenham method is also known as midpoint circle algorithm.\n    Anti-aliased circle generator is available with `circle_perimeter_aa`.\n\n    References\n    ----------\n    .. [1] J.E. Bresenham, "Algorithm for computer control of a digital\n           plotter", IBM Systems journal, 4 (1965) 25-30.\n    .. [2] E. Andres, "Discrete circles, rings and spheres", Computers &\n           Graphics, 18 (1994) 695-706.\n\n    Examples\n    --------\n    >>> from skimage.draw import circle_perimeter\n    >>> img = np.zeros((10, 10), dtype=np.uint8)\n    >>> rr, cc = circle_perimeter(4, 4, 3)\n    >>> img[rr, cc] = 1\n    >>> img\n    array([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],\n           [0, 0, 0, 1, 1, 1, 0, 0, 0, 0],\n           [0, 0, 1, 0, 0, 0, 1, 0, 0, 0],\n           [0, 1, 0, 0, 0, 0, 0, 1, 0, 0],\n           [0, 1, 0, 0, 0, 0, 0, 1, 0, 0],\n           [0, 1, 0, 0, 0, 0, 0, 1, 0, 0],\n           [0, 0, 1, 0, 0, 0, 1, 0, 0, 0],\n           [0, 0, 0, 1, 1, 1, 0, 0, 0, 0],\n           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],\n           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]], dtype=uint8)\n\n    ',
    'circle_perimeter_aa (line 419)': 'Generate anti-aliased circle perimeter coordinates.\n\n    Parameters\n    ----------\n    cy, cx : int\n        Centre coordinate of circle.\n    radius: int\n        Radius of circle.\n    shape : tuple, optional\n        Image shape which is used to determine the maximum extent of output pixel\n        coordinates. This is useful for circles which exceed the image size.\n        By default the full extent of the circle are used.\n\n    Returns\n    -------\n    rr, cc, val : (N,) ndarray (int, int, float)\n        Indices of pixels (`rr`, `cc`) and intensity values (`val`).\n        ``img[rr, cc] = val``.\n\n    Notes\n    -----\n    Wu\'s method draws anti-aliased circle. This implementation doesn\'t use\n    lookup table optimization.\n\n    References\n    ----------\n    .. [1] X. Wu, "An efficient antialiasing technique", In ACM SIGGRAPH\n           Computer Graphics, 25 (1991) 143-152.\n\n    Examples\n    --------\n    >>> from skimage.draw import circle_perimeter_aa\n    >>> img = np.zeros((10, 10), dtype=np.uint8)\n    >>> rr, cc, val = circle_perimeter_aa(4, 4, 3)\n    >>> img[rr, cc] = val * 255\n    >>> img\n    array([[  0,   0,   0,   0,   0,   0,   0,   0,   0,   0],\n           [  0,   0,  60, 211, 255, 211,  60,   0,   0,   0],\n           [  0,  60, 194,  43,   0,  43, 194,  60,   0,   0],\n           [  0, 211,  43,   0,   0,   0,  43, 211,   0,   0],\n           [  0, 255,   0,   0,   0,   0,   0, 255,   0,   0],\n           [  0, 211,  43,   0,   0,   0,  43, 211,   0,   0],\n           [  0,  60, 194,  43,   0,  43, 194,  60,   0,   0],\n           [  0,   0,  60, 211, 255, 211,  60,   0,   0,   0],\n           [  0,   0,   0,   0,   0,   0,   0,   0,   0,   0],\n           [  0,   0,   0,   0,   0,   0,   0,   0,   0,   0]], dtype=uint8)\n    ',
    'ellipse_perimeter (line 505)': 'Generate ellipse perimeter coordinates.\n\n    Parameters\n    ----------\n    cy, cx : int\n        Centre coordinate of ellipse.\n    yradius, xradius : int\n        Minor and major semi-axes. ``(x/xradius)**2 + (y/yradius)**2 = 1``.\n    orientation : double, optional (default 0)\n        Major axis orientation in clockwise direction as radians.\n    shape : tuple, optional\n        Image shape which is used to determine the maximum extent of output pixel\n        coordinates. This is useful for ellipses which exceed the image size.\n        By default the full extent of the ellipse are used.\n\n    Returns\n    -------\n    rr, cc : (N,) ndarray of int\n        Indices of pixels that belong to the ellipse perimeter.\n        May be used to directly index into an array, e.g.\n        ``img[rr, cc] = 1``.\n\n    References\n    ----------\n    .. [1] A Rasterizing Algorithm for Drawing Curves, A. Zingl, 2012\n           http://members.chello.at/easyfilter/Bresenham.pdf\n\n    Examples\n    --------\n    >>> from skimage.draw import ellipse_perimeter\n    >>> img = np.zeros((10, 10), dtype=np.uint8)\n    >>> rr, cc = ellipse_perimeter(5, 5, 3, 4)\n    >>> img[rr, cc] = 1\n    >>> img\n    array([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],\n           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],\n           [0, 0, 0, 1, 1, 1, 1, 1, 0, 0],\n           [0, 0, 1, 0, 0, 0, 0, 0, 1, 0],\n           [0, 1, 0, 0, 0, 0, 0, 0, 0, 1],\n           [0, 1, 0, 0, 0, 0, 0, 0, 0, 1],\n           [0, 1, 0, 0, 0, 0, 0, 0, 0, 1],\n           [0, 0, 1, 0, 0, 0, 0, 0, 1, 0],\n           [0, 0, 0, 1, 1, 1, 1, 1, 0, 0],\n           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]], dtype=uint8)\n\n    ',
    'line (line 41)': 'Generate line pixel coordinates.\n\n    Parameters\n    ----------\n    y0, x0 : int\n        Starting position (row, column).\n    y1, x1 : int\n        End position (row, column).\n\n    Returns\n    -------\n    rr, cc : (N,) ndarray of int\n        Indices of pixels that belong to the line.\n        May be used to directly index into an array, e.g.\n        ``img[rr, cc] = 1``.\n\n    See Also\n    --------\n    line_aa : Anti-aliased line generator\n\n    Examples\n    --------\n    >>> from skimage.draw import line\n    >>> img = np.zeros((10, 10), dtype=np.uint8)\n    >>> rr, cc = line(1, 1, 8, 8)\n    >>> img[rr, cc] = 1\n    >>> img\n    array([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],\n           [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],\n           [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],\n           [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],\n           [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],\n           [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],\n           [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],\n           [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],\n           [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],\n           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]], dtype=uint8)\n\n    ',
    'line_aa (line 128)': 'Generate anti-aliased line pixel coordinates.\n\n    Parameters\n    ----------\n    y0, x0 : int\n        Starting position (row, column).\n    y1, x1 : int\n        End position (row, column).\n\n    Returns\n    -------\n    rr, cc, val : (N,) ndarray (int, int, float)\n        Indices of pixels (`rr`, `cc`) and intensity values (`val`).\n        ``img[rr, cc] = val``.\n\n    References\n    ----------\n    .. [1] A Rasterizing Algorithm for Drawing Curves, A. Zingl, 2012\n           http://members.chello.at/easyfilter/Bresenham.pdf\n\n    Examples\n    --------\n    >>> from skimage.draw import line_aa\n    >>> img = np.zeros((10, 10), dtype=np.uint8)\n    >>> rr, cc, val = line_aa(1, 1, 8, 8)\n    >>> img[rr, cc] = val * 255\n    >>> img\n    array([[  0,   0,   0,   0,   0,   0,   0,   0,   0,   0],\n           [  0, 255,  56,   0,   0,   0,   0,   0,   0,   0],\n           [  0,  56, 255,  56,   0,   0,   0,   0,   0,   0],\n           [  0,   0,  56, 255,  56,   0,   0,   0,   0,   0],\n           [  0,   0,   0,  56, 255,  56,   0,   0,   0,   0],\n           [  0,   0,   0,   0,  56, 255,  56,   0,   0,   0],\n           [  0,   0,   0,   0,   0,  56, 255,  56,   0,   0],\n           [  0,   0,   0,   0,   0,   0,  56, 255,  56,   0],\n           [  0,   0,   0,   0,   0,   0,   0,  56, 255,   0],\n           [  0,   0,   0,   0,   0,   0,   0,   0,   0,   0]], dtype=uint8)\n    ',
    'polygon (line 230)': 'Generate coordinates of pixels within polygon.\n\n    Parameters\n    ----------\n    y : (N,) ndarray\n        Y-coordinates of vertices of polygon.\n    x : (N,) ndarray\n        X-coordinates of vertices of polygon.\n    shape : tuple, optional\n        Image shape which is used to determine the maximum extent of output\n        pixel coordinates. This is useful for polygons which exceed the image\n        size. By default the full extent of the polygon are used.\n\n    Returns\n    -------\n    rr, cc : ndarray of int\n        Pixel coordinates of polygon.\n        May be used to directly index into an array, e.g.\n        ``img[rr, cc] = 1``.\n\n    Examples\n    --------\n    >>> from skimage.draw import polygon\n    >>> img = np.zeros((10, 10), dtype=np.uint8)\n    >>> x = np.array([1, 7, 4, 1])\n    >>> y = np.array([1, 2, 8, 1])\n    >>> rr, cc = polygon(y, x)\n    >>> img[rr, cc] = 1\n    >>> img\n    array([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],\n           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],\n           [0, 0, 1, 1, 1, 1, 1, 0, 0, 0],\n           [0, 0, 1, 1, 1, 1, 1, 0, 0, 0],\n           [0, 0, 0, 1, 1, 1, 0, 0, 0, 0],\n           [0, 0, 0, 1, 1, 1, 0, 0, 0, 0],\n           [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],\n           [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],\n           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],\n           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]], dtype=uint8)\n\n    ',
}

