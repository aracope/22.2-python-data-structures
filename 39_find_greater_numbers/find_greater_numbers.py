def find_greater_numbers(nums):
    """Return # of times a number is followed by a greater number.

    For example, for [1, 2, 3], the answer is 3:
    - the 1 is followed by the 2 *and* the 3
    - the 2 is followed by the 3

    Examples:

        >>> find_greater_numbers([1, 2, 3])
        3

        >>> find_greater_numbers([6, 1, 2, 7])
        4

        >>> find_greater_numbers([5, 4, 3, 2, 1])
        0

        >>> find_greater_numbers([])
        0
    """
    """
    Iterate through the list using index i, for each number at nums[i], look at all numbers after it (nums[j] where j > i).
    If nums[j] is greater than nums[i], increment the count."
    """
    count = 0

    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):  # Look at numbers after nums[i]
            if nums[j] > nums[i]:
                count += 1

    return count
