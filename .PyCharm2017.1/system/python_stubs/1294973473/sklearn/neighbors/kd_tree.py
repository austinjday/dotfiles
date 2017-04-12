# encoding: utf-8
# module sklearn.neighbors.kd_tree
# from C:\Users\austi\Anaconda3\lib\site-packages\sklearn\neighbors\kd_tree.cp36-win_amd64.pyd
# by generator 1.145
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import numpy as np # C:\Users\austi\Anaconda3\lib\site-packages\numpy\__init__.py
import warnings as warnings # C:\Users\austi\Anaconda3\lib\warnings.py
from sklearn.neighbors.dist_metrics import get_valid_metric_ids

import numpy as __numpy


# Variables with simple values

CLASS_DOC = "{BinaryTree} for fast generalized N-point problems\n\n{BinaryTree}(X, leaf_size=40, metric='minkowski', \\**kwargs)\n\nParameters\n----------\nX : array-like, shape = [n_samples, n_features]\n    n_samples is the number of points in the data set, and\n    n_features is the dimension of the parameter space.\n    Note: if X is a C-contiguous array of doubles then data will\n    not be copied. Otherwise, an internal copy will be made.\n\nleaf_size : positive integer (default = 40)\n    Number of points at which to switch to brute-force. Changing\n    leaf_size will not affect the results of a query, but can\n    significantly impact the speed of a query and the memory required\n    to store the constructed tree.  The amount of memory needed to\n    store the tree scales as approximately n_samples / leaf_size.\n    For a specified ``leaf_size``, a leaf node is guaranteed to\n    satisfy ``leaf_size <= n_points <= 2 * leaf_size``, except in\n    the case that ``n_samples < leaf_size``.\n\nmetric : string or DistanceMetric object\n    the distance metric to use for the tree.  Default='minkowski'\n    with p=2 (that is, a euclidean metric). See the documentation\n    of the DistanceMetric class for a list of available metrics.\n    {binary_tree}.valid_metrics gives a list of the metrics which\n    are valid for {BinaryTree}.\n\nAdditional keywords are passed to the distance metric class.\n\nAttributes\n----------\ndata : np.ndarray\n    The training data\n\nExamples\n--------\nQuery for k-nearest neighbors\n\n    >>> import numpy as np\n    >>> np.random.seed(0)\n    >>> X = np.random.random((10, 3))  # 10 points in 3 dimensions\n    >>> tree = {BinaryTree}(X, leaf_size=2)              # doctest: +SKIP\n    >>> dist, ind = tree.query([X[0]], k=3)                # doctest: +SKIP\n    >>> print ind  # indices of 3 closest neighbors\n    [0 3 1]\n    >>> print dist  # distances to 3 closest neighbors\n    [ 0.          0.19662693  0.29473397]\n\nPickle and Unpickle a tree.  Note that the state of the tree is saved in the\npickle operation: the tree needs not be rebuilt upon unpickling.\n\n    >>> import numpy as np\n    >>> import pickle\n    >>> np.random.seed(0)\n    >>> X = np.random.random((10, 3))  # 10 points in 3 dimensions\n    >>> tree = {BinaryTree}(X, leaf_size=2)        # doctest: +SKIP\n    >>> s = pickle.dumps(tree)                     # doctest: +SKIP\n    >>> tree_copy = pickle.loads(s)                # doctest: +SKIP\n    >>> dist, ind = tree_copy.query(X[0], k=3)     # doctest: +SKIP\n    >>> print ind  # indices of 3 closest neighbors\n    [0 3 1]\n    >>> print dist  # distances to 3 closest neighbors\n    [ 0.          0.19662693  0.29473397]\n\nQuery for neighbors within a given radius\n\n    >>> import numpy as np\n    >>> np.random.seed(0)\n    >>> X = np.random.random((10, 3))  # 10 points in 3 dimensions\n    >>> tree = {BinaryTree}(X, leaf_size=2)     # doctest: +SKIP\n    >>> print tree.query_radius(X[0], r=0.3, count_only=True)\n    3\n    >>> ind = tree.query_radius(X[0], r=0.3)  # doctest: +SKIP\n    >>> print ind  # indices of neighbors within distance 0.3\n    [3 0 1]\n\n\nCompute a gaussian kernel density estimate:\n\n    >>> import numpy as np\n    >>> np.random.seed(1)\n    >>> X = np.random.random((100, 3))\n    >>> tree = {BinaryTree}(X)                # doctest: +SKIP\n    >>> tree.kernel_density(X[:3], h=0.1, kernel='gaussian')\n    array([ 6.94114649,  7.83281226,  7.2071716 ])\n\nCompute a two-point auto-correlation function\n\n    >>> import numpy as np\n    >>> np.random.seed(0)\n    >>> X = np.random.random((30, 3))\n    >>> r = np.linspace(0, 1, 5)\n    >>> tree = {BinaryTree}(X)                # doctest: +SKIP\n    >>> tree.two_point_correlation(X, r)\n    array([ 30,  62, 278, 580, 820])\n\n"

# functions

def check_array(array, accept_sparse=None, dtype=None, order=None, copy=False, force_all_finite=True, ensure_2d=True, allow_nd=False, ensure_min_samples=1, ensure_min_features=1, warn_on_dtype=False, estimator=None): # reliably restored by inspect
    """
    Input validation on an array, list, sparse matrix or similar.
    
        By default, the input is converted to an at least 2D numpy array.
        If the dtype of the array is object, attempt converting to float,
        raising on failure.
    
        Parameters
        ----------
        array : object
            Input object to check / convert.
    
        accept_sparse : string, list of string or None (default=None)
            String[s] representing allowed sparse matrix formats, such as 'csc',
            'csr', etc.  None means that sparse matrix input will raise an error.
            If the input is sparse but not in the allowed format, it will be
            converted to the first listed format.
    
        dtype : string, type, list of types or None (default="numeric")
            Data type of result. If None, the dtype of the input is preserved.
            If "numeric", dtype is preserved unless array.dtype is object.
            If dtype is a list of types, conversion on the first type is only
            performed if the dtype of the input is not in the list.
    
        order : 'F', 'C' or None (default=None)
            Whether an array will be forced to be fortran or c-style.
            When order is None (default), then if copy=False, nothing is ensured
            about the memory layout of the output array; otherwise (copy=True)
            the memory layout of the returned array is kept as close as possible
            to the original array.
    
        copy : boolean (default=False)
            Whether a forced copy will be triggered. If copy=False, a copy might
            be triggered by a conversion.
    
        force_all_finite : boolean (default=True)
            Whether to raise an error on np.inf and np.nan in X.
    
        ensure_2d : boolean (default=True)
            Whether to make X at least 2d.
    
        allow_nd : boolean (default=False)
            Whether to allow X.ndim > 2.
    
        ensure_min_samples : int (default=1)
            Make sure that the array has a minimum number of samples in its first
            axis (rows for a 2D array). Setting to 0 disables this check.
    
        ensure_min_features : int (default=1)
            Make sure that the 2D array has some minimum number of features
            (columns). The default value of 1 rejects empty datasets.
            This check is only enforced when the input data has effectively 2
            dimensions or is originally 1D and ``ensure_2d`` is True. Setting to 0
            disables this check.
    
        warn_on_dtype : boolean (default=False)
            Raise DataConversionWarning if the dtype of the input data structure
            does not match the requested dtype, causing a memory copy.
    
        estimator : str or estimator instance (default=None)
            If passed, include the name of the estimator in warning messages.
    
        Returns
        -------
        X_converted : object
            The converted and validated X.
    """
    pass

def kernel_norm(*args, **kwargs): # real signature unknown
    """
    Given a string specification of a kernel, compute the normalization.
    
        Parameters
        ----------
        h : float
            the bandwidth of the kernel
        d : int
            the dimension of the space in which the kernel norm is computed
        kernel : string
            The kernel identifier.  Must be one of
            ['gaussian'|'tophat'|'epanechnikov'|
             'exponential'|'linear'|'cosine']
        return_log : boolean
            if True, return the log of the kernel norm.  Otherwise, return the
            kernel norm.
        Returns
        -------
        knorm or log_knorm : float
            the kernel norm or logarithm of the kernel norm.
    """
    pass

def load_heap(*args, **kwargs): # real signature unknown
    """ test fully loading the heap """
    pass

def newObj(*args, **kwargs): # real signature unknown
    pass

def nodeheap_sort(*args, **kwargs): # real signature unknown
    """ In-place reverse sort of vals using NodeHeap """
    pass

def simultaneous_sort(*args, **kwargs): # real signature unknown
    """
    In-place simultaneous sort the given row of the arrays
    
        This python wrapper exists primarily to enable unit testing
        of the _simultaneous_sort C routine.
    """
    pass

# classes

class BinaryTree(object):
    # no doc
    def get_arrays(self, *args, **kwargs): # real signature unknown
        pass

    def get_n_calls(self, *args, **kwargs): # real signature unknown
        pass

    def get_tree_stats(self, *args, **kwargs): # real signature unknown
        pass

    def kernel_density(self, X, h, kernel='gaussian', atol=0, rtol=1, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        kernel_density(self, X, h, kernel='gaussian', atol=0, rtol=1E-8,
                               breadth_first=True, return_log=False)
        
                Compute the kernel density estimate at points X with the given kernel,
                using the distance metric specified at tree creation.
        
                Parameters
                ----------
                X : array_like
                    An array of points to query.  Last dimension should match dimension
                    of training data.
                h : float
                    the bandwidth of the kernel
                kernel : string
                    specify the kernel to use.  Options are
                    - 'gaussian'
                    - 'tophat'
                    - 'epanechnikov'
                    - 'exponential'
                    - 'linear'
                    - 'cosine'
                    Default is kernel = 'gaussian'
                atol, rtol : float (default = 0)
                    Specify the desired relative and absolute tolerance of the result.
                    If the true result is K_true, then the returned result K_ret
                    satisfies ``abs(K_true - K_ret) < atol + rtol * K_ret``
                    The default is zero (i.e. machine precision) for both.
                breadth_first : boolean (default = False)
                    if True, use a breadth-first search.  If False (default) use a
                    depth-first search.  Breadth-first is generally faster for
                    compact kernels and/or high tolerances.
                return_log : boolean (default = False)
                    return the logarithm of the result.  This can be more accurate
                    than returning the result itself for narrow kernels.
        
                Returns
                -------
                density : ndarray
                    The array of (log)-density evaluations, shape = X.shape[:-1]
        
                Examples
                --------
                Compute a gaussian kernel density estimate:
        
                >>> import numpy as np
                >>> np.random.seed(1)
                >>> X = np.random.random((100, 3))
                >>> tree = BinaryTree(X)           # doctest: +SKIP
                >>> tree.kernel_density(X[:3], h=0.1, kernel='gaussian')
                array([ 6.94114649,  7.83281226,  7.2071716 ])
        """
        pass

    def query(self, X, k=1, return_distance=True, dualtree=False, breadth_first=False): # real signature unknown; restored from __doc__
        """
        query(X, k=1, return_distance=True,
                      dualtree=False, breadth_first=False)
        
                query the tree for the k nearest neighbors
        
                Parameters
                ----------
                X : array-like, last dimension self.dim
                    An array of points to query
                k : integer  (default = 1)
                    The number of nearest neighbors to return
                return_distance : boolean (default = True)
                    if True, return a tuple (d, i) of distances and indices
                    if False, return array i
                dualtree : boolean (default = False)
                    if True, use the dual tree formalism for the query: a tree is
                    built for the query points, and the pair of trees is used to
                    efficiently search this space.  This can lead to better
                    performance as the number of points grows large.
                breadth_first : boolean (default = False)
                    if True, then query the nodes in a breadth-first manner.
                    Otherwise, query the nodes in a depth-first manner.
                sort_results : boolean (default = True)
                    if True, then distances and indices of each point are sorted
                    on return, so that the first column contains the closest points.
                    Otherwise, neighbors are returned in an arbitrary order.
        
                Returns
                -------
                i    : if return_distance == False
                (d,i) : if return_distance == True
        
                d : array of doubles - shape: x.shape[:-1] + (k,)
                    each entry gives the list of distances to the
                    neighbors of the corresponding point
        
                i : array of integers - shape: x.shape[:-1] + (k,)
                    each entry gives the list of indices of
                    neighbors of the corresponding point
        
                Examples
                --------
                Query for k-nearest neighbors
        
                    >>> import numpy as np
                    >>> np.random.seed(0)
                    >>> X = np.random.random((10, 3))  # 10 points in 3 dimensions
                    >>> tree = BinaryTree(X, leaf_size=2)    # doctest: +SKIP
                    >>> dist, ind = tree.query(X[0], k=3)    # doctest: +SKIP
                    >>> print ind  # indices of 3 closest neighbors
                    [0 3 1]
                    >>> print dist  # distances to 3 closest neighbors
                    [ 0.          0.19662693  0.29473397]
        """
        pass

    def query_radius(self, X, r, count_only=False): # real signature unknown; restored from __doc__
        """
        query_radius(self, X, r, count_only = False):
        
                query the tree for neighbors within a radius r
        
                Parameters
                ----------
                X : array-like, last dimension self.dim
                    An array of points to query
                r : distance within which neighbors are returned
                    r can be a single value, or an array of values of shape
                    x.shape[:-1] if different radii are desired for each point.
                return_distance : boolean (default = False)
                    if True,  return distances to neighbors of each point
                    if False, return only neighbors
                    Note that unlike the query() method, setting return_distance=True
                    here adds to the computation time.  Not all distances need to be
                    calculated explicitly for return_distance=False.  Results are
                    not sorted by default: see ``sort_results`` keyword.
                count_only : boolean (default = False)
                    if True,  return only the count of points within distance r
                    if False, return the indices of all points within distance r
                    If return_distance==True, setting count_only=True will
                    result in an error.
                sort_results : boolean (default = False)
                    if True, the distances and indices will be sorted before being
                    returned.  If False, the results will not be sorted.  If
                    return_distance == False, setting sort_results = True will
                    result in an error.
        
                Returns
                -------
                count       : if count_only == True
                ind         : if count_only == False and return_distance == False
                (ind, dist) : if count_only == False and return_distance == True
        
                count : array of integers, shape = X.shape[:-1]
                    each entry gives the number of neighbors within
                    a distance r of the corresponding point.
        
                ind : array of objects, shape = X.shape[:-1]
                    each element is a numpy integer array listing the indices of
                    neighbors of the corresponding point.  Note that unlike
                    the results of a k-neighbors query, the returned neighbors
                    are not sorted by distance by default.
        
                dist : array of objects, shape = X.shape[:-1]
                    each element is a numpy double array
                    listing the distances corresponding to indices in i.
        
                Examples
                --------
                Query for neighbors in a given radius
        
                >>> import numpy as np
                >>> np.random.seed(0)
                >>> X = np.random.random((10, 3))  # 10 points in 3 dimensions
                >>> tree = BinaryTree(X, leaf_size=2)     # doctest: +SKIP
                >>> print tree.query_radius(X[0], r=0.3, count_only=True)
                3
                >>> ind = tree.query_radius(X[0], r=0.3)  # doctest: +SKIP
                >>> print ind  # indices of neighbors within distance 0.3
                [3 0 1]
        """
        pass

    def reset_n_calls(self, *args, **kwargs): # real signature unknown
        pass

    def two_point_correlation(self, X, r): # real signature unknown; restored from __doc__
        """
        Compute the two-point correlation function
        
                Parameters
                ----------
                X : array_like
                    An array of points to query.  Last dimension should match dimension
                    of training data.
                r : array_like
                    A one-dimensional array of distances
                dualtree : boolean (default = False)
                    If true, use a dualtree algorithm.  Otherwise, use a single-tree
                    algorithm.  Dual tree algorithms can have better scaling for
                    large N.
        
                Returns
                -------
                counts : ndarray
                    counts[i] contains the number of pairs of points with distance
                    less than or equal to r[i]
        
                Examples
                --------
                Compute the two-point autocorrelation function of X:
        
                >>> import numpy as np
                >>> np.random.seed(0)
                >>> X = np.random.random((30, 3))
                >>> r = np.linspace(0, 1, 5)
                >>> tree = BinaryTree(X)     # doctest: +SKIP
                >>> tree.two_point_correlation(X, r)
                array([ 30,  62, 278, 580, 820])
        """
        pass

    def __getstate__(self, *args, **kwargs): # real signature unknown
        """ get state for pickling """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ reduce method used for pickling """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        """ set state for pickling """
        pass

    data = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    idx_array = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    node_bounds = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    node_data = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    valid_metrics = [
        'euclidean',
        'l2',
        'minkowski',
        'p',
        'manhattan',
        'cityblock',
        'l1',
        'chebyshev',
        'infinity',
    ]
    __pyx_vtable__ = None # (!) real value is ''


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


class KDTree(BinaryTree):
    """
    KDTree for fast generalized N-point problems
    
    KDTree(X, leaf_size=40, metric='minkowski', \**kwargs)
    
    Parameters
    ----------
    X : array-like, shape = [n_samples, n_features]
        n_samples is the number of points in the data set, and
        n_features is the dimension of the parameter space.
        Note: if X is a C-contiguous array of doubles then data will
        not be copied. Otherwise, an internal copy will be made.
    
    leaf_size : positive integer (default = 40)
        Number of points at which to switch to brute-force. Changing
        leaf_size will not affect the results of a query, but can
        significantly impact the speed of a query and the memory required
        to store the constructed tree.  The amount of memory needed to
        store the tree scales as approximately n_samples / leaf_size.
        For a specified ``leaf_size``, a leaf node is guaranteed to
        satisfy ``leaf_size <= n_points <= 2 * leaf_size``, except in
        the case that ``n_samples < leaf_size``.
    
    metric : string or DistanceMetric object
        the distance metric to use for the tree.  Default='minkowski'
        with p=2 (that is, a euclidean metric). See the documentation
        of the DistanceMetric class for a list of available metrics.
        kd_tree.valid_metrics gives a list of the metrics which
        are valid for KDTree.
    
    Additional keywords are passed to the distance metric class.
    
    Attributes
    ----------
    data : np.ndarray
        The training data
    
    Examples
    --------
    Query for k-nearest neighbors
    
        >>> import numpy as np
        >>> np.random.seed(0)
        >>> X = np.random.random((10, 3))  # 10 points in 3 dimensions
        >>> tree = KDTree(X, leaf_size=2)              # doctest: +SKIP
        >>> dist, ind = tree.query([X[0]], k=3)                # doctest: +SKIP
        >>> print ind  # indices of 3 closest neighbors
        [0 3 1]
        >>> print dist  # distances to 3 closest neighbors
        [ 0.          0.19662693  0.29473397]
    
    Pickle and Unpickle a tree.  Note that the state of the tree is saved in the
    pickle operation: the tree needs not be rebuilt upon unpickling.
    
        >>> import numpy as np
        >>> import pickle
        >>> np.random.seed(0)
        >>> X = np.random.random((10, 3))  # 10 points in 3 dimensions
        >>> tree = KDTree(X, leaf_size=2)        # doctest: +SKIP
        >>> s = pickle.dumps(tree)                     # doctest: +SKIP
        >>> tree_copy = pickle.loads(s)                # doctest: +SKIP
        >>> dist, ind = tree_copy.query(X[0], k=3)     # doctest: +SKIP
        >>> print ind  # indices of 3 closest neighbors
        [0 3 1]
        >>> print dist  # distances to 3 closest neighbors
        [ 0.          0.19662693  0.29473397]
    
    Query for neighbors within a given radius
    
        >>> import numpy as np
        >>> np.random.seed(0)
        >>> X = np.random.random((10, 3))  # 10 points in 3 dimensions
        >>> tree = KDTree(X, leaf_size=2)     # doctest: +SKIP
        >>> print tree.query_radius(X[0], r=0.3, count_only=True)
        3
        >>> ind = tree.query_radius(X[0], r=0.3)  # doctest: +SKIP
        >>> print ind  # indices of neighbors within distance 0.3
        [3 0 1]
    
    
    Compute a gaussian kernel density estimate:
    
        >>> import numpy as np
        >>> np.random.seed(1)
        >>> X = np.random.random((100, 3))
        >>> tree = KDTree(X)                # doctest: +SKIP
        >>> tree.kernel_density(X[:3], h=0.1, kernel='gaussian')
        array([ 6.94114649,  7.83281226,  7.2071716 ])
    
    Compute a two-point auto-correlation function
    
        >>> import numpy as np
        >>> np.random.seed(0)
        >>> X = np.random.random((30, 3))
        >>> r = np.linspace(0, 1, 5)
        >>> tree = KDTree(X)                # doctest: +SKIP
        >>> tree.two_point_correlation(X, r)
        array([ 30,  62, 278, 580, 820])
    """
    def __init__(self, X, leaf_size=40, metric='minkowski', *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    __pyx_vtable__ = None # (!) real value is ''


class NeighborsHeap(object):
    """
    A max-heap structure to keep track of distances/indices of neighbors
    
        This implements an efficient pre-allocated set of fixed-size heaps
        for chasing neighbors, holding both an index and a distance.
        When any row of the heap is full, adding an additional point will push
        the furthest point off the heap.
    
        Parameters
        ----------
        n_pts : int
            the number of heaps to use
        n_nbrs : int
            the size of each heap.
    """
    def get_arrays(self, *args, **kwargs): # real signature unknown
        """
        Get the arrays of distances and indices within the heap.
        
                If sort=True, then simultaneously sort the indices and distances,
                so the closer points are listed first.
        """
        pass

    def push(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    __pyx_vtable__ = None # (!) real value is ''


class NodeHeap(object):
    """
    NodeHeap
    
        This is a min-heap implementation for keeping track of nodes
        during a breadth-first search.  Unlike the NeighborsHeap above,
        the NodeHeap does not have a fixed size and must be able to grow
        as elements are added.
    
        Internally, the data is stored in a simple binary heap which meets
        the min heap condition:
    
            heap[i].val < min(heap[2 * i + 1].val, heap[2 * i + 2].val)
    """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    __pyx_vtable__ = None # (!) real value is ''


# variables with complex values

DOC_DICT = {
    'BinaryTree': 'KDTree',
    'binary_tree': 'kd_tree',
}

NodeData = None # (!) real value is ''

NodeHeapData = None # (!) real value is ''

offsets = [
    0,
    8,
    16,
    24,
]

VALID_METRICS = [
    'EuclideanDistance',
    'ManhattanDistance',
    'ChebyshevDistance',
    'MinkowskiDistance',
]

VALID_METRIC_IDS = [
    'euclidean',
    'l2',
    'minkowski',
    'p',
    'manhattan',
    'cityblock',
    'l1',
    'chebyshev',
    'infinity',
]

__all__ = [
    'KDTree',
]

__loader__ = None # (!) real value is ''

__spec__ = None # (!) real value is ''

__test__ = {
    'BinaryTree.kernel_density (line 1504)': "\n        kernel_density(self, X, h, kernel='gaussian', atol=0, rtol=1E-8,\n                       breadth_first=True, return_log=False)\n\n        Compute the kernel density estimate at points X with the given kernel,\n        using the distance metric specified at tree creation.\n\n        Parameters\n        ----------\n        X : array_like\n            An array of points to query.  Last dimension should match dimension\n            of training data.\n        h : float\n            the bandwidth of the kernel\n        kernel : string\n            specify the kernel to use.  Options are\n            - 'gaussian'\n            - 'tophat'\n            - 'epanechnikov'\n            - 'exponential'\n            - 'linear'\n            - 'cosine'\n            Default is kernel = 'gaussian'\n        atol, rtol : float (default = 0)\n            Specify the desired relative and absolute tolerance of the result.\n            If the true result is K_true, then the returned result K_ret\n            satisfies ``abs(K_true - K_ret) < atol + rtol * K_ret``\n            The default is zero (i.e. machine precision) for both.\n        breadth_first : boolean (default = False)\n            if True, use a breadth-first search.  If False (default) use a\n            depth-first search.  Breadth-first is generally faster for\n            compact kernels and/or high tolerances.\n        return_log : boolean (default = False)\n            return the logarithm of the result.  This can be more accurate\n            than returning the result itself for narrow kernels.\n\n        Returns\n        -------\n        density : ndarray\n            The array of (log)-density evaluations, shape = X.shape[:-1]\n\n        Examples\n        --------\n        Compute a gaussian kernel density estimate:\n\n        >>> import numpy as np\n        >>> np.random.seed(1)\n        >>> X = np.random.random((100, 3))\n        >>> tree = BinaryTree(X)           # doctest: +SKIP\n        >>> tree.kernel_density(X[:3], h=0.1, kernel='gaussian')\n        array([ 6.94114649,  7.83281226,  7.2071716 ])\n        ",
    'BinaryTree.query (line 1232)': '\n        query(X, k=1, return_distance=True,\n              dualtree=False, breadth_first=False)\n\n        query the tree for the k nearest neighbors\n\n        Parameters\n        ----------\n        X : array-like, last dimension self.dim\n            An array of points to query\n        k : integer  (default = 1)\n            The number of nearest neighbors to return\n        return_distance : boolean (default = True)\n            if True, return a tuple (d, i) of distances and indices\n            if False, return array i\n        dualtree : boolean (default = False)\n            if True, use the dual tree formalism for the query: a tree is\n            built for the query points, and the pair of trees is used to\n            efficiently search this space.  This can lead to better\n            performance as the number of points grows large.\n        breadth_first : boolean (default = False)\n            if True, then query the nodes in a breadth-first manner.\n            Otherwise, query the nodes in a depth-first manner.\n        sort_results : boolean (default = True)\n            if True, then distances and indices of each point are sorted\n            on return, so that the first column contains the closest points.\n            Otherwise, neighbors are returned in an arbitrary order.\n\n        Returns\n        -------\n        i    : if return_distance == False\n        (d,i) : if return_distance == True\n\n        d : array of doubles - shape: x.shape[:-1] + (k,)\n            each entry gives the list of distances to the\n            neighbors of the corresponding point\n\n        i : array of integers - shape: x.shape[:-1] + (k,)\n            each entry gives the list of indices of\n            neighbors of the corresponding point\n\n        Examples\n        --------\n        Query for k-nearest neighbors\n\n            >>> import numpy as np\n            >>> np.random.seed(0)\n            >>> X = np.random.random((10, 3))  # 10 points in 3 dimensions\n            >>> tree = BinaryTree(X, leaf_size=2)    # doctest: +SKIP\n            >>> dist, ind = tree.query(X[0], k=3)    # doctest: +SKIP\n            >>> print ind  # indices of 3 closest neighbors\n            [0 3 1]\n            >>> print dist  # distances to 3 closest neighbors\n            [ 0.          0.19662693  0.29473397]\n        ',
    'BinaryTree.query_radius (line 1358)': '\n        query_radius(self, X, r, count_only = False):\n\n        query the tree for neighbors within a radius r\n\n        Parameters\n        ----------\n        X : array-like, last dimension self.dim\n            An array of points to query\n        r : distance within which neighbors are returned\n            r can be a single value, or an array of values of shape\n            x.shape[:-1] if different radii are desired for each point.\n        return_distance : boolean (default = False)\n            if True,  return distances to neighbors of each point\n            if False, return only neighbors\n            Note that unlike the query() method, setting return_distance=True\n            here adds to the computation time.  Not all distances need to be\n            calculated explicitly for return_distance=False.  Results are\n            not sorted by default: see ``sort_results`` keyword.\n        count_only : boolean (default = False)\n            if True,  return only the count of points within distance r\n            if False, return the indices of all points within distance r\n            If return_distance==True, setting count_only=True will\n            result in an error.\n        sort_results : boolean (default = False)\n            if True, the distances and indices will be sorted before being\n            returned.  If False, the results will not be sorted.  If\n            return_distance == False, setting sort_results = True will\n            result in an error.\n\n        Returns\n        -------\n        count       : if count_only == True\n        ind         : if count_only == False and return_distance == False\n        (ind, dist) : if count_only == False and return_distance == True\n\n        count : array of integers, shape = X.shape[:-1]\n            each entry gives the number of neighbors within\n            a distance r of the corresponding point.\n\n        ind : array of objects, shape = X.shape[:-1]\n            each element is a numpy integer array listing the indices of\n            neighbors of the corresponding point.  Note that unlike\n            the results of a k-neighbors query, the returned neighbors\n            are not sorted by distance by default.\n\n        dist : array of objects, shape = X.shape[:-1]\n            each element is a numpy double array\n            listing the distances corresponding to indices in i.\n\n        Examples\n        --------\n        Query for neighbors in a given radius\n\n        >>> import numpy as np\n        >>> np.random.seed(0)\n        >>> X = np.random.random((10, 3))  # 10 points in 3 dimensions\n        >>> tree = BinaryTree(X, leaf_size=2)     # doctest: +SKIP\n        >>> print tree.query_radius(X[0], r=0.3, count_only=True)\n        3\n        >>> ind = tree.query_radius(X[0], r=0.3)  # doctest: +SKIP\n        >>> print ind  # indices of neighbors within distance 0.3\n        [3 0 1]\n        ',
    'BinaryTree.two_point_correlation (line 1655)': 'Compute the two-point correlation function\n\n        Parameters\n        ----------\n        X : array_like\n            An array of points to query.  Last dimension should match dimension\n            of training data.\n        r : array_like\n            A one-dimensional array of distances\n        dualtree : boolean (default = False)\n            If true, use a dualtree algorithm.  Otherwise, use a single-tree\n            algorithm.  Dual tree algorithms can have better scaling for\n            large N.\n\n        Returns\n        -------\n        counts : ndarray\n            counts[i] contains the number of pairs of points with distance\n            less than or equal to r[i]\n\n        Examples\n        --------\n        Compute the two-point autocorrelation function of X:\n\n        >>> import numpy as np\n        >>> np.random.seed(0)\n        >>> X = np.random.random((30, 3))\n        >>> r = np.linspace(0, 1, 5)\n        >>> tree = BinaryTree(X)     # doctest: +SKIP\n        >>> tree.two_point_correlation(X, r)\n        array([ 30,  62, 278, 580, 820])\n        ',
}

