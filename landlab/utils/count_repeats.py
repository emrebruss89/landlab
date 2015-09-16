#! /usr/bin/env python


import numpy as np

from ..core.utils import as_id_array


def count_repeated_values(x):
    """Count how many times in an array values repeat and where they appear.

    Return a list of length *n* that gives the values and indices of repeated
    values. The first element of the list will be the values and indices of
    all values that appear once or the first time repeated values appear. The
    next element, values that repeat twice or more, and so on. Thus, the
    length of the returned list will be the maximum number that any value is
    repeated in *x*.

    Parameters
    ----------
    x : array_like
        Input array to count repeated values.

    Returns
    -------
    list of tuple
        List of tuples of (*repeated_values*, *indices*).

    Examples
    --------

    For an array that contains no repeated values, this function just returns
    a copy of *x*, and the indices to each element.

    >>> import numpy as np
    >>> from landlab.utils.count_repeats import count_repeated_values
    >>> counts = count_repeated_values(np.array([20, 30, 40], dtype=np.int))
    >>> len(counts)
    1
    >>> counts[0]
    (array([20, 30, 40]), array([0, 1, 2]))

    If *x* contains a repeated value, the first element contains all unique
    values along with their indices. For repeated values, return indices to
    their first occurance. The second element contains values and indices to
    values occuring two or more times.

    >>> counts = count_repeated_values(np.array([20, 30, 40, 30, 30], dtype=np.int))
    >>> len(counts)
    3
    >>> counts[0]
    (array([20, 30, 40]), array([0, 1, 2]))
    >>> counts[1]
    (array([30]), array([3]))
    >>> counts[2]
    (array([30]), array([4]))
    """
    counts = []

    (unique_values, unique_inds) = np.unique(x, return_index=True)
    x_inds = np.arange(len(x), dtype=np.int)
    while len(unique_values) > 0:
        counts.append((unique_values, x_inds[unique_inds]))
        x = np.delete(x, unique_inds)
        x_inds = np.delete(x_inds, unique_inds)
        (unique_values, unique_inds) = np.unique(x, return_index=True)

    return counts
