from typing import List

def double_the_difference(lst: List[float]) -> int:
    """
    Given a list of numbers, return the sum of squares of the numbers
    in the list that are odd. Ignore numbers that are negative or not integers.
    
    >>> double_the_difference([1, 3, 2, 0])
    10
    >>> double_the_difference([-1, -2, 0])
    0
    >>> double_the_difference([9, -2])
    81
    >>> double_the_difference([0])
    0
   
    If the input list is empty, return 0.
    """

    if not lst:
        return 0
    # Calculate the sum of all numbers in the list
    sum_of_list = sum(lst)
    # Calculate the sum of odd numbers in the list
    sum_of_odd_numbers = sum([x for x in lst if x % 2 != 0])
    # Calculate the difference between the two sums
    diff = sum_of_list - sum_of_odd_numbers
    # Return the difference squared
    return diff * diff
