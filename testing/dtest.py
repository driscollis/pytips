def double(a):
    """
    >>> double(4)
    8
    >>> double(9)
    18
    """
    return a*2


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)