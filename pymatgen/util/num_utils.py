"""
This module provides utilities for basic math operations.
"""
from __future__ import division, print_function

import itertools
import collections
import numpy as np


def iterator_from_slice(s):
    """
    Constructs an iterator given a slice object s.

    .. note::

        The function returns an infinite iterator if s.stop is None
    """
    start = s.start if s.start is not None else 0
    step = s.step if s.step is not None else 1

    if s.stop is None:
        # Infinite iterator.
        return itertools.count(start=start, step=step)
    else:
        # xrange-like iterator that suppors float.
        return iter(np.arange(start, s.stop, step))


def sort_dict(d, key=None, reverse=False):
    """
    Sorts a dict by value.

    Args:
        d:
            Input dictionary
        key:
            function which takes an tuple (key, object) and returns a value to
            compare and sort by. By default, the function compares the values
            of the dict i.e. key = lambda t : t[1]
        reverse:
            allows to reverse sort order.

    Returns:
        OrderedDict object whose keys are ordered according to their value.
    """
    kv_items = [kv for kv in d.items()]

    # Sort kv_items according to key.
    if key is None:
        kv_items.sort(key=lambda t: t[1], reverse=reverse)
    else:
        kv_items.sort(key=key, reverse=reverse)

    # Build ordered dict.
    return collections.OrderedDict(kv_items)


def chunks(items, n):
    """
    Yield successive n-sized chunks from a list-like object.

    >>> import pprint
    >>> pprint.pprint(list(chunks(range(1, 25), 10)))
    [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
     [11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
     [21, 22, 23, 24]]
    """
    for i in range(0, len(items), n):
        yield items[i:i+n]


def min_max_indexes(seq):
    """
    Uses enumerate, max, and min to return the indices of the values
    in a list with the maximum and minimum value:
    """
    minimum = min(enumerate(seq), key=lambda s: s[1])
    maximum = max(enumerate(seq), key=lambda s: s[1])
    return minimum[0], maximum[0]


def strictly_increasing(values):
    """True if values are stricly increasing."""
    return all(x < y for x, y in zip(values, values[1:]))


def strictly_decreasing(values):
    """True if values are stricly decreasing."""
    return all(x > y for x, y in zip(values, values[1:]))


def non_increasing(values):
    """True if values are not increasing."""
    return all(x >= y for x, y in zip(values, values[1:]))


def non_decreasing(values):
    """True if values are not decreasing."""
    return all(x <= y for x, y in zip(values, values[1:]))


def monotonic(values, mode="<", atol=1.e-8):
    """
    Returns False if values are not monotonic (decreasing|increasing).
    mode is "<" for a decreasing sequence, ">" for an increasing sequence.
    Two numbers are considered equal if they differ less that atol.

    .. warning:
        Not very efficient for large data sets.

    >>> values = [1.2, 1.3, 1.4]
    >>> monotonic(values, mode="<")
    False
    >>> monotonic(values, mode=">")
    True
    """
    if len(values) == 1:
        return True

    if mode == ">":
        for i in range(len(values)-1):
            v, vp = values[i], values[i+1]
            if abs(vp - v) > atol and vp <= v:
                return False

    elif mode == "<":
        for i in range(len(values)-1):
            v, vp = values[i], values[i+1]
            if abs(vp - v) > atol and vp >= v:
                return False

    else:
        raise ValueError("Wrong mode %s" % str(mode))

    return True


#def listify(obj):
#    """
#    Transform any object, iterable or not, to a list. 
#    Returns obj if object is Iterable with the exception of 
#    single string that is converted to list.
#    """
#    if is_string(obj)
#       return [obj]
#
#    if isinstance(obj, collections.Iterable):
#        if isinstance(obj, tuple):
#            return list(obj)
#        else:
#            return obj
#
#    elif isinstance(obj, collections.Iterator):
#        return list(obj)
#
#    else:
#        return [obj]
