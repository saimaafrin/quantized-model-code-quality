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

    max_negative_integer = None
    min_positive_integer = None

    for number in lst:
        if number > 0 and (min_positive_integer is None or number < min_positive_integer):
            min_positive_integer = number
        elif number < 0 and (max_negative_integer is None or number > max_negative_integer):
            max_negative_integer = number

    return max_negative_integer, min_positive_integer
