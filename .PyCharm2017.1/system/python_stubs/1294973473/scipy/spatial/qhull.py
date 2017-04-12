# encoding: utf-8
# module scipy.spatial.qhull
# from C:\Users\austi\Anaconda3\lib\site-packages\scipy\spatial\qhull.cp36-win_amd64.pyd
# by generator 1.145
"""
Wrappers for Qhull triangulation, plus some additional N-D geometry utilities

.. versionadded:: 0.9
"""

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import threading as threading # C:\Users\austi\Anaconda3\lib\threading.py
import numpy as np # C:\Users\austi\Anaconda3\lib\site-packages\numpy\__init__.py
import os as os # C:\Users\austi\Anaconda3\lib\os.py
import sys as sys # <module 'sys' (built-in)>
import tempfile as tempfile # C:\Users\austi\Anaconda3\lib\tempfile.py

# functions

def asbytes(s): # reliably restored by inspect
    # no doc
    pass

def tsearch(tri, xi): # real signature unknown; restored from __doc__
    """
    tsearch(tri, xi)
    
        Find simplices containing the given points. This function does the
        same thing as `Delaunay.find_simplex`.
    
        .. versionadded:: 0.9
    
        See Also
        --------
        Delaunay.find_simplex
    """
    pass

def _get_barycentric_transforms(*args, **kwargs): # real signature unknown
    """
    Compute barycentric affine coordinate transformations for given
        simplices.
    
        Returns
        -------
        Tinvs : array, shape (nsimplex, ndim+1, ndim)
            Barycentric transforms for each simplex.
    
            Tinvs[i,:ndim,:ndim] contains inverse of the matrix ``T``,
            and Tinvs[i,ndim,:] contains the vector ``r_n`` (see below).
    
        Notes
        -----
        Barycentric transform from ``x`` to ``c`` is defined by::
    
            T c = x - r_n
    
        where the ``r_1, ..., r_n`` are the vertices of the simplex.
        The matrix ``T`` is defined by the condition::
    
            T e_j = r_j - r_n
    
        where ``e_j`` is the unit axis vector, e.g, ``e_2 = [0,1,0,0,...]``
        This implies that ``T_ij = (r_j - r_n)_i``.
    
        For the barycentric transforms, we need to compute the inverse
        matrix ``T^-1`` and store the vectors ``r_n`` for each vertex.
        These are stacked into the `Tinvs` returned.
    """
    pass

# classes

class _QhullUser(object):
    """ Takes care of basic dealings with the Qhull objects """
    def add_points(self, points, restart=False): # real signature unknown; restored from __doc__
        """
        add_points(points, restart=False)
        
                Process a set of additional new points.
        
                Parameters
                ----------
                points : ndarray
                    New points to add. The dimensionality should match that of the
                    initial points.
                restart : bool, optional
                    Whether to restart processing from scratch, rather than
                    adding points incrementally.
        
                Raises
                ------
                QhullError
                    Raised when Qhull encounters an error condition, such as
                    geometrical degeneracy when options to resolve are not enabled.
        
                See Also
                --------
                close
        
                Notes
                -----
                You need to specify ``incremental=True`` when constructing the
                object to be able to add points incrementally. Incremental addition
                of points is also not possible after `close` has been called.
        """
        pass

    def close(self): # real signature unknown; restored from __doc__
        """
        close()
        
                Finish incremental processing.
        
                Call this to free resources taken up by Qhull, when using the
                incremental mode. After calling this, adding more points is no
                longer possible.
        """
        pass

    def _update(self, *args, **kwargs): # real signature unknown
        pass

    def __del__(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    _qhull = None
    __dict__ = None # (!) real value is ''


class ConvexHull(_QhullUser):
    """
    ConvexHull(points, incremental=False, qhull_options=None)
    
        Convex hulls in N dimensions.
    
        .. versionadded:: 0.12.0
    
        Parameters
        ----------
        points : ndarray of floats, shape (npoints, ndim)
            Coordinates of points to construct a convex hull from
        incremental : bool, optional
            Allow adding new points incrementally. This takes up some additional
            resources.
        qhull_options : str, optional
            Additional options to pass to Qhull. See Qhull manual
            for details. (Default: "Qx" for ndim > 4 and "" otherwise)
            Option "Qt" is always enabled.
    
        Attributes
        ----------
        points : ndarray of double, shape (npoints, ndim)
            Coordinates of input points.
        vertices : ndarray of ints, shape (nvertices,)
            Indices of points forming the vertices of the convex hull.
            For 2-D convex hulls, the vertices are in counterclockwise order.
            For other dimensions, they are in input order.
        simplices : ndarray of ints, shape (nfacet, ndim)
            Indices of points forming the simplical facets of the convex hull.
        neighbors : ndarray of ints, shape (nfacet, ndim)
            Indices of neighbor facets for each facet.
            The kth neighbor is opposite to the kth vertex.
            -1 denotes no neighbor.
        equations : ndarray of double, shape (nfacet, ndim+1)
            [normal, offset] forming the hyperplane equation of the facet
            (see `Qhull documentation <http://www.qhull.org/>`__  for more).
        coplanar : ndarray of int, shape (ncoplanar, 3)
            Indices of coplanar points and the corresponding indices of
            the nearest facets and nearest vertex indices.  Coplanar
            points are input points which were *not* included in the
            triangulation due to numerical precision issues.
    
            If option "Qc" is not specified, this list is not computed.
        area : float
            Area of the convex hull
        volume : float
            Volume of the convex hull
    
        Raises
        ------
        QhullError
            Raised when Qhull encounters an error condition, such as
            geometrical degeneracy when options to resolve are not enabled.
        ValueError
            Raised if an incompatible array is given as input.
    
        Notes
        -----
        The convex hull is computed using the 
        `Qhull library <http://www.qhull.org/>`__.
    
        Examples
        --------
    
        Convex hull of a random set of points:
    
        >>> from scipy.spatial import ConvexHull
        >>> points = np.random.rand(30, 2)   # 30 random points in 2-D
        >>> hull = ConvexHull(points)
    
        Plot it:
    
        >>> import matplotlib.pyplot as plt
        >>> plt.plot(points[:,0], points[:,1], 'o')
        >>> for simplex in hull.simplices:
        ...     plt.plot(points[simplex, 0], points[simplex, 1], 'k-')
    
        We could also have directly used the vertices of the hull, which
        for 2-D are guaranteed to be in counterclockwise order:
    
        >>> plt.plot(points[hull.vertices,0], points[hull.vertices,1], 'r--', lw=2)
        >>> plt.plot(points[hull.vertices[0],0], points[hull.vertices[0],1], 'ro')
        >>> plt.show()
    
        References
        ----------
        .. [Qhull] http://www.qhull.org/
    """
    def _update(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    vertices = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class Delaunay(_QhullUser):
    """
    Delaunay(points, furthest_site=False, incremental=False, qhull_options=None)
    
        Delaunay tesselation in N dimensions.
    
        .. versionadded:: 0.9
    
        Parameters
        ----------
        points : ndarray of floats, shape (npoints, ndim)
            Coordinates of points to triangulate
        furthest_site : bool, optional
            Whether to compute a furthest-site Delaunay triangulation.
            Default: False
    
            .. versionadded:: 0.12.0
        incremental : bool, optional
            Allow adding new points incrementally. This takes up some additional
            resources.
        qhull_options : str, optional
            Additional options to pass to Qhull. See Qhull manual for
            details. Option "Qt" is always enabled.
            Default:"Qbb Qc Qz Qx Q12" for ndim > 4 and "Qbb Qc Qz Q12" otherwise.
            Incremental mode omits "Qz".
    
            .. versionadded:: 0.12.0
    
        Attributes
        ----------
        points : ndarray of double, shape (npoints, ndim)
            Coordinates of input points.
        simplices : ndarray of ints, shape (nsimplex, ndim+1)
            Indices of the points forming the simplices in the triangulation.
            For 2-D, the points are oriented counterclockwise.
        neighbors : ndarray of ints, shape (nsimplex, ndim+1)
            Indices of neighbor simplices for each simplex.
            The kth neighbor is opposite to the kth vertex.
            For simplices at the boundary, -1 denotes no neighbor.
        equations : ndarray of double, shape (nsimplex, ndim+2)
            [normal, offset] forming the hyperplane equation of the facet
            on the paraboloid
            (see `Qhull documentation <http://www.qhull.org/>`__ for more).
        paraboloid_scale, paraboloid_shift : float
            Scale and shift for the extra paraboloid dimension
            (see `Qhull documentation <http://www.qhull.org/>`__ for more).
        transform : ndarray of double, shape (nsimplex, ndim+1, ndim)
            Affine transform from ``x`` to the barycentric coordinates ``c``.
            This is defined by::
    
                T c = x - r
    
            At vertex ``j``, ``c_j = 1`` and the other coordinates zero.
    
            For simplex ``i``, ``transform[i,:ndim,:ndim]`` contains
            inverse of the matrix ``T``, and ``transform[i,ndim,:]``
            contains the vector ``r``.
    
            If the simplex is degenerate or nearly degenerate, its
            barycentric transform contains NaNs.
        vertex_to_simplex : ndarray of int, shape (npoints,)
            Lookup array, from a vertex, to some simplex which it is a part of.
            If qhull option "Qc" was not specified, the list will contain -1
            for points that are not vertices of the tesselation.
        convex_hull : ndarray of int, shape (nfaces, ndim)
            Vertices of facets forming the convex hull of the point set.
            The array contains the indices of the points belonging to
            the (N-1)-dimensional facets that form the convex hull
            of the triangulation.
    
            .. note::
    
               Computing convex hulls via the Delaunay triangulation is
               inefficient and subject to increased numerical instability.
               Use `ConvexHull` instead.
        coplanar : ndarray of int, shape (ncoplanar, 3)
            Indices of coplanar points and the corresponding indices of
            the nearest facet and the nearest vertex.  Coplanar
            points are input points which were *not* included in the
            triangulation due to numerical precision issues.
    
            If option "Qc" is not specified, this list is not computed.
    
            .. versionadded:: 0.12.0
        vertices
            Same as `simplices`, but deprecated.
        vertex_neighbor_vertices : tuple of two ndarrays of int; (indices, indptr)
            Neighboring vertices of vertices. The indices of neighboring
            vertices of vertex `k` are ``indptr[indices[k]:indices[k+1]]``.
    
        Raises
        ------
        QhullError
            Raised when Qhull encounters an error condition, such as
            geometrical degeneracy when options to resolve are not enabled.
        ValueError
            Raised if an incompatible array is given as input.
    
        Notes
        -----
        The tesselation is computed using the Qhull library 
        `Qhull library <http://www.qhull.org/>`__.
    
        .. note::
    
           Unless you pass in the Qhull option "QJ", Qhull does not
           guarantee that each input point appears as a vertex in the
           Delaunay triangulation. Omitted points are listed in the
           `coplanar` attribute.
    
        Examples
        --------
        Triangulation of a set of points:
    
        >>> points = np.array([[0, 0], [0, 1.1], [1, 0], [1, 1]])
        >>> from scipy.spatial import Delaunay
        >>> tri = Delaunay(points)
    
        We can plot it:
    
        >>> import matplotlib.pyplot as plt
        >>> plt.triplot(points[:,0], points[:,1], tri.simplices.copy())
        >>> plt.plot(points[:,0], points[:,1], 'o')
        >>> plt.show()
    
        Point indices and coordinates for the two triangles forming the
        triangulation:
    
        >>> tri.simplices
        array([[2, 3, 0],                 # may vary
               [3, 1, 0]], dtype=int32)
    
        Note that depending on how rounding errors go, the simplices may
        be in a different order than above.
    
        >>> points[tri.simplices]
        array([[[ 1. ,  0. ],            # may vary
                [ 1. ,  1. ],
                [ 0. ,  0. ]],
               [[ 1. ,  1. ],
                [ 0. ,  1.1],
                [ 0. ,  0. ]]])
    
        Triangle 0 is the only neighbor of triangle 1, and it's opposite to
        vertex 1 of triangle 1:
    
        >>> tri.neighbors[1]
        array([-1,  0, -1], dtype=int32)
        >>> points[tri.simplices[1,1]]
        array([ 0. ,  1.1])
    
        We can find out which triangle points are in:
    
        >>> p = np.array([(0.1, 0.2), (1.5, 0.5)])
        >>> tri.find_simplex(p)
        array([ 1, -1], dtype=int32)
    
        We can also compute barycentric coordinates in triangle 1 for
        these points:
    
        >>> b = tri.transform[1,:2].dot(p - tri.transform[1,2])
        >>> np.c_[b, 1 - b.sum(axis=1)]
        array([[ 0.1       ,  0.2       ,  0.7       ],
               [ 1.27272727,  0.27272727, -0.54545455]])
    
        The coordinates for the first point are all positive, meaning it
        is indeed inside the triangle.
    """
    def find_simplex(self, xi, bruteforce=False, tol=None): # real signature unknown; restored from __doc__
        """
        find_simplex(self, xi, bruteforce=False, tol=None)
        
                Find the simplices containing the given points.
        
                Parameters
                ----------
                tri : DelaunayInfo
                    Delaunay triangulation
                xi : ndarray of double, shape (..., ndim)
                    Points to locate
                bruteforce : bool, optional
                    Whether to only perform a brute-force search
                tol : float, optional
                    Tolerance allowed in the inside-triangle check.
                    Default is ``100*eps``.
        
                Returns
                -------
                i : ndarray of int, same shape as `xi`
                    Indices of simplices containing each point.
                    Points outside the triangulation get the value -1.
        
                Notes
                -----
                This uses an algorithm adapted from Qhull's ``qh_findbestfacet``,
                which makes use of the connection between a convex hull and a
                Delaunay triangulation. After finding the simplex closest to
                the point in N+1 dimensions, the algorithm falls back to
                directed search in N dimensions.
        """
        pass

    def lift_points(self, x): # real signature unknown; restored from __doc__
        """
        lift_points(self, x)
        
                Lift points to the Qhull paraboloid.
        """
        pass

    def plane_distance(self, xi): # real signature unknown; restored from __doc__
        """
        plane_distance(self, xi)
        
                Compute hyperplane distances to the point `xi` from all simplices.
        """
        pass

    def _update(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    convex_hull = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Vertices of facets forming the convex hull of the point set.

        :type: ndarray of int, shape (nfaces, ndim)

        The array contains the indices of the points
        belonging to the (N-1)-dimensional facets that form the convex
        hull of the triangulation.

        .. note::

           Computing convex hulls via the Delaunay triangulation is
           inefficient and subject to increased numerical instability.
           Use `ConvexHull` instead.

        """

    transform = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Affine transform from ``x`` to the barycentric coordinates ``c``.

        :type: ndarray of double, shape (nsimplex, ndim+1, ndim)

        This is defined by::

            T c = x - r

        At vertex ``j``, ``c_j = 1`` and the other coordinates zero.

        For simplex ``i``, ``transform[i,:ndim,:ndim]`` contains
        inverse of the matrix ``T``, and ``transform[i,ndim,:]``
        contains the vector ``r``.

        """

    vertex_neighbor_vertices = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Neighboring vertices of vertices.

        Tuple of two ndarrays of int: (indices, indptr). The indices of
        neighboring vertices of vertex `k` are
        ``indptr[indices[k]:indices[k+1]]``.

        """

    vertex_to_simplex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Lookup array, from a vertex, to some simplex which it is a part of.

        :type: ndarray of int, shape (npoints,)
        """



class QhullError(RuntimeError):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class Voronoi(_QhullUser):
    """
    Voronoi(points, furthest_site=False, incremental=False, qhull_options=None)
    
        Voronoi diagrams in N dimensions.
    
        .. versionadded:: 0.12.0
    
        Parameters
        ----------
        points : ndarray of floats, shape (npoints, ndim)
            Coordinates of points to construct a convex hull from
        furthest_site : bool, optional
            Whether to compute a furthest-site Voronoi diagram. Default: False
        incremental : bool, optional
            Allow adding new points incrementally. This takes up some additional
            resources.
        qhull_options : str, optional
            Additional options to pass to Qhull. See Qhull manual
            for details. (Default: "Qbb Qc Qz Qx" for ndim > 4 and
            "Qbb Qc Qz" otherwise. Incremental mode omits "Qz".)
    
        Attributes
        ----------
        points : ndarray of double, shape (npoints, ndim)
            Coordinates of input points.
        vertices : ndarray of double, shape (nvertices, ndim)
            Coordinates of the Voronoi vertices.
        ridge_points : ndarray of ints, shape ``(nridges, 2)``
            Indices of the points between which each Voronoi ridge lies.
        ridge_vertices : list of list of ints, shape ``(nridges, *)``
            Indices of the Voronoi vertices forming each Voronoi ridge.
        regions : list of list of ints, shape ``(nregions, *)``
            Indices of the Voronoi vertices forming each Voronoi region.
            -1 indicates vertex outside the Voronoi diagram.
        point_region : list of ints, shape (npoints)
            Index of the Voronoi region for each input point.
            If qhull option "Qc" was not specified, the list will contain -1
            for points that are not associated with a Voronoi region.
    
        Raises
        ------
        QhullError
            Raised when Qhull encounters an error condition, such as
            geometrical degeneracy when options to resolve are not enabled.
        ValueError
            Raised if an incompatible array is given as input.
    
        Notes
        -----
        The Voronoi diagram is computed using the 
        `Qhull library <http://www.qhull.org/>`__.
    
        Examples
        --------
        Voronoi diagram for a set of point:
    
        >>> points = np.array([[0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2],
        ...                    [2, 0], [2, 1], [2, 2]])
        >>> from scipy.spatial import Voronoi, voronoi_plot_2d
        >>> vor = Voronoi(points)
    
        Plot it:
    
        >>> import matplotlib.pyplot as plt
        >>> voronoi_plot_2d(vor)
        >>> plt.show()
    
        The Voronoi vertices:
    
        >>> vor.vertices
        array([[ 0.5,  0.5],
               [ 1.5,  0.5],
               [ 0.5,  1.5],
               [ 1.5,  1.5]])
    
        There is a single finite Voronoi region, and four finite Voronoi
        ridges:
    
        >>> vor.regions
        [[], [-1, 0], [-1, 1], [1, -1, 0], [3, -1, 2], [-1, 3], [-1, 2], [3, 2, 0, 1], [2, -1, 0], [3, -1, 1]]
        >>> vor.ridge_vertices
        [[-1, 0], [-1, 0], [-1, 1], [-1, 1], [0, 1], [-1, 3], [-1, 2], [2, 3], [-1, 3], [-1, 2], [0, 2], [1, 3]]
    
        The ridges are perpendicular between lines drawn between the following
        input points:
    
        >>> vor.ridge_points
        array([[0, 1],
               [0, 3],
               [6, 3],
               [6, 7],
               [3, 4],
               [5, 8],
               [5, 2],
               [5, 4],
               [8, 7],
               [2, 1],
               [4, 1],
               [4, 7]], dtype=int32)
    """
    def _update(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    ridge_dict = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class _Qhull(object):
    # no doc
    def add_points(self, *args, **kwargs): # real signature unknown
        pass

    def check_active(self, *args, **kwargs): # real signature unknown
        pass

    def close(self, *args, **kwargs): # real signature unknown
        """ Uninitialize this instance """
        pass

    def get_extremes_2d(self, *args, **kwargs): # real signature unknown
        """
        Compute the extremal points in a 2-D convex hull, i.e. the
                vertices of the convex hull, ordered counterclockwise.
        
                See qhull/io.c:qh_printextremes_2d
        """
        pass

    def get_paraboloid_shift_scale(self, *args, **kwargs): # real signature unknown
        pass

    def get_points(self, *args, **kwargs): # real signature unknown
        pass

    def get_simplex_facet_array(self, *args, **kwargs): # real signature unknown
        """
        Return array of simplical facets currently in Qhull.
        
                Returns
                -------
                facets : array of int, shape (nfacets, ndim+1)
                    Indices of coordinates of vertices forming the simplical facets
                neighbors : array of int, shape (nfacets, ndim)
                    Indices of neighboring facets.  The kth neighbor is opposite
                    the kth vertex, and the first neighbor is the horizon facet
                    for the first vertex.
        
                    Facets extending to infinity are denoted with index -1.
                equations : array of double, shape (nfacets, ndim+2)
        """
        pass

    def get_voronoi_diagram(self, *args, **kwargs): # real signature unknown
        """
        Return the voronoi diagram currently in Qhull.
        
                Returns
                -------
                voronoi_vertices : array of double, shape (nvoronoi_vertices, ndim)
                    Coordinates of the Voronoi vertices
        
                ridge_points : array of double, shape (nridges, 2)
                    Voronoi ridges, as indices to the points array.
        
                ridge_vertices : list of lists, shape (nridges, *)
                    Voronoi vertices for each Voronoi ridge, as indices to
                    the Voronoi vertices array.
                    Infinity is indicated by index ``-1``.
        
                regions : list of lists, shape (nregion, *)
                    Voronoi vertices of all regions.
        
                point_region : array of int, shape (npoint,)
                    Index of the Voronoi region for each input point.
        """
        pass

    def triangulate(self, *args, **kwargs): # real signature unknown
        pass

    def volume_area(self, *args, **kwargs): # real signature unknown
        pass

    def __del__(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    furthest_site = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    mode_option = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ndim = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    options = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class _QhullMessageStream(object):
    """
    Qhull emits error messages to FILE* streams, which we should capture.
        Do this by directing them to a temporary file.
    """
    def clear(self, *args, **kwargs): # real signature unknown
        pass

    def close(self, *args, **kwargs): # real signature unknown
        pass

    def get(self, *args, **kwargs): # real signature unknown
        pass

    def __del__(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass


# variables with complex values

__all__ = [
    'Delaunay',
    'ConvexHull',
    'Voronoi',
    'tsearch',
]

__loader__ = None # (!) real value is ''

__pyx_capi__ = {
    '_barycentric_coordinate_single': None, # (!) real value is ''
    '_barycentric_coordinates': None, # (!) real value is ''
    '_barycentric_inside': None, # (!) real value is ''
    '_distplane': None, # (!) real value is ''
    '_find_simplex': None, # (!) real value is ''
    '_find_simplex_bruteforce': None, # (!) real value is ''
    '_find_simplex_directed': None, # (!) real value is ''
    '_get_delaunay_info': None, # (!) real value is ''
    '_is_point_fully_outside': None, # (!) real value is ''
    '_lift_point': None, # (!) real value is ''
}

__spec__ = None # (!) real value is ''

__test__ = {}

