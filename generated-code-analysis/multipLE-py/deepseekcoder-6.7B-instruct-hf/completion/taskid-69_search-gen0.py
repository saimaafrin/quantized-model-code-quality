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

    frequency_dict = {}
    for num in lst:
        frequency_dict[num] = frequency_dict.get(num, 0) + 1
    sorted_keys = sorted(frequency_dict.keys(), reverse=True)
    for key in sorted_keys:
        if key <= len(lst) and frequency_dict[key] >= key:
            return key
    return -1
