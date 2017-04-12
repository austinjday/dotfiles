# encoding: utf-8
# module sklearn.cluster._k_means_elkan
# from C:\Users\austi\Anaconda3\lib\site-packages\sklearn\cluster\_k_means_elkan.cp36-win_amd64.pyd
# by generator 1.145
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import numpy as np # C:\Users\austi\Anaconda3\lib\site-packages\numpy\__init__.py

# functions

def euclidean_distances(X, Y=None, Y_norm_squared=None, squared=False, X_norm_squared=None): # reliably restored by inspect
    """
    Considering the rows of X (and Y=X) as vectors, compute the
        distance matrix between each pair of vectors.
    
        For efficiency reasons, the euclidean distance between a pair of row
        vector x and y is computed as::
    
            dist(x, y) = sqrt(dot(x, x) - 2 * dot(x, y) + dot(y, y))
    
        This formulation has two advantages over other ways of computing distances.
        First, it is computationally efficient when dealing with sparse data.
        Second, if one argument varies but the other remains unchanged, then
        `dot(x, x)` and/or `dot(y, y)` can be pre-computed.
    
        However, this is not the most precise way of doing this computation, and
        the distance matrix returned by this function may not be exactly
        symmetric as required by, e.g., ``scipy.spatial.distance`` functions.
    
        Read more in the :ref:`User Guide <metrics>`.
    
        Parameters
        ----------
        X : {array-like, sparse matrix}, shape (n_samples_1, n_features)
    
        Y : {array-like, sparse matrix}, shape (n_samples_2, n_features)
    
        Y_norm_squared : array-like, shape (n_samples_2, ), optional
            Pre-computed dot-products of vectors in Y (e.g.,
            ``(Y**2).sum(axis=1)``)
    
        squared : boolean, optional
            Return squared Euclidean distances.
    
        X_norm_squared : array-like, shape = [n_samples_1], optional
            Pre-computed dot-products of vectors in X (e.g.,
            ``(X**2).sum(axis=1)``)
    
        Returns
        -------
        distances : {array, sparse matrix}, shape (n_samples_1, n_samples_2)
    
        Examples
        --------
        >>> from sklearn.metrics.pairwise import euclidean_distances
        >>> X = [[0, 1], [1, 1]]
        >>> # distance between rows of X
        >>> euclidean_distances(X, X)
        array([[ 0.,  1.],
               [ 1.,  0.]])
        >>> # get distance to origin
        >>> euclidean_distances(X, [[0, 0]])
        array([[ 1.        ],
               [ 1.41421356]])
    
        See also
        --------
        paired_distances : distances betweens pairs of elements of X and Y.
    """
    pass

def k_means_elkan(*args, **kwargs): # real signature unknown
    """
    Run Elkan's k-means.
    
        Parameters
        ----------
        X_ : nd-array, shape (n_samples, n_features)
    
        n_clusters : int
            Number of clusters to find.
    
        init : nd-array, shape (n_clusters, n_features)
            Initial position of centers.
    
        tol : float, default=1e-4
            The relative increment in cluster means before declaring convergence.
    
        max_iter : int, default=30
        Maximum number of iterations of the k-means algorithm.
    
        verbose : bool, default=False
            Whether to be verbose.
    """
    pass

def partition(a, kth, axis=-1, kind=None, order=None): # reliably restored by inspect
    """
    Return a partitioned copy of an array.
    
        Creates a copy of the array with its elements rearranged in such a way that
        the value of the element in kth position is in the position it would be in
        a sorted array. All elements smaller than the kth element are moved before
        this element and all equal or greater are moved behind it. The ordering of
        the elements in the two partitions is undefined.
    
        .. versionadded:: 1.8.0
    
        Parameters
        ----------
        a : array_like
            Array to be sorted.
        kth : int or sequence of ints
            Element index to partition by. The kth value of the element will be in
            its final sorted position and all smaller elements will be moved before
            it and all equal or greater elements behind it.
            The order all elements in the partitions is undefined.
            If provided with a sequence of kth it will partition all elements
            indexed by kth  of them into their sorted position at once.
        axis : int or None, optional
            Axis along which to sort. If None, the array is flattened before
            sorting. The default is -1, which sorts along the last axis.
        kind : {'introselect'}, optional
            Selection algorithm. Default is 'introselect'.
        order : str or list of str, optional
            When `a` is an array with fields defined, this argument specifies
            which fields to compare first, second, etc.  A single field can
            be specified as a string.  Not all fields need be specified, but
            unspecified fields will still be used, in the order in which they
            come up in the dtype, to break ties.
    
        Returns
        -------
        partitioned_array : ndarray
            Array of the same type and shape as `a`.
    
        See Also
        --------
        ndarray.partition : Method to sort an array in-place.
        argpartition : Indirect partition.
        sort : Full sorting
    
        Notes
        -----
        The various selection algorithms are characterized by their average speed,
        worst case performance, work space size, and whether they are stable. A
        stable sort keeps items with the same key in the same relative order. The
        available algorithms have the following properties:
    
        ================= ======= ============= ============ =======
           kind            speed   worst case    work space  stable
        ================= ======= ============= ============ =======
        'introselect'        1        O(n)           0         no
        ================= ======= ============= ============ =======
    
        All the partition algorithms make temporary copies of the data when
        partitioning along any but the last axis.  Consequently, partitioning
        along the last axis is faster and uses less space than partitioning
        along any other axis.
    
        The sort order for complex numbers is lexicographic. If both the real
        and imaginary parts are non-nan then the order is determined by the
        real parts except when they are equal, in which case the order is
        determined by the imaginary parts.
    
        Examples
        --------
        >>> a = np.array([3, 4, 2, 1])
        >>> np.partition(a, 3)
        array([2, 1, 3, 4])
    
        >>> np.partition(a, (1, 3))
        array([1, 2, 3, 4])
    """
    pass

def _centers_dense(*args, **kwargs): # real signature unknown
    """
    M step of the K-means EM algorithm
    
        Computation of cluster centers / means.
    
        Parameters
        ----------
        X: array-like, shape (n_samples, n_features)
    
        labels: array of integers, shape (n_samples)
            Current label assignment
    
        n_clusters: int
            Number of desired clusters
    
        distances: array-like, shape (n_samples)
            Distance to closest cluster for each sample.
    
        Returns
        -------
        centers: array, shape (n_clusters, n_features)
            The resulting centers
    """
    pass

# no classes
# variables with complex values

__loader__ = None # (!) real value is ''

__spec__ = None # (!) real value is ''

__test__ = {}

