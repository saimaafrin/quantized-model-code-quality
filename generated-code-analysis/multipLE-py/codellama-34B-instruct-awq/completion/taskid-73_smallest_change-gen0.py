from typing import List

def smallest_change(arr: List[int]) -> int:
    """
    Given an array arr of integers, find the minimum number of elements that
    need to be changed to make the array palindromic. A palindromic array is an array that
    is read the same backwards and forwards. In one change, you can change one element to any other element.

    For example:
    >>> smallest_change([1, 2, 3, 5, 4, 7, 9, 6])
    4
    >>> smallest_change([1, 2, 3, 4, 3, 2, 2])
    1
    >>> smallest_change([1, 2, 3, 2, 1])
    0
    """

    if len(arr) < 2:
        return 0

    # This implementation uses a dynamic programming approach.
    # We keep a table of the longest palindromic sequence for each index of the array.
    # The longest palindromic sequence is a sequence where every element matches the
    # element at the same index in the reversed array.
    # At each index, we can either use the element at that index, or we can change it to the
    # element at the same index in the reversed array. This allows us to do O(n) work to find the
    # minimum number of changes we need to make to make the array palindromic.
    #
    # For example:
    # arr = [1, 2, 3, 4, 5]
    # rev = [5, 4, 3, 2, 1]
    # table = [
    #   [1, 1, 0, 0, 0],
    #   [1, 1, 1, 0, 0],
    #   [1, 1, 1, 1, 0],
    #   [1, 1, 1, 1, 1],
    #   [1, 1, 1, 1, 1],
    # ]

    table = [[1] * len(arr) for _ in range(len(arr))]

    # table[i][j] represents the length of the longest palindromic sequence starting at index i
    # and ending at index j
    for i in range(1, len(arr)):
        # table[i][j] is at most len(arr)
        for j in range(i, len(arr)):
            # If the element at index i matches the element at index j
            # in the reversed array, then we can extend the palindromic
            # sequence starting at index i - 1 and ending at index j + 1.
            if arr[i] == arr[len(arr) - j - 1]:
                table[i][j] = table[i - 1][j - 1] + 1
            else:
                # Otherwise, we can either use the element at index i, or
                # the element at index j in the reversed array.
                table[i][j] = max(table[i - 1][j], table[i][j - 1])

    # The number of changes we need to make is the length of the original array minus
    # the length of the longest palindromic sequence.
    return len(arr) - table[-1][-1]
