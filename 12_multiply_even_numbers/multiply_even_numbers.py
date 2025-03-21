def multiply_even_numbers(nums):
    """Multiply the even numbers.

        >>> multiply_even_numbers([2, 3, 4, 5, 6])
        48

        >>> multiply_even_numbers([3, 4, 5])
        4

    If there are no even numbers, return 1.

        >>> multiply_even_numbers([1, 3, 5])
        1
    """
    product = 1
    found_even_num = False

    for num in nums:
        if num % 2 == 0:
            product *= num
            found_even_num = True

    return product if found_even_num else 1
