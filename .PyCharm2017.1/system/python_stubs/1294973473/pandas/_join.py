# encoding: utf-8
# module pandas._join
# from C:\Users\austi\Anaconda3\lib\site-packages\pandas\_join.cp36-win_amd64.pyd
# by generator 1.145
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import numpy as np # C:\Users\austi\Anaconda3\lib\site-packages\numpy\__init__.py
from pandas.algos import ensure_platform_int, groupsort_indexer


# functions

def asof_join_double(*args, **kwargs): # real signature unknown
    pass

def asof_join_double_by_int64_t(*args, **kwargs): # real signature unknown
    pass

def asof_join_double_by_object(*args, **kwargs): # real signature unknown
    pass

def asof_join_float(*args, **kwargs): # real signature unknown
    pass

def asof_join_float_by_int64_t(*args, **kwargs): # real signature unknown
    pass

def asof_join_float_by_object(*args, **kwargs): # real signature unknown
    pass

def asof_join_int16_t(*args, **kwargs): # real signature unknown
    pass

def asof_join_int16_t_by_int64_t(*args, **kwargs): # real signature unknown
    pass

def asof_join_int16_t_by_object(*args, **kwargs): # real signature unknown
    pass

def asof_join_int32_t(*args, **kwargs): # real signature unknown
    pass

def asof_join_int32_t_by_int64_t(*args, **kwargs): # real signature unknown
    pass

def asof_join_int32_t_by_object(*args, **kwargs): # real signature unknown
    pass

def asof_join_int64_t(*args, **kwargs): # real signature unknown
    pass

def asof_join_int64_t_by_int64_t(*args, **kwargs): # real signature unknown
    pass

def asof_join_int64_t_by_object(*args, **kwargs): # real signature unknown
    pass

def asof_join_int8_t(*args, **kwargs): # real signature unknown
    pass

def asof_join_int8_t_by_int64_t(*args, **kwargs): # real signature unknown
    pass

def asof_join_int8_t_by_object(*args, **kwargs): # real signature unknown
    pass

def asof_join_uint16_t(*args, **kwargs): # real signature unknown
    pass

def asof_join_uint16_t_by_int64_t(*args, **kwargs): # real signature unknown
    pass

def asof_join_uint16_t_by_object(*args, **kwargs): # real signature unknown
    pass

def asof_join_uint32_t(*args, **kwargs): # real signature unknown
    pass

def asof_join_uint32_t_by_int64_t(*args, **kwargs): # real signature unknown
    pass

def asof_join_uint32_t_by_object(*args, **kwargs): # real signature unknown
    pass

def asof_join_uint64_t(*args, **kwargs): # real signature unknown
    pass

def asof_join_uint64_t_by_int64_t(*args, **kwargs): # real signature unknown
    pass

def asof_join_uint64_t_by_object(*args, **kwargs): # real signature unknown
    pass

def asof_join_uint8_t(*args, **kwargs): # real signature unknown
    pass

def asof_join_uint8_t_by_int64_t(*args, **kwargs): # real signature unknown
    pass

def asof_join_uint8_t_by_object(*args, **kwargs): # real signature unknown
    pass

def ffill_by_group(*args, **kwargs): # real signature unknown
    pass

def ffill_indexer(*args, **kwargs): # real signature unknown
    pass

def full_outer_join(*args, **kwargs): # real signature unknown
    pass

def inner_join(*args, **kwargs): # real signature unknown
    pass

def inner_join_indexer_float32(*args, **kwargs): # real signature unknown
    """ Two-pass algorithm for monotonic indexes. Handles many-to-one merges """
    pass

def inner_join_indexer_float64(*args, **kwargs): # real signature unknown
    """ Two-pass algorithm for monotonic indexes. Handles many-to-one merges """
    pass

def inner_join_indexer_int32(*args, **kwargs): # real signature unknown
    """ Two-pass algorithm for monotonic indexes. Handles many-to-one merges """
    pass

def inner_join_indexer_int64(*args, **kwargs): # real signature unknown
    """ Two-pass algorithm for monotonic indexes. Handles many-to-one merges """
    pass

def inner_join_indexer_object(*args, **kwargs): # real signature unknown
    """ Two-pass algorithm for monotonic indexes. Handles many-to-one merges """
    pass

def left_join_indexer_float32(*args, **kwargs): # real signature unknown
    """ Two-pass algorithm for monotonic indexes. Handles many-to-one merges """
    pass

def left_join_indexer_float64(*args, **kwargs): # real signature unknown
    """ Two-pass algorithm for monotonic indexes. Handles many-to-one merges """
    pass

def left_join_indexer_int32(*args, **kwargs): # real signature unknown
    """ Two-pass algorithm for monotonic indexes. Handles many-to-one merges """
    pass

def left_join_indexer_int64(*args, **kwargs): # real signature unknown
    """ Two-pass algorithm for monotonic indexes. Handles many-to-one merges """
    pass

def left_join_indexer_object(*args, **kwargs): # real signature unknown
    """ Two-pass algorithm for monotonic indexes. Handles many-to-one merges """
    pass

def left_join_indexer_unique_float32(*args, **kwargs): # real signature unknown
    pass

def left_join_indexer_unique_float64(*args, **kwargs): # real signature unknown
    pass

def left_join_indexer_unique_int32(*args, **kwargs): # real signature unknown
    pass

def left_join_indexer_unique_int64(*args, **kwargs): # real signature unknown
    pass

def left_join_indexer_unique_object(*args, **kwargs): # real signature unknown
    pass

def left_outer_join(*args, **kwargs): # real signature unknown
    pass

def outer_join_indexer_float32(*args, **kwargs): # real signature unknown
    pass

def outer_join_indexer_float64(*args, **kwargs): # real signature unknown
    pass

def outer_join_indexer_int32(*args, **kwargs): # real signature unknown
    pass

def outer_join_indexer_int64(*args, **kwargs): # real signature unknown
    pass

def outer_join_indexer_object(*args, **kwargs): # real signature unknown
    pass

def take_nd(arr, indexer, axis=0, out=None, fill_value=nan, mask_info=None, allow_fill=True): # reliably restored by inspect
    """
    Specialized Cython take which sets NaN values in one pass
    
        Parameters
        ----------
        arr : ndarray
            Input array
        indexer : ndarray
            1-D array of indices to take, subarrays corresponding to -1 value
            indicies are filed with fill_value
        axis : int, default 0
            Axis to take from
        out : ndarray or None, default None
            Optional output array, must be appropriate type to hold input and
            fill_value together, if indexer has any -1 value entries; call
            _maybe_promote to determine this type for any fill_value
        fill_value : any, default np.nan
            Fill value to replace -1 values with
        mask_info : tuple of (ndarray, boolean)
            If provided, value should correspond to:
                (indexer != -1, (indexer != -1).any())
            If not provided, it will be computed internally if necessary
        allow_fill : boolean, default True
            If False, indexer is assumed to contain no -1 values so no filling
            will be done.  This short-circuits computation of a mask.  Result is
            undefined if allow_fill == False and -1 is present in indexer.
    """
    pass

def _get_result_indexer(*args, **kwargs): # real signature unknown
    pass

# no classes
# variables with complex values

float16 = None # (!) real value is ''

float32 = None # (!) real value is ''

float64 = None # (!) real value is ''

int16 = None # (!) real value is ''

int32 = None # (!) real value is ''

int64 = None # (!) real value is ''

int8 = None # (!) real value is ''

__loader__ = None # (!) real value is ''

__spec__ = None # (!) real value is ''

__test__ = {}

