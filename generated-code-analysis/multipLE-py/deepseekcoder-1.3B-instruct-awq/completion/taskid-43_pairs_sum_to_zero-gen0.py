from typing import List

def pairs_sum_to_zero(l: List[int]) -> bool:
    """
    pairs_sum_to_zero takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.
    >>> pairs_sum_to_zero([1, 3, 5, 0])
    False
    >>> pairs_sum_to_zero([1, 3, -2, 1])
    False
    >>> pairs_sum_to_zero([1, 2, 3, 7])
    False
    >>> pairs_sum_to_zero([2, 4, -5, 3, 5, 7])
    True
    >>> pairs_sum_to_zero([1])
    False
    """


    # create an empty set to store the encountered numbers
    encountered = set()

    # iterate through the list
    for num in l:
        # if the number has been encountered before, return True
        if -num in encountered:
            return True
        # otherwise, add the number to the set of encountered numbers
        encountered.add(num)

    # if we reach here, it means there are no numbers that sum to zero
    return False
