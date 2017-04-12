# encoding: utf-8
# module sklearn.linear_model.sgd_fast
# from C:\Users\austi\Anaconda3\lib\site-packages\sklearn\linear_model\sgd_fast.cp36-win_amd64.pyd
# by generator 1.145
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import numpy as np # C:\Users\austi\Anaconda3\lib\site-packages\numpy\__init__.py
import sys as sys # <module 'sys' (built-in)>
from time import time


# functions

def average_sgd(*args, **kwargs): # real signature unknown
    """
    Average SGD for generic loss functions and penalties.
    
        Parameters
        ----------
        weights : ndarray[double, ndim=1]
            The allocated coef_ vector.
        intercept : double
            The initial intercept.
        average_weights : ndarray[double, ndim=1]
            The average weights as computed for ASGD
        average_intercept : double
            The average intercept for ASGD
        loss : LossFunction
            A concrete ``LossFunction`` object.
        penalty_type : int
            The penalty 2 for L2, 1 for L1, and 3 for Elastic-Net.
        alpha : float
            The regularization parameter.
        C : float
            Maximum step size for passive aggressive.
        l1_ratio : float
            The Elastic Net mixing parameter, with 0 <= l1_ratio <= 1.
            l1_ratio=0 corresponds to L2 penalty, l1_ratio=1 to L1.
        dataset : SequentialDataset
            A concrete ``SequentialDataset`` object.
        n_iter : int
            The number of iterations (epochs).
        fit_intercept : int
            Whether or not to fit the intercept (1 or 0).
        verbose : int
            Print verbose output; 0 for quite.
        shuffle : boolean
            Whether to shuffle the training data before each epoch.
        weight_pos : float
            The weight of the positive class.
        weight_neg : float
            The weight of the negative class.
        seed : np.uint32_t
            Seed of the pseudorandom number generator used to shuffle the data.
        learning_rate : int
            The learning rate:
            (1) constant, eta = eta0
            (2) optimal, eta = 1.0/(alpha * t).
            (3) inverse scaling, eta = eta0 / pow(t, power_t)
            (4) Passive Aggressive-I, eta = min(alpha, loss/norm(x))
            (5) Passive Aggressive-II, eta = 1.0 / (norm(x) + 0.5*alpha)
        eta0 : double
            The initial learning rate.
        power_t : double
            The exponent for inverse scaling learning rate.
        t : double
            Initial state of the learning rate. This value is equal to the
            iteration count except when the learning rate is set to `optimal`.
            Default: 1.0.
        average : int
            The number of iterations before averaging starts. average=1 is
            equivalent to averaging for all iterations.
    
        Returns
        -------
        weights : array, shape=[n_features]
            The fitted weight vector.
        intercept : float
            The fitted intercept term.
        average_weights : array shape=[n_features]
            The averaged weights across iterations
        average_intercept : float
            The averaged intercept across iterations
    """
    pass

def plain_sgd(*args, **kwargs): # real signature unknown
    """
    Plain SGD for generic loss functions and penalties.
    
        Parameters
        ----------
        weights : ndarray[double, ndim=1]
            The allocated coef_ vector.
        intercept : double
            The initial intercept.
        loss : LossFunction
            A concrete ``LossFunction`` object.
        penalty_type : int
            The penalty 2 for L2, 1 for L1, and 3 for Elastic-Net.
        alpha : float
            The regularization parameter.
        C : float
            Maximum step size for passive aggressive.
        l1_ratio : float
            The Elastic Net mixing parameter, with 0 <= l1_ratio <= 1.
            l1_ratio=0 corresponds to L2 penalty, l1_ratio=1 to L1.
        dataset : SequentialDataset
            A concrete ``SequentialDataset`` object.
        n_iter : int
            The number of iterations (epochs).
        fit_intercept : int
            Whether or not to fit the intercept (1 or 0).
        verbose : int
            Print verbose output; 0 for quite.
        shuffle : boolean
            Whether to shuffle the training data before each epoch.
        weight_pos : float
            The weight of the positive class.
        weight_neg : float
            The weight of the negative class.
        seed : np.uint32_t
            Seed of the pseudorandom number generator used to shuffle the data.
        learning_rate : int
            The learning rate:
            (1) constant, eta = eta0
            (2) optimal, eta = 1.0/(alpha * t).
            (3) inverse scaling, eta = eta0 / pow(t, power_t)
            (4) Passive Agressive-I, eta = min(alpha, loss/norm(x))
            (5) Passive Agressive-II, eta = 1.0 / (norm(x) + 0.5*alpha)
        eta0 : double
            The initial learning rate.
        power_t : double
            The exponent for inverse scaling learning rate.
        t : double
            Initial state of the learning rate. This value is equal to the
            iteration count except when the learning rate is set to `optimal`.
            Default: 1.0.
    
        Returns
        -------
        weights : array, shape=[n_features]
            The fitted weight vector.
        intercept : float
            The fitted intercept term.
    """
    pass

def _plain_sgd(*args, **kwargs): # real signature unknown
    pass

# classes

class LossFunction(object):
    """ Base class for convex loss functions """
    def dloss(self, *args, **kwargs): # real signature unknown
        """
        Evaluate the derivative of the loss function with respect to
                the prediction `p`.
        
                Parameters
                ----------
                p : double
                    The prediction, p = w^T x
                y : double
                    The true value (aka target)
                Returns
                -------
                double
                    The derivative of the loss function with regards to `p`.
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    __pyx_vtable__ = None # (!) real value is ''


class Classification(LossFunction):
    """ Base class for loss functions for classification """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    __pyx_vtable__ = None # (!) real value is ''


class Regression(LossFunction):
    """ Base class for loss functions for regression """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    __pyx_vtable__ = None # (!) real value is ''


class EpsilonInsensitive(Regression):
    """
    Epsilon-Insensitive loss (used by SVR).
    
        loss = max(0, |y - p| - epsilon)
    """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    __pyx_vtable__ = None # (!) real value is ''


class Hinge(Classification):
    """
    Hinge loss for binary classification tasks with y in {-1,1}
    
        Parameters
        ----------
    
        threshold : float > 0.0
            Margin threshold. When threshold=1.0, one gets the loss used by SVM.
            When threshold=0.0, one gets the loss used by the Perceptron.
    """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    __pyx_vtable__ = None # (!) real value is ''


class Huber(Regression):
    """
    Huber regression loss
    
        Variant of the SquaredLoss that is robust to outliers (quadratic near zero,
        linear in for large errors).
    
        https://en.wikipedia.org/wiki/Huber_Loss_Function
    """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    __pyx_vtable__ = None # (!) real value is ''


class Log(Classification):
    """ Logistic regression loss for binary classification with y in {-1, 1} """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    __pyx_vtable__ = None # (!) real value is ''


class ModifiedHuber(Classification):
    """
    Modified Huber loss for binary classification with y in {-1, 1}
    
        This is equivalent to quadratically smoothed SVM with gamma = 2.
    
        See T. Zhang 'Solving Large Scale Linear Prediction Problems Using
        Stochastic Gradient Descent', ICML'04.
    """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    __pyx_vtable__ = None # (!) real value is ''


class SquaredEpsilonInsensitive(Regression):
    """
    Epsilon-Insensitive loss.
    
        loss = max(0, |y - p| - epsilon)^2
    """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    __pyx_vtable__ = None # (!) real value is ''


class SquaredHinge(Classification):
    """
    Squared Hinge loss for binary classification tasks with y in {-1,1}
    
        Parameters
        ----------
    
        threshold : float > 0.0
            Margin threshold. When threshold=1.0, one gets the loss used by
            (quadratically penalized) SVM.
    """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    __pyx_vtable__ = None # (!) real value is ''


class SquaredLoss(Regression):
    """ Squared loss traditional used in linear regression. """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    __pyx_vtable__ = None # (!) real value is ''


# variables with complex values

__loader__ = None # (!) real value is ''

__spec__ = None # (!) real value is ''

__test__ = {}

