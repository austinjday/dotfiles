# encoding: utf-8
# module _license
# from C:\Users\austi\Anaconda3\lib\site-packages\_license.cp36-win_amd64.pyd
# by generator 1.145
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import re as re # C:\Users\austi\Anaconda3\lib\re.py
import os as os # C:\Users\austi\Anaconda3\lib\os.py
import sys as sys # <module 'sys' (built-in)>
import json as json # C:\Users\austi\Anaconda3\lib\json\__init__.py
import binascii as binascii # <module 'binascii' (built-in)>
import hashlib as hashlib # C:\Users\austi\Anaconda3\lib\hashlib.py
from nt import isdir


# Variables with simple values

trial_period = 30

_n = 6549380614876658142239843127518355726709677171365943092295101515463043194535201613477679412024312990119003027951690113324019655026041674108124040490142169

_package = 'None'
_pubkey = 3156754680603053726312458854820573346222980642320013775541839708808517168264393754949042722669552634116578454380685104210321333633365039921040218042061753

__version__ = '361fa109f3a40c3f6f5fd26911d452e4a909c634'

# functions

def abspath(path): # reliably restored by inspect
    """ Return the absolute version of a path. """
    pass

def compute_digest(*args, **kwargs): # real signature unknown
    pass

def crypt(*args, **kwargs): # real signature unknown
    pass

def date_from_string(*args, **kwargs): # real signature unknown
    pass

def expanduser(path): # reliably restored by inspect
    """
    Expand ~ and ~user constructs.
    
        If user or $HOME is unknown, do nothing.
    """
    pass

def filter_package(*args, **kwargs): # real signature unknown
    pass

def filter_signatures(*args, **kwargs): # real signature unknown
    pass

def filter_vendor(*args, **kwargs): # real signature unknown
    pass

def find_licenses(*args, **kwargs): # real signature unknown
    pass

def gettempdir(): # reliably restored by inspect
    """ Accessor for tempfile.tempdir. """
    pass

def get_days_since_install(*args, **kwargs): # real signature unknown
    pass

def get_end_dates(*args, **kwargs): # real signature unknown
    pass

def get_install_date(*args, **kwargs): # real signature unknown
    pass

def get_license(*args, **kwargs): # real signature unknown
    pass

def get_license_dirs(*args, **kwargs): # real signature unknown
    pass

def get_license_paths(*args, **kwargs): # real signature unknown
    pass

def get_nag_msg(*args, **kwargs): # real signature unknown
    pass

def get_type_and_end_date(*args, **kwargs): # real signature unknown
    pass

# Error generating skeleton for function glob: Function has keyword-only parameters or annotations, use getfullargspec() API which can support them

def human_days_delta(*args, **kwargs): # real signature unknown
    pass

def isfile(path): # reliably restored by inspect
    """ Test whether a path is a regular file """
    pass

def is_license_valid(*args, **kwargs): # real signature unknown
    pass

def join(path, *paths): # reliably restored by inspect
    # no doc
    pass

def nag(*args, **kwargs): # real signature unknown
    pass

def on_wakari(*args, **kwargs): # real signature unknown
    pass

def print_info_line(*args, **kwargs): # real signature unknown
    pass

def read_licenses(*args, **kwargs): # real signature unknown
    pass

def show_info(*args, **kwargs): # real signature unknown
    pass

def verify_license(*args, **kwargs): # real signature unknown
    pass

# classes

class date(object):
    """ date(year, month, day) --> date object """
    def ctime(self): # real signature unknown; restored from __doc__
        """ Return ctime() style string. """
        pass

    @classmethod
    def fromordinal(cls, *args, **kwargs): # real signature unknown
        """ int -> date corresponding to a proleptic Gregorian ordinal. """
        pass

    @classmethod
    def fromtimestamp(cls, *args, **kwargs): # real signature unknown
        """ timestamp -> local date from a POSIX timestamp (like time.time()). """
        pass

    def isocalendar(self, *args, **kwargs): # real signature unknown
        """ Return a 3-tuple containing ISO year, week number, and weekday. """
        pass

    def isoformat(self, *args, **kwargs): # real signature unknown
        """ Return string in ISO 8601 format, YYYY-MM-DD. """
        pass

    def isoweekday(self, *args, **kwargs): # real signature unknown
        """
        Return the day of the week represented by the date.
        Monday == 1 ... Sunday == 7
        """
        pass

    def replace(self, *args, **kwargs): # real signature unknown
        """ Return date with new specified fields. """
        pass

    def strftime(self): # real signature unknown; restored from __doc__
        """ format -> strftime() style string. """
        pass

    def timetuple(self, *args, **kwargs): # real signature unknown
        """ Return time tuple, compatible with time.localtime(). """
        pass

    @classmethod
    def today(cls, *args, **kwargs): # real signature unknown
        """ Current date or datetime:  same as self.__class__.fromtimestamp(time.time()). """
        pass

    def toordinal(self, *args, **kwargs): # real signature unknown
        """ Return proleptic Gregorian ordinal.  January 1 of year 1 is day 1. """
        pass

    def weekday(self, *args, **kwargs): # real signature unknown
        """
        Return the day of the week represented by the date.
        Monday == 0 ... Sunday == 6
        """
        pass

    def __add__(self, *args, **kwargs): # real signature unknown
        """ Return self+value. """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __format__(self, *args, **kwargs): # real signature unknown
        """ Formats self with strftime. """
        pass

    def __getattribute__(self, *args, **kwargs): # real signature unknown
        """ Return getattr(self, name). """
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

    def __init__(self, year, month, day): # real signature unknown; restored from __doc__
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

    def __radd__(self, *args, **kwargs): # real signature unknown
        """ Return value+self. """
        pass

    def __reduce__(self): # real signature unknown; restored from __doc__
        """ __reduce__() -> (cls, state) """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __rsub__(self, *args, **kwargs): # real signature unknown
        """ Return value-self. """
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass

    def __sub__(self, *args, **kwargs): # real signature unknown
        """ Return self-value. """
        pass

    day = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    month = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    year = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    max = None # (!) real value is ''
    min = None # (!) real value is ''
    resolution = None # (!) real value is ''


class defaultdict(dict):
    """
    defaultdict(default_factory[, ...]) --> dict with default factory
    
    The default factory is called without arguments to produce
    a new value when a key is not present, in __getitem__ only.
    A defaultdict compares equal to a dict with the same items.
    All remaining arguments are treated the same as if they were
    passed to the dict constructor, including keyword arguments.
    """
    def copy(self): # real signature unknown; restored from __doc__
        """ D.copy() -> a shallow copy of D. """
        pass

    def __copy__(self, *args, **kwargs): # real signature unknown
        """ D.copy() -> a shallow copy of D. """
        pass

    def __getattribute__(self, *args, **kwargs): # real signature unknown
        """ Return getattr(self, name). """
        pass

    def __init__(self, default_factory, *some): # real signature unknown; restored from __doc__
        pass

    def __missing__(self, key): # real signature unknown; restored from __doc__
        """
        __missing__(key) # Called by __getitem__ for missing key; pseudo-code:
          if self.default_factory is None: raise KeyError((key,))
          self[key] = value = self.default_factory()
          return value
        """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ Return state information for pickling. """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    default_factory = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Factory for default value called by __missing__()."""



# variables with complex values

__loader__ = None # (!) real value is ''

__spec__ = None # (!) real value is ''

__test__ = {}

