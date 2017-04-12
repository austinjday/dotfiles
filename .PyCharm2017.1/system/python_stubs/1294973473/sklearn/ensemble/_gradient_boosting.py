# encoding: utf-8
# module sklearn.ensemble._gradient_boosting
# from C:\Users\austi\Anaconda3\lib\site-packages\sklearn\ensemble\_gradient_boosting.cp36-win_amd64.pyd
# by generator 1.145
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import numpy as np # C:\Users\austi\Anaconda3\lib\site-packages\numpy\__init__.py
from numpy.core.multiarray import np_zeros

import numpy as __numpy


# functions

def np_ones(shape, dtype=None, order=None): # reliably restored by inspect
    """
    Return a new array of given shape and type, filled with ones.
    
        Parameters
        ----------
        shape : int or sequence of ints
            Shape of the new array, e.g., ``(2, 3)`` or ``2``.
        dtype : data-type, optional
            The desired data-type for the array, e.g., `numpy.int8`.  Default is
            `numpy.float64`.
        order : {'C', 'F'}, optional
            Whether to store multidimensional data in C- or Fortran-contiguous
            (row- or column-wise) order in memory.
    
        Returns
        -------
        out : ndarray
            Array of ones with the given shape, dtype, and order.
    
        See Also
        --------
        zeros, ones_like
    
        Examples
        --------
        >>> np.ones(5)
        array([ 1.,  1.,  1.,  1.,  1.])
    
        >>> np.ones((5,), dtype=np.int)
        array([1, 1, 1, 1, 1])
    
        >>> np.ones((2, 1))
        array([[ 1.],
               [ 1.]])
    
        >>> s = (2,2)
        >>> np.ones(s)
        array([[ 1.,  1.],
               [ 1.,  1.]])
    """
    pass

def predict_stage(*args, **kwargs): # real signature unknown
    """
    Add predictions of ``estimators[stage]`` to ``out``.
    
        Each estimator in the stage is scaled by ``scale`` before
        its prediction is added to ``out``.
    """
    pass

def predict_stages(*args, **kwargs): # real signature unknown
    """
    Add predictions of ``estimators`` to ``out``.
    
        Each estimator is scaled by ``scale`` before its prediction
        is added to ``out``.
    """
    pass

def _partial_dependence_tree(*args, **kwargs): # real signature unknown
    """
    Partial dependence of the response on the ``target_feature`` set.
    
        For each row in ``X`` a tree traversal is performed.
        Each traversal starts from the root with weight 1.0.
    
        At each non-terminal node that splits on a target variable either
        the left child or the right child is visited based on the feature
        value of the current sample and the weight is not modified.
        At each non-terminal node that splits on a complementary feature
        both children are visited and the weight is multiplied by the fraction
        of training samples which went to each child.
    
        At each terminal node the value of the node is multiplied by the
        current weight (weights sum to 1 for all visited terminal nodes).
    
        Parameters
        ----------
        tree : sklearn.tree.Tree
            A regression tree; tree.values.shape[1] == 1
        X : memory view on 2d ndarray
            The grid points on which the partial dependence
            should be evaluated. X.shape[1] == target_feature.shape[0].
        target_feature : memory view on 1d ndarray
            The set of target features for which the partial dependence
            should be evaluated. X.shape[1] == target_feature.shape[0].
        learn_rate : double
            Constant scaling factor for the leaf predictions.
        out : memory view on 1d ndarray
            The value of the partial dependence function on each grid
            point.
    """
    pass

def _random_sample_mask(*args, **kwargs): # real signature unknown
    """
    Create a random sample mask where ``n_total_in_bag`` elements are set.
    
         Parameters
         ----------
         n_total_samples : int
             The length of the resulting mask.
    
         n_total_in_bag : int
             The number of elements in the sample mask which are set to 1.
    
         random_state : np.RandomState
             A numpy ``RandomState`` object.
    
         Returns
         -------
         sample_mask : np.ndarray, shape=[n_total_samples]
             An ndarray where ``n_total_in_bag`` elements are set to ``True``
             the others are ``False``.
    """
    pass

# classes

class np_float32(__numpy.floating):
    """ 32-bit floating-point number. Character code 'f'. C float compatible. """
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


DTYPE = np_float32


class np_bool(int):
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


class np_float64(__numpy.floating, float):
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


# variables with complex values

__loader__ = None # (!) real value is ''

__spec__ = None # (!) real value is ''

__test__ = {}

