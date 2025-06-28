from typing import List

def specialFilter(nums: List[int]) -> int:
    """Write a function that takes an array of numbers as input and returns 
    the number of elements in the array that are greater than 10 and both 
    first and last digits of a number are odd (1, 3, 5, 7, 9).
    For example:
    >>> specialFilter([15, -73, 14, -15])
    1
    >>> specialFilter([33, -2, -3, 45, 21, 109])
    2
    """

    def is_special(n):
        n = abs(n)
        first_last_are_odd = str(n)[0] in ['1', '3', '5', '7', '9'] and str(n)[-1] in ['1', '3', '5', '7', '9']
        return n > 10 and first_last_are_odd

    return sum(is_special(n) for n in nums)
