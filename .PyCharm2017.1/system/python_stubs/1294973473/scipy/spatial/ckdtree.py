# encoding: utf-8
# module scipy.spatial.ckdtree
# from C:\Users\austi\Anaconda3\lib\site-packages\scipy\spatial\ckdtree.cp36-win_amd64.pyd
# by generator 1.145
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import numpy as np # C:\Users\austi\Anaconda3\lib\site-packages\numpy\__init__.py
import scipy as scipy # C:\Users\austi\Anaconda3\lib\site-packages\scipy\__init__.py
import threading as threading # C:\Users\austi\Anaconda3\lib\threading.py

# functions

def cpu_count(*args, **kwargs): # real signature unknown
    """ Returns the number of CPUs in the system """
    pass

def new_object(*args, **kwargs): # real signature unknown
    pass

# classes

class cKDTree(object):
    """
    cKDTree(data, leafsize=16, compact_nodes=True, copy_data=False,
                balanced_tree=True)
    
        kd-tree for quick nearest-neighbor lookup
    
        This class provides an index into a set of k-dimensional points
        which can be used to rapidly look up the nearest neighbors of any
        point. 
    
        The algorithm used is described in Maneewongvatana and Mount 1999. 
        The general idea is that the kd-tree is a binary trie, each of whose
        nodes represents an axis-aligned hyperrectangle. Each node specifies
        an axis and splits the set of points based on whether their coordinate
        along that axis is greater than or less than a particular value. 
    
        During construction, the axis and splitting point are chosen by the 
        "sliding midpoint" rule, which ensures that the cells do not all
        become long and thin. 
    
        The tree can be queried for the r closest neighbors of any given point 
        (optionally returning only those within some maximum distance of the 
        point). It can also be queried, with a substantial gain in efficiency, 
        for the r approximate closest neighbors.
    
        For large dimensions (20 is already large) do not expect this to run 
        significantly faster than brute force. High-dimensional nearest-neighbor
        queries are a substantial open problem in computer science.
    
        Parameters
        ----------
        data : array_like, shape (n,m)
            The n data points of dimension m to be indexed. This array is 
            not copied unless this is necessary to produce a contiguous 
            array of doubles, and so modifying this data will result in 
            bogus results. The data are also copied if the kd-tree is built
            with copy_data=True.
        leafsize : positive int, optional
            The number of points at which the algorithm switches over to
            brute-force. Default: 16.
        compact_nodes : bool, optional    
            If True, the kd-tree is built to shrink the hyperrectangles to
            the actual data range. This usually gives a more compact tree and 
            faster queries at the expense of longer build time. Default: True.
        copy_data : bool, optional
            If True the data is always copied to protect the kd-tree against 
            data corruption. Default: False.
        balanced_tree : bool, optional    
            If True, the median is used to split the hyperrectangles instead of 
            the midpoint. This usually gives a more compact tree and 
            faster queries at the expense of longer build time. Default: True.
        boxsize : array_like or scalar, optional
            Apply a m-d toroidal topology to the KDTree.. The topology is generated 
            by :math:`x_i + n_i L_i` where :math:`n_i` are integers and :math:`L_i`
            is the boxsize along i-th dimension. The input data shall be wrapped 
            into :math:`[0, L_i)`. A ValueError is raised if any of the data is
            outside of this bound.
    
        See Also
        --------
        KDTree : Implementation of `cKDTree` in pure Python
    """
    def count_neighbors(self, other, r, p=2.): # real signature unknown; restored from __doc__
        """
        count_neighbors(self, other, r, p=2.)
        
                Count how many nearby pairs can be formed.
        
                Count the number of pairs (x1,x2) can be formed, with x1 drawn
                from self and x2 drawn from `other`, and where
                ``distance(x1, x2, p) <= r``.
                This is the "two-point correlation" described in Gray and Moore 2000,
                "N-body problems in statistical learning", and the code here is based
                on their algorithm.
        
                Parameters
                ----------
                other : cKDTree instance
                    The other tree to draw points from.
                r : float or one-dimensional array of floats
                    The radius to produce a count for. Multiple radii are searched with
                    a single tree traversal.
                p : float, optional 
                    1<=p<=infinity, default 2.0
                    Which Minkowski p-norm to use
        
                Returns
                -------
                result : int or 1-D array of ints
                    The number of pairs.
        """
        pass

    def query(self, x, k=1, eps=0, p=2, distance_upper_bound=None, n_jobs=1): # real signature unknown; restored from __doc__
        """
        query(self, x, k=1, eps=0, p=2, distance_upper_bound=np.inf, n_jobs=1)
        
                Query the kd-tree for nearest neighbors
        
                Parameters
                ----------
                x : array_like, last dimension self.m
                    An array of points to query.
                k : list of integer or integer
                    The list of k-th nearest neighbors to return. If k is an 
                    integer it is treated as a list of [1, ... k] (range(1, k+1)).
                    Note that the counting starts from 1.
                eps : non-negative float
                    Return approximate nearest neighbors; the k-th returned value 
                    is guaranteed to be no further than (1+eps) times the 
                    distance to the real k-th nearest neighbor.
                p : float, 1<=p<=infinity
                    Which Minkowski p-norm to use. 
                    1 is the sum-of-absolute-values "Manhattan" distance
                    2 is the usual Euclidean distance
                    infinity is the maximum-coordinate-difference distance
                distance_upper_bound : nonnegative float
                    Return only neighbors within this distance.  This is used to prune
                    tree searches, so if you are doing a series of nearest-neighbor
                    queries, it may help to supply the distance to the nearest neighbor
                    of the most recent point.
                n_jobs : int, optional
                    Number of jobs to schedule for parallel processing. If -1 is given
                    all processors are used. Default: 1.
                                
                Returns
                -------
                d : array of floats
                    The distances to the nearest neighbors. 
                    If x has shape tuple+(self.m,), then d has shape tuple+(len(k),).
                    When k == 1, the last dimension of the output is squeezed.
                    Missing neighbors are indicated with infinite distances.
                i : ndarray of ints
                    The locations of the neighbors in self.data.
                    If `x` has shape tuple+(self.m,), then `i` has shape tuple+(len(k),).
                    When k == 1, the last dimension of the output is squeezed.
                    Missing neighbors are indicated with self.n.
        
                Notes
                -----
                If the KD-Tree is periodic, the position :py:code:`x` is wrapped into the
                box.
                
                When the input k is a list, a query for arange(max(k)) is performed, but
                only columns that store the requested values of k are preserved. This is 
                implemented in a manner that reduces memory usage.
        
                Examples
                --------
                
                >>> tree = cKDTree(data)
        
                To query the nearest neighbours and return squeezed result, use
        
                >>> dd, ii = tree.query(x, k=1)
        
                To query the nearest neighbours and return unsqueezed result, use
        
                >>> dd, ii = tree.query(x, k=[1])
        
                To query the second nearest neighbours and return unsqueezed result, use
        
                >>> dd, ii = tree.query(x, k=[2])
        
                To query the first and second nearest neighbours, use
        
                >>> dd, ii = tree.query(x, k=2)
        
                or, be more specific
        
                >>> dd, ii = tree.query(x, k=[1, 2])
        """
        pass

    def query_ball_point(self, x, r, p=2., eps=0): # real signature unknown; restored from __doc__
        """
        query_ball_point(self, x, r, p=2., eps=0)
                
                Find all points within distance r of point(s) x.
        
                Parameters
                ----------
                x : array_like, shape tuple + (self.m,)
                    The point or points to search for neighbors of.
                r : positive float
                    The radius of points to return.
                p : float, optional
                    Which Minkowski p-norm to use.  Should be in the range [1, inf].
                eps : nonnegative float, optional
                    Approximate search. Branches of the tree are not explored if their
                    nearest points are further than ``r / (1 + eps)``, and branches are
                    added in bulk if their furthest points are nearer than
                    ``r * (1 + eps)``.
                n_jobs : int, optional
                    Number of jobs to schedule for parallel processing. If -1 is given
                    all processors are used. Default: 1.
        
                Returns
                -------
                results : list or array of lists
                    If `x` is a single point, returns a list of the indices of the
                    neighbors of `x`. If `x` is an array of points, returns an object
                    array of shape tuple containing lists of neighbors.
        
                Notes
                -----
                If you have many points whose neighbors you want to find, you may save
                substantial amounts of time by putting them in a cKDTree and using
                query_ball_tree.
        
                Examples
                --------
                >>> from scipy import spatial
                >>> x, y = np.mgrid[0:4, 0:4]
                >>> points = zip(x.ravel(), y.ravel())
                >>> tree = spatial.cKDTree(points)
                >>> tree.query_ball_point([2, 0], 1)
                [4, 8, 9, 12]
        """
        pass

    def query_ball_tree(self, other, r, p=2., eps=0): # real signature unknown; restored from __doc__
        """
        query_ball_tree(self, other, r, p=2., eps=0)
        
                Find all pairs of points whose distance is at most r
        
                Parameters
                ----------
                other : cKDTree instance
                    The tree containing points to search against.
                r : float
                    The maximum distance, has to be positive.
                p : float, optional
                    Which Minkowski norm to use.  `p` has to meet the condition
                    ``1 <= p <= infinity``.
                eps : float, optional
                    Approximate search.  Branches of the tree are not explored
                    if their nearest points are further than ``r/(1+eps)``, and
                    branches are added in bulk if their furthest points are nearer
                    than ``r * (1+eps)``.  `eps` has to be non-negative.
        
                Returns
                -------
                results : list of lists
                    For each element ``self.data[i]`` of this tree, ``results[i]`` is a
                    list of the indices of its neighbors in ``other.data``.
        """
        pass

    def query_pairs(self, r, p=2., eps=0): # real signature unknown; restored from __doc__
        """
        query_pairs(self, r, p=2., eps=0)
        
                Find all pairs of points whose distance is at most r.
        
                Parameters
                ----------
                r : positive float
                    The maximum distance.
                p : float, optional
                    Which Minkowski norm to use.  `p` has to meet the condition
                    ``1 <= p <= infinity``.
                eps : float, optional
                    Approximate search.  Branches of the tree are not explored
                    if their nearest points are further than ``r/(1+eps)``, and
                    branches are added in bulk if their furthest points are nearer
                    than ``r * (1+eps)``.  `eps` has to be non-negative.
                output_type : string, optional
                    Choose the output container, 'set' or 'ndarray'. Default: 'set'
        
                Returns
                -------
                results : set or ndarray
                    Set of pairs ``(i,j)``, with ``i < j``, for which the corresponding
                    positions are close. If output_type is 'ndarray', an ndarry is 
                    returned instead of a set.
        """
        pass

    def sparse_distance_matrix(self, other, max_distance, p=2.): # real signature unknown; restored from __doc__
        """
        sparse_distance_matrix(self, other, max_distance, p=2.)
        
                Compute a sparse distance matrix
        
                Computes a distance matrix between two cKDTrees, leaving as zero
                any distance greater than max_distance.
        
                Parameters
                ----------
                other : cKDTree
        
                max_distance : positive float
                
                p : float, 1<=p<=infinity
                    Which Minkowski p-norm to use. 
                
                output_type : string, optional
                    Which container to use for output data. Options: 'dok_matrix',
                    'coo_matrix', 'dict', or 'ndarray'. Default: 'dok_matrix'.
        
                Returns
                -------
                result : dok_matrix, coo_matrix, dict or ndarray
                    Sparse matrix representing the results in "dictionary of keys" 
                    format. If a dict is returned the keys are (i,j) tuples of indices.
                    If output_type is 'ndarray' a record array with fields 'i', 'j',
                    and 'k' is returned,
        """
        pass

    def __getstate__(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, data, leafsize=16, compact_nodes=True, copy_data=False, balanced_tree=True): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    boxsize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    data = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    indices = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    leafsize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    m = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    maxes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    mins = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    n = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    tree = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __pyx_vtable__ = None # (!) real value is ''


class cKDTreeNode(object):
    """
    class cKDTreeNode
    
        This class exposes a Python view of a node in the cKDTree object.
        
        All attributes are read-only.
        
        Attributes
        ----------
        level : int
            The depth of the node. 0 is the level of the root node.
        split_dim : int
            The dimension along which this node is split. If this value is -1  
            the node is a leafnode in the kd-tree. Leafnodes are not split further
            and scanned by brute force.
        split : float
            The value used to separate split this node. Points with value >= split
            in the split_dim dimension are sorted to the 'greater' subnode 
            whereas those with value < split are sorted to the 'lesser' subnode.
        children : int
            The number of data points sorted to this node.
        data_points : ndarray of float64
            An array with the data points sorted to this node.
        indices : ndarray of intp
            An array with the indices of the data points sorted to this node. The
            indices refer to the position in the data set used to construct the
            kd-tree.
        lesser : cKDTreeNode or None
            Subnode with the 'lesser' data points. This attribute is None for
            leafnodes.
        greater : cKDTreeNode or None
            Subnode with the 'greater' data points. This attribute is None for
            leafnodes.
    """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    children = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    data_points = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    greater = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    indices = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    lesser = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    level = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    split = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    split_dim = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __pyx_vtable__ = None # (!) real value is ''


class coo_entries(object):
    # no doc
    def coo_matrix(self, *args, **kwargs): # real signature unknown
        pass

    def dict(self, *args, **kwargs): # real signature unknown
        pass

    def dok_matrix(self, *args, **kwargs): # real signature unknown
        pass

    def ndarray(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    __array_interface__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class ordered_pairs(object):
    # no doc
    def ndarray(self, *args, **kwargs): # real signature unknown
        pass

    def set(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    __array_interface__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



# variables with complex values

__all__ = [
    'cKDTree',
]

__loader__ = None # (!) real value is ''

__spec__ = None # (!) real value is ''

__test__ = {
    'cKDTree.query (line 582)': '\n        query(self, x, k=1, eps=0, p=2, distance_upper_bound=np.inf, n_jobs=1)\n\n        Query the kd-tree for nearest neighbors\n\n        Parameters\n        ----------\n        x : array_like, last dimension self.m\n            An array of points to query.\n        k : list of integer or integer\n            The list of k-th nearest neighbors to return. If k is an \n            integer it is treated as a list of [1, ... k] (range(1, k+1)).\n            Note that the counting starts from 1.\n        eps : non-negative float\n            Return approximate nearest neighbors; the k-th returned value \n            is guaranteed to be no further than (1+eps) times the \n            distance to the real k-th nearest neighbor.\n        p : float, 1<=p<=infinity\n            Which Minkowski p-norm to use. \n            1 is the sum-of-absolute-values "Manhattan" distance\n            2 is the usual Euclidean distance\n            infinity is the maximum-coordinate-difference distance\n        distance_upper_bound : nonnegative float\n            Return only neighbors within this distance.  This is used to prune\n            tree searches, so if you are doing a series of nearest-neighbor\n            queries, it may help to supply the distance to the nearest neighbor\n            of the most recent point.\n        n_jobs : int, optional\n            Number of jobs to schedule for parallel processing. If -1 is given\n            all processors are used. Default: 1.\n                        \n        Returns\n        -------\n        d : array of floats\n            The distances to the nearest neighbors. \n            If x has shape tuple+(self.m,), then d has shape tuple+(len(k),).\n            When k == 1, the last dimension of the output is squeezed.\n            Missing neighbors are indicated with infinite distances.\n        i : ndarray of ints\n            The locations of the neighbors in self.data.\n            If `x` has shape tuple+(self.m,), then `i` has shape tuple+(len(k),).\n            When k == 1, the last dimension of the output is squeezed.\n            Missing neighbors are indicated with self.n.\n\n        Notes\n        -----\n        If the KD-Tree is periodic, the position :py:code:`x` is wrapped into the\n        box.\n        \n        When the input k is a list, a query for arange(max(k)) is performed, but\n        only columns that store the requested values of k are preserved. This is \n        implemented in a manner that reduces memory usage.\n\n        Examples\n        --------\n        \n        >>> tree = cKDTree(data)\n\n        To query the nearest neighbours and return squeezed result, use\n\n        >>> dd, ii = tree.query(x, k=1)\n\n        To query the nearest neighbours and return unsqueezed result, use\n\n        >>> dd, ii = tree.query(x, k=[1])\n\n        To query the second nearest neighbours and return unsqueezed result, use\n\n        >>> dd, ii = tree.query(x, k=[2])\n\n        To query the first and second nearest neighbours, use\n\n        >>> dd, ii = tree.query(x, k=2)\n\n        or, be more specific\n\n        >>> dd, ii = tree.query(x, k=[1, 2])\n\n\n        ',
    'cKDTree.query_ball_point (line 774)': '\n        query_ball_point(self, x, r, p=2., eps=0)\n        \n        Find all points within distance r of point(s) x.\n\n        Parameters\n        ----------\n        x : array_like, shape tuple + (self.m,)\n            The point or points to search for neighbors of.\n        r : positive float\n            The radius of points to return.\n        p : float, optional\n            Which Minkowski p-norm to use.  Should be in the range [1, inf].\n        eps : nonnegative float, optional\n            Approximate search. Branches of the tree are not explored if their\n            nearest points are further than ``r / (1 + eps)``, and branches are\n            added in bulk if their furthest points are nearer than\n            ``r * (1 + eps)``.\n        n_jobs : int, optional\n            Number of jobs to schedule for parallel processing. If -1 is given\n            all processors are used. Default: 1.\n\n        Returns\n        -------\n        results : list or array of lists\n            If `x` is a single point, returns a list of the indices of the\n            neighbors of `x`. If `x` is an array of points, returns an object\n            array of shape tuple containing lists of neighbors.\n\n        Notes\n        -----\n        If you have many points whose neighbors you want to find, you may save\n        substantial amounts of time by putting them in a cKDTree and using\n        query_ball_tree.\n\n        Examples\n        --------\n        >>> from scipy import spatial\n        >>> x, y = np.mgrid[0:4, 0:4]\n        >>> points = zip(x.ravel(), y.ravel())\n        >>> tree = spatial.cKDTree(points)\n        >>> tree.query_ball_point([2, 0], 1)\n        [4, 8, 9, 12]\n\n        ',
}

