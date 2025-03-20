def includes(collection, sought, start=None):
    """Is sought in collection, starting at index start?

    Return True/False if sought is in the given collection:
    - lists/strings/sets/tuples: returns True/False if sought present
    - dictionaries: return True/False if *value* of sought in dictionary

    If string/list/tuple and `start` is provided, starts searching only at that
    index. This `start` is ignored for sets/dictionaries, since they aren't
    ordered.

        >>> includes([1, 2, 3], 1)
        True

        >>> includes([1, 2, 3], 1, 2)
        False

        >>> includes("hello", "o")
        True

        >>> includes(('Elmo', 5, 'red'), 'red', 1)
        True

        >>> includes({1, 2, 3}, 1)
        True

        >>> includes({1, 2, 3}, 1, 3)  # "start" ignored for sets!
        True

        >>> includes({"apple": "red", "berry": "blue"}, "blue")
        True
    """

    # If collection is a dictionary, check if sought is in the values
    if isinstance(collection, dict):
        return sought in collection.values()

    # If collection is a set, ignore `start` and check membership
    if isinstance(collection, set):
        return sought in collection

    # If start is provided and collection is indexable (list, tuple, string)
    if start is not None and isinstance(collection, (list, tuple, str)):
        return sought in collection[start:]

    # Default case: check if sought is in collection
    return sought in collection
