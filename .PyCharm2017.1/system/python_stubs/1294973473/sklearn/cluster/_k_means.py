# encoding: utf-8
# module sklearn.cluster._k_means
# from C:\Users\austi\Anaconda3\lib\site-packages\sklearn\cluster\_k_means.cp36-win_amd64.pyd
# by generator 1.145
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import numpy as np # C:\Users\austi\Anaconda3\lib\site-packages\numpy\__init__.py
import scipy.sparse as sp # C:\Users\austi\Anaconda3\lib\site-packages\scipy\sparse\__init__.py
from numpy.core.multiarray import bincount

from sklearn.utils.sparsefuncs_fast import assign_rows_csr


# functions

def norm(x): # reliably restored by inspect
    """
    Compute the Euclidean or Frobenius norm of x.
    
        Returns the Euclidean norm when x is a vector, the Frobenius norm when x
        is a matrix (2-d array). More precise than sqrt(squared_norm(x)).
    """
    pass

def _assign_labels_array(*args, **kwargs): # real signature unknown
    """
    Compute label assignment and inertia for a dense array
    
        Return the inertia (sum of squared distances to the centers).
    """
    pass

def _assign_labels_csr(*args, **kwargs): # real signature unknown
    """
    Compute label assignment and inertia for a CSR input
    
        Return the inertia (sum of squared distances to the centers).
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

def _centers_sparse(*args, **kwargs): # real signature unknown
    """
    M step of the K-means EM algorithm
    
        Computation of cluster centers / means.
    
        Parameters
        ----------
        X: scipy.sparse.csr_matrix, shape (n_samples, n_features)
    
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

def _mini_batch_update_csr(*args, **kwargs): # real signature unknown
    """
    Incremental update of the centers for sparse MiniBatchKMeans.
    
        Parameters
        ----------
    
        X: CSR matrix, dtype float
            The complete (pre allocated) training set as a CSR matrix.
    
        centers: array, shape (n_clusters, n_features)
            The cluster centers
    
        counts: array, shape (n_clusters,)
             The vector in which we keep track of the numbers of elements in a
             cluster
    
        Returns
        -------
        inertia: float
            The inertia of the batch prior to centers update, i.e. the sum
            distances to the closest center for each sample. This is the objective
            function being minimized by the k-means algorithm.
    
        squared_diff: float
            The sum of squared update (squared norm of the centers position
            change). If compute_squared_diff is 0, this computation is skipped and
            0.0 is returned instead.
    
        Both squared diff and inertia are commonly used to monitor the convergence
        of the algorithm.
    """
    pass

# no classes
# variables with complex values

__loader__ = None # (!) real value is ''

__spec__ = None # (!) real value is ''

__test__ = {}

