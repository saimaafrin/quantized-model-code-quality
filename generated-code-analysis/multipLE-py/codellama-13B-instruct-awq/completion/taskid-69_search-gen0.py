from typing import List

def search(lst: List[int]) -> int:
    """
    You are given a non-empty list of positive integers. Return the greatest integer that is greater than 
    zero, and has a frequency greater than or equal to the value of the integer itself. 
    The frequency of an integer is the number of times it appears in the list.
    If no such a value exist, return -1.
    Examples:
    >>> search([4, 1, 2, 2, 3, 1])
    2
    >>> search([1, 2, 2, 3, 3, 3, 4, 4, 4])
    3
    >>> search([5, 5, 4, 4, 4])
    -1
    """

    max_count = 0
    max_key = None
    frequency = {}
    for item in lst:
        if item > 0:
            if item in frequency:
                frequency[item] += 1
            else:
                frequency[item] = 1
            if frequency[item] > max_count:
                max_count = frequency[item]
                max_key = item
    if max_key is not None and max_count >= max_key:
        return max_key
    else:
        return -1
