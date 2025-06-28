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


    if len(arr) == 0:
        return 0

    # Find the midpoint of the array
    mid = len(arr) // 2

    # Find the maximum number of elements that need to be changed
    # to make the left half of the array equal to the right half
    # of the array.
    left_mid = mid
    left_count = 0
    while left_mid >= 0:
        if arr[left_mid] != arr[mid - left_mid]:
            left_count += 1
        left_mid -= 1

    # Find the maximum number of elements that need to be changed
    # to make the right half of the array equal to the left half
    # of the array.
    right_mid = mid
    right_count = 0
    while right_mid < len(arr):
        if arr[right_mid] != arr[mid - right_mid]:
            right_count += 1
        right_mid += 1

    # Return the minimum number of elements that need to be changed
    # to make the array palindromic.
    return min(left_count, right_count)
