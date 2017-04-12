# encoding: utf-8
# module sklearn.cluster._hierarchical
# from C:\Users\austi\Anaconda3\lib\site-packages\sklearn\cluster\_hierarchical.cp36-win_amd64.pyd
# by generator 1.145
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import numpy as np # C:\Users\austi\Anaconda3\lib\site-packages\numpy\__init__.py
import numpy as __numpy


# functions

def average_merge(*args, **kwargs): # real signature unknown
    """
    Merge two IntFloatDicts with the average strategy: when the 
        same key is present in the two dicts, the weighted average of the two 
        values is used.
    
        Parameters
        ==========
        a, b : IntFloatDict object
            The IntFloatDicts to merge
        mask : ndarray array of dtype integer and of dimension 1
            a mask for keys to ignore: if not mask[key] the corresponding key
            is skipped in the output dictionnary
        n_a, n_b : float
            n_a and n_b are weights for a and b for the merge strategy.
            They are used for a weighted mean.
    
        Returns
        =======
        out : IntFloatDict object
            The IntFloatDict resulting from the merge
    """
    pass

def compute_ward_dist(*args, **kwargs): # real signature unknown
    pass

def hc_get_heads(*args, **kwargs): # real signature unknown
    """
    Returns the heads of the forest, as defined by parents.
    
        Parameters
        ----------
        parents : array of integers
            The parent structure defining the forest (ensemble of trees)
        copy : boolean
            If copy is False, the input 'parents' array is modified inplace
    
        Returns
        -------
        heads : array of integers of same shape as parents
            The indices in the 'parents' of the tree heads
    """
    pass

def max_merge(*args, **kwargs): # real signature unknown
    """
    Merge two IntFloatDicts with the max strategy: when the same key is
        present in the two dicts, the max of the two values is used.
    
        Parameters
        ==========
        a, b : IntFloatDict object
            The IntFloatDicts to merge
        mask : ndarray array of dtype integer and of dimension 1
            a mask for keys to ignore: if not mask[key] the corresponding key
            is skipped in the output dictionnary
        n_a, n_b : float
            n_a and n_b are weights for a and b for the merge strategy.
            They are not used in the case of a max merge.
    
        Returns
        =======
        out : IntFloatDict object
            The IntFloatDict resulting from the merge
    """
    pass

def _get_parents(*args, **kwargs): # real signature unknown
    """
    Returns the heads of the given nodes, as defined by parents.
    
        Modifies 'heads' and 'not_visited' in-place.
    
        Parameters
        ----------
        nodes : list of integers
            The nodes to start from
        heads : list of integers
            A list to hold the results (modified inplace)
        parents : array of integers
            The parent structure defining the tree
        not_visited
            The tree nodes to consider (modified inplace)
    """
    pass

def _hc_get_descendent(*args, **kwargs): # real signature unknown
    """
    Function returning all the descendent leaves of a set of nodes in the tree.
    
        Parameters
        ----------
        node : integer
            The node for which we want the descendents.
    
        children : list of pairs, length n_nodes
            The children of each non-leaf node. Values less than `n_samples` refer
            to leaves of the tree. A greater value `i` indicates a node with
            children `children[i - n_samples]`.
    
        n_leaves : integer
            Number of leaves.
    
        Returns
        -------
        descendent : list of int
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


class WeightedEdge(object):
    # no doc
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

    a = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    b = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    weight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __hash__ = None


# variables with complex values

__loader__ = None # (!) real value is ''

__spec__ = None # (!) real value is ''

__test__ = {}

