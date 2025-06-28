from typing import List

def can_arrange(arr: List[int]) -> int:
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    >>> can_arrange([1, 2, 4, 3, 5])
    3
    >>> can_arrange([1, 2, 3])
    -1
    """

    n = len(arr)
    if n < 2:
        return -1

    max_index = -1
    for i in range(n-1):
        for j in range(i+1, n):
            if arr[i] >= arr[j]:
                max_index = max(max_index, j)
                break

    return max_index
