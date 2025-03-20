def min_max_keys(d):
    """Return tuple (min-keys, max-keys) in d.

        >>> min_max_keys({2: 'a', 7: 'b', 1: 'c', 10: 'd', 4: 'e'})
        (1, 10)

    Works with any kind of key that can be compared, like strings:

        >>> min_max_keys({"apple": "red", "cherry": "red", "berry": "blue"})
        ('apple', 'cherry')
    """
    
    """
    d.keys gives us a view of all the keys in the dictionary.
    min and max are built in functions for python
    The result is returned as a tuple with the smallest key first and the largest key second."
    """
    return (min(d.keys()), max(d.keys()))
