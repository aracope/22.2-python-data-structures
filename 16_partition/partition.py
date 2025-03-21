def partition(lst, fn):
    """Partition lst by predicate.

    - lst: list of items
    - fn: function that returns True or False

    Returns new list: [a, b], where `a` are items that passed fn test,
    and `b` are items that failed fn test.

       >>> def is_even(num):
       ...     return num % 2 == 0

       >>> def is_string(el):
       ...     return isinstance(el, str)

       >>> partition([1, 2, 3, 4], is_even)
       [[2, 4], [1, 3]]

       >>> partition(["hi", None, 6, "bye"], is_string)
       [['hi', 'bye'], [None, 6]]
    """
    # Elements that pass the test
    passed = [item for item in lst if fn(item)]

    # Elements that fail the test
    failed = [item for item in lst if not fn(item)]

    return [passed, failed]
