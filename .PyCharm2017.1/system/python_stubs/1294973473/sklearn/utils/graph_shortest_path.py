# encoding: utf-8
# module sklearn.utils.graph_shortest_path
# from C:\Users\austi\Anaconda3\lib\site-packages\sklearn\utils\graph_shortest_path.cp36-win_amd64.pyd
# by generator 1.145
"""
Routines for performing shortest-path graph searches

The main interface is in the function `graph_shortest_path`.  This
calls cython routines that compute the shortest path using either
the Floyd-Warshall algorithm, or Dykstra's algorithm with Fibonacci Heaps.
"""

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import numpy as np # C:\Users\austi\Anaconda3\lib\site-packages\numpy\__init__.py
import numpy as __numpy
import scipy.sparse.compressed as __scipy_sparse_compressed
import scipy.sparse.sputils as __scipy_sparse_sputils


# functions

def graph_shortest_path(*args, **kwargs): # real signature unknown
    """
    Perform a shortest-path graph search on a positive directed or
        undirected graph.
    
        Parameters
        ----------
        dist_matrix : arraylike or sparse matrix, shape = (N,N)
            Array of positive distances.
            If vertex i is connected to vertex j, then dist_matrix[i,j] gives
            the distance between the vertices.
            If vertex i is not connected to vertex j, then dist_matrix[i,j] = 0
        directed : boolean
            if True, then find the shortest path on a directed graph: only
            progress from a point to its neighbors, not the other way around.
            if False, then find the shortest path on an undirected graph: the
            algorithm can progress from a point to its neighbors and vice versa.
        method : string ['auto'|'FW'|'D']
            method to use.  Options are
            'auto' : attempt to choose the best method for the current problem
            'FW' : Floyd-Warshall algorithm.  O[N^3]
            'D' : Dijkstra's algorithm with Fibonacci stacks.  O[(k+log(N))N^2]
    
        Returns
        -------
        G : np.ndarray, float, shape = [N,N]
            G[i,j] gives the shortest distance from point i to point j
            along the graph.
    
        Notes
        -----
        As currently implemented, Dijkstra's algorithm does not work for
        graphs with direction-dependent distances when directed == False.
        i.e., if dist_matrix[i,j] and dist_matrix[j,i] are not equal and
        both are nonzero, method='D' will not necessarily yield the correct
        result.
    
        Also, these routines have not been tested for graphs with negative
        distances.  Negative distances can lead to infinite cycles that must
        be handled by specialized algorithms.
    """
    pass

def isspmatrix(x): # reliably restored by inspect
    # no doc
    pass

def isspmatrix_csr(x): # reliably restored by inspect
    # no doc
    pass

# classes

class csr_matrix(__scipy_sparse_compressed._cs_matrix, __scipy_sparse_sputils.IndexMixin):
    """
    Compressed Sparse Row matrix
    
        This can be instantiated in several ways:
            csr_matrix(D)
                with a dense matrix or rank-2 ndarray D
    
            csr_matrix(S)
                with another sparse matrix S (equivalent to S.tocsr())
    
            csr_matrix((M, N), [dtype])
                to construct an empty matrix with shape (M, N)
                dtype is optional, defaulting to dtype='d'.
    
            csr_matrix((data, (row_ind, col_ind)), [shape=(M, N)])
                where ``data``, ``row_ind`` and ``col_ind`` satisfy the
                relationship ``a[row_ind[k], col_ind[k]] = data[k]``.
    
            csr_matrix((data, indices, indptr), [shape=(M, N)])
                is the standard CSR representation where the column indices for
                row i are stored in ``indices[indptr[i]:indptr[i+1]]`` and their
                corresponding values are stored in ``data[indptr[i]:indptr[i+1]]``.
                If the shape parameter is not supplied, the matrix dimensions
                are inferred from the index arrays.
    
        Attributes
        ----------
        dtype : dtype
            Data type of the matrix
        shape : 2-tuple
            Shape of the matrix
        ndim : int
            Number of dimensions (this is always 2)
        nnz
            Number of nonzero elements
        data
            CSR format data array of the matrix
        indices
            CSR format index array of the matrix
        indptr
            CSR format index pointer array of the matrix
        has_sorted_indices
            Whether indices are sorted
    
        Notes
        -----
    
        Sparse matrices can be used in arithmetic operations: they support
        addition, subtraction, multiplication, division, and matrix power.
    
        Advantages of the CSR format
          - efficient arithmetic operations CSR + CSR, CSR * CSR, etc.
          - efficient row slicing
          - fast matrix vector products
    
        Disadvantages of the CSR format
          - slow column slicing operations (consider CSC)
          - changes to the sparsity structure are expensive (consider LIL or DOK)
    
        Examples
        --------
    
        >>> import numpy as np
        >>> from scipy.sparse import csr_matrix
        >>> csr_matrix((3, 4), dtype=np.int8).toarray()
        array([[0, 0, 0, 0],
               [0, 0, 0, 0],
               [0, 0, 0, 0]], dtype=int8)
    
        >>> row = np.array([0, 0, 1, 2, 2, 2])
        >>> col = np.array([0, 2, 2, 0, 1, 2])
        >>> data = np.array([1, 2, 3, 4, 5, 6])
        >>> csr_matrix((data, (row, col)), shape=(3, 3)).toarray()
        array([[1, 0, 2],
               [0, 0, 3],
               [4, 5, 6]])
    
        >>> indptr = np.array([0, 2, 3, 6])
        >>> indices = np.array([0, 2, 2, 0, 1, 2])
        >>> data = np.array([1, 2, 3, 4, 5, 6])
        >>> csr_matrix((data, indices, indptr), shape=(3, 3)).toarray()
        array([[1, 0, 2],
               [0, 0, 3],
               [4, 5, 6]])
    
        As an example of how to construct a CSR matrix incrementally,
        the following snippet builds a term-document matrix from texts:
    
        >>> docs = [["hello", "world", "hello"], ["goodbye", "cruel", "world"]]
        >>> indptr = [0]
        >>> indices = []
        >>> data = []
        >>> vocabulary = {}
        >>> for d in docs:
        ...     for term in d:
        ...         index = vocabulary.setdefault(term, len(vocabulary))
        ...         indices.append(index)
        ...         data.append(1)
        ...     indptr.append(len(indices))
        ...
        >>> csr_matrix((data, indices, indptr), dtype=int).toarray()
        array([[2, 1, 0, 0],
               [0, 1, 1, 1]])
    """
    def getcol(self, i): # reliably restored by inspect
        """
        Returns a copy of column i of the matrix, as a (m x 1)
                CSR matrix (column vector).
        """
        pass

    def getrow(self, i): # reliably restored by inspect
        """
        Returns a copy of row i of the matrix, as a (1 x n)
                CSR matrix (row vector).
        """
        pass

    def tobsr(self, blocksize=None, copy=True): # reliably restored by inspect
        """
        Convert this matrix to Block Sparse Row format.
        
                With copy=False, the data/indices may be shared between this matrix and
                the resultant bsr_matrix.
        
                When blocksize=(R, C) is provided, it will be used for construction of
                the bsr_matrix.
        """
        pass

    def tocsc(self, copy=False): # reliably restored by inspect
        # no doc
        pass

    def tocsr(self, copy=False): # reliably restored by inspect
        """
        Convert this matrix to Compressed Sparse Row format.
        
                With copy=False, the data/indices may be shared between this matrix and
                the resultant csr_matrix.
        """
        pass

    def tolil(self, copy=False): # reliably restored by inspect
        """
        Convert this matrix to LInked List format.
        
                With copy=False, the data/indices may be shared between this matrix and
                the resultant lil_matrix.
        """
        pass

    def transpose(self, axes=None, copy=False): # reliably restored by inspect
        """
        Reverses the dimensions of the sparse matrix.
        
                Parameters
                ----------
                axes : None, optional
                    This argument is in the signature *solely* for NumPy
                    compatibility reasons. Do not pass in anything except
                    for the default value.
                copy : bool, optional
                    Indicates whether or not attributes of `self` should be
                    copied whenever possible. The degree to which attributes
                    are copied varies depending on the type of sparse matrix
                    being used.
        
                Returns
                -------
                p : `self` with the dimensions reversed.
        
                See Also
                --------
                np.matrix.transpose : NumPy's implementation of 'transpose'
                                      for matrices
        """
        pass

    def _get_row_slice(self, i, cslice): # reliably restored by inspect
        """ Returns a copy of row self[i, cslice] """
        pass

    def _get_submatrix(self, row_slice, col_slice): # reliably restored by inspect
        """ Return a submatrix of this matrix (new matrix is created). """
        pass

    def _swap(self, x): # reliably restored by inspect
        """ swap the members of x if this is a column-oriented matrix """
        pass

    def __getitem__(self, key): # reliably restored by inspect
        # no doc
        pass

    def __init__(self, arg1, shape=None, dtype=None, copy=False): # reliably restored by inspect
        # no doc
        pass

    format = 'csr'


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

