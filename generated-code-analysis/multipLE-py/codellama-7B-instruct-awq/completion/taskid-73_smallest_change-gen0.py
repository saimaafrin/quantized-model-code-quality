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

    # find the first and last elements
    first, last = 0, len(arr) - 1
    while first < last and arr[first] == arr[last]:
        first += 1
        last -= 1

    # if the array is already palindromic, return 0
    if first == last:
        return 0

    # find the smallest element and the largest element
    smallest = last + 1
    largest = first - 1
    for i in range(first, last + 1):
        if arr[i] < smallest:
            smallest = arr[i]
        if arr[i] > largest:
            largest = arr[i]

    # find the smallest element to change
    smallest_to_change = largest + 1
    for i in range(first, last + 1):
        if arr[i] == smallest:
            smallest_to_change = i
            break

    # find the largest element to change
    largest_to_change = smallest - 1
    for i in range(first, last + 1):
        if arr[i] == largest:
            largest_to_change = i
            break

    # swap the smallest and largest elements
    arr[smallest_to_change], arr[largest_to_change] = arr[largest_to_change], arr[smallest_to_change]

    # return the number of elements that need to be changed
    return last - first + 1
