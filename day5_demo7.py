import doctest


def square(x):
    """
    >>> square(2)
    4
    >>> square(-2)
    -4
    >>> square(3)
    9
    """
    return x * x

doctest.testmod()