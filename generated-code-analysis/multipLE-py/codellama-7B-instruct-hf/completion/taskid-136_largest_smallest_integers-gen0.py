from typing import List, Tuple, Optional

def largest_smallest_integers(lst: List[int]) -> Tuple[Optional[int], Optional[int]]:
    """
    Create a function that returns a tuple (a, b), where 'a' is
    the largest of negative integers, and 'b' is the smallest
    of positive integers in a list.
    If there is no negative or positive integers, return them as None.

    Examples:
    >>> largest_smallest_integers([2, 4, 1, 3, 5, 7])
    (None, 1)
    >>> largest_smallest_integers([])
    (None, None)
    >>> largest_smallest_integers([0])
    (None, None)
    """

    # sort the list in ascending order
    lst.sort()

    # find the smallest positive integer
    smallest = None
    for i in range(len(lst)):
        if lst[i] > 0:
            smallest = lst[i]
            break

    # find the largest negative integer
    largest = None
    for i in range(len(lst)-1, -1, -1):
        if lst[i] < 0:
            largest = lst[i]
            break

    return (largest, smallest)
