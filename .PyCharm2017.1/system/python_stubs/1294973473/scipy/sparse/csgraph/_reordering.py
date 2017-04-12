# encoding: utf-8
# module scipy.sparse.csgraph._reordering
# from C:\Users\austi\Anaconda3\lib\site-packages\scipy\sparse\csgraph\_reordering.cp36-win_amd64.pyd
# by generator 1.145
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import numpy as np # C:\Users\austi\Anaconda3\lib\site-packages\numpy\__init__.py
import numpy as __numpy


# functions

def isspmatrix_coo(x): # reliably restored by inspect
    # no doc
    pass

def isspmatrix_csc(x): # reliably restored by inspect
    # no doc
    pass

def isspmatrix_csr(x): # reliably restored by inspect
    # no doc
    pass

def maximum_bipartite_matching(*args, **kwargs): # real signature unknown
    """
    Returns an array of row or column permutations that makes
        the diagonal of a nonsingular square CSC sparse matrix zero free.  
        
        Such a permutation is always possible provided that the matrix 
        is nonsingular. This function looks at the structure of the matrix 
        only. The input matrix will be converted to CSC matrix format if
        necessary.
    
        Parameters
        ----------
        graph : sparse matrix
            Input sparse in CSC format
        perm_type : str, {'row', 'column'}
            Type of permutation to generate.
    
        Returns
        -------
        perm : ndarray
            Array of row or column permutations.
    
        Notes
        -----
        This function relies on a maximum cardinality bipartite matching 
        algorithm based on a breadth-first search (BFS) of the underlying 
        graph.
    
        .. versionadded:: 0.15.0
    
        References
        ----------
        I. S. Duff, K. Kaya, and B. Ucar, "Design, Implementation, and 
        Analysis of Maximum Transversal Algorithms", ACM Trans. Math. Softw.
        38, no. 2, (2011).
    """
    pass

def reverse_cuthill_mckee(*args, **kwargs): # real signature unknown
    """
    Returns the permutation array that orders a sparse CSR or CSC matrix
        in Reverse-Cuthill McKee ordering.  
        
        It is assumed by default, ``symmetric_mode=False``, that the input matrix 
        is not symmetric and works on the matrix ``A+A.T``. If you are 
        guaranteed that the matrix is symmetric in structure (values of matrix 
        elements do not matter) then set ``symmetric_mode=True``.
        
        Parameters
        ----------
        graph : sparse matrix
            Input sparse in CSC or CSR sparse matrix format.
        symmetric_mode : bool, optional
            Is input matrix guaranteed to be symmetric.
    
        Returns
        -------
        perm : ndarray
            Array of permuted row and column indices.
     
        Notes
        -----
        .. versionadded:: 0.15.0
    
        References
        ----------
        E. Cuthill and J. McKee, "Reducing the Bandwidth of Sparse Symmetric Matrices",
        ACM '69 Proceedings of the 1969 24th national conference, (1969).
    """
    pass

def _maximum_bipartite_matching(*args, **kwargs): # real signature unknown
    """ Maximum bipartite matching of a graph in CSC format. """
    pass

def _reverse_cuthill_mckee(*args, **kwargs): # real signature unknown
    """
    Reverse Cuthill-McKee ordering of a sparse symmetric CSR or CSC matrix.  
        We follow the original Cuthill-McKee paper and always start the routine
        at a node of lowest degree for each connected component.
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
    """ 32-bit integer. Character code 'i'. C int compatible. """
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

