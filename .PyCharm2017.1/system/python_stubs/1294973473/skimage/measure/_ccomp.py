# encoding: utf-8
# module skimage.measure._ccomp
# from C:\Users\austi\Anaconda3\lib\site-packages\skimage\measure\_ccomp.cp36-win_amd64.pyd
# by generator 1.145
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import numpy as np # C:\Users\austi\Anaconda3\lib\site-packages\numpy\__init__.py
import numpy as __numpy


# functions

def label(x, connectivity=1): # real signature unknown; restored from __doc__
    """
    Label connected regions of an integer array.
    
        Two pixels are connected when they are neighbors and have the same value.
        In 2D, they can be neighbors either in a 1- or 2-connected sense.
        The value refers to the maximum number of orthogonal hops to consider a
        pixel/voxel a neighbor::
    
          1-connectivity      2-connectivity     diagonal connection close-up
    
               [ ]           [ ]  [ ]  [ ]         [ ]
                |               \  |  /             |  <- hop 2
          [ ]--[x]--[ ]      [ ]--[x]--[ ]    [x]--[ ]
                |               /  |  \         hop 1
               [ ]           [ ]  [ ]  [ ]
    
        Parameters
        ----------
        input : ndarray of dtype int
            Image to label.
        neighbors : {4, 8}, int, optional
            Whether to use 4- or 8-"connectivity".
            In 3D, 4-"connectivity" means connected pixels have to share face,
            whereas with 8-"connectivity", they have to share only edge or vertex.
            **Deprecated, use ``connectivity`` instead.**
        background : int, optional
            Consider all pixels with this value as background pixels, and label
            them as 0. By default, 0-valued pixels are considered as background
            pixels.
        return_num : bool, optional
            Whether to return the number of assigned labels.
        connectivity : int, optional
            Maximum number of orthogonal hops to consider a pixel/voxel
            as a neighbor.
            Accepted values are ranging from  1 to input.ndim. If ``None``, a full
            connectivity of ``input.ndim`` is used.
    
        Returns
        -------
        labels : ndarray of dtype int
            Labeled array, where all connected regions are assigned the
            same integer value.
        num : int, optional
            Number of labels, which equals the maximum label index and is only
            returned if return_num is `True`.
    
        Examples
        --------
        >>> import numpy as np
        >>> x = np.eye(3).astype(int)
        >>> print(x)
        [[1 0 0]
         [0 1 0]
         [0 0 1]]
        >>> from skimage.measure import label
        >>> print(label(x, connectivity=1))
        [[1 0 0]
         [0 2 0]
         [0 0 3]]
    
        >>> print(label(x, connectivity=2))
        [[1 0 0]
         [0 1 0]
         [0 0 1]]
    
        >>> print(label(x, background=-1))
        [[1 2 2]
         [2 1 2]
         [2 2 1]]
    
        >>> x = np.array([[1, 0, 0],
        ...               [1, 1, 5],
        ...               [0, 0, 0]])
    
        >>> print(label(x))
        [[1 0 0]
         [1 1 2]
         [0 0 0]]
    """
    pass

def reshape_array(*args, **kwargs): # real signature unknown
    """
    "Rotates" the array so it gains a shape that the algorithm can work with.
        An illegal shape is (3, 1, 4), and correct one is (1, 3, 4) or (1, 4, 3).
        The point is to have all 1s of the shape at the beginning, not in the
        middle of the shape tuple.
    
        Note: The greater-than-one shape component should go from greatest to
        lowest numbers since it is more friendly to the CPU cache (so (1, 3, 4) is
        less optimal than (1, 4, 3). Keyword to this is "memory spatial locality"
    
        Args:
            arr (np.ndarray): The array we want to fix
    
        Returns:
            tuple (result, swaps): The result is the "fixed" array and a record
            of what has been done with it.
    """
    pass

def undo_reshape_array(*args, **kwargs): # real signature unknown
    """
    Does the opposite of what :func:`reshape_array` does
    
        Args:
            arr (np.ndarray): The array to "revert"
            swaps (list): The second result of :func:`reshape_array`
    
        Returns:
            np.ndarray: The array of the original shape
    """
    pass

def warn(message, category=None, stacklevel=2): # reliably restored by inspect
    """ A version of `warnings.warn` with a default stacklevel of 2. """
    pass

def _apply_swaps(*args, **kwargs): # real signature unknown
    pass

def _get_swaps(*args, **kwargs): # real signature unknown
    """
    What axes to swap if we want to convert an illegal array shape
        to a legal one.
    
        Args:
            shp (tuple-like): The array shape
    
        Returns:
            list: List of tuples to be passed to np.swapaxes
    """
    pass

def _label(*args, **kwargs): # real signature unknown
    pass

# classes

class DTYPE(__numpy.signedinteger):
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

__pyx_capi__ = {
    'find_root': None, # (!) real value is ''
    'join_trees': None, # (!) real value is ''
    'set_root': None, # (!) real value is ''
}

__spec__ = None # (!) real value is ''

__test__ = {
    'label (line 361)': 'Label connected regions of an integer array.\n\n    Two pixels are connected when they are neighbors and have the same value.\n    In 2D, they can be neighbors either in a 1- or 2-connected sense.\n    The value refers to the maximum number of orthogonal hops to consider a\n    pixel/voxel a neighbor::\n\n      1-connectivity      2-connectivity     diagonal connection close-up\n\n           [ ]           [ ]  [ ]  [ ]         [ ]\n            |               \\  |  /             |  <- hop 2\n      [ ]--[x]--[ ]      [ ]--[x]--[ ]    [x]--[ ]\n            |               /  |  \\         hop 1\n           [ ]           [ ]  [ ]  [ ]\n\n    Parameters\n    ----------\n    input : ndarray of dtype int\n        Image to label.\n    neighbors : {4, 8}, int, optional\n        Whether to use 4- or 8-"connectivity".\n        In 3D, 4-"connectivity" means connected pixels have to share face,\n        whereas with 8-"connectivity", they have to share only edge or vertex.\n        **Deprecated, use ``connectivity`` instead.**\n    background : int, optional\n        Consider all pixels with this value as background pixels, and label\n        them as 0. By default, 0-valued pixels are considered as background\n        pixels.\n    return_num : bool, optional\n        Whether to return the number of assigned labels.\n    connectivity : int, optional\n        Maximum number of orthogonal hops to consider a pixel/voxel\n        as a neighbor.\n        Accepted values are ranging from  1 to input.ndim. If ``None``, a full\n        connectivity of ``input.ndim`` is used.\n\n    Returns\n    -------\n    labels : ndarray of dtype int\n        Labeled array, where all connected regions are assigned the\n        same integer value.\n    num : int, optional\n        Number of labels, which equals the maximum label index and is only\n        returned if return_num is `True`.\n\n    Examples\n    --------\n    >>> import numpy as np\n    >>> x = np.eye(3).astype(int)\n    >>> print(x)\n    [[1 0 0]\n     [0 1 0]\n     [0 0 1]]\n    >>> from skimage.measure import label\n    >>> print(label(x, connectivity=1))\n    [[1 0 0]\n     [0 2 0]\n     [0 0 3]]\n\n    >>> print(label(x, connectivity=2))\n    [[1 0 0]\n     [0 1 0]\n     [0 0 1]]\n\n    >>> print(label(x, background=-1))\n    [[1 2 2]\n     [2 1 2]\n     [2 2 1]]\n\n    >>> x = np.array([[1, 0, 0],\n    ...               [1, 1, 5],\n    ...               [0, 0, 0]])\n\n    >>> print(label(x))\n    [[1 0 0]\n     [1 1 2]\n     [0 0 0]]\n    ',
}

