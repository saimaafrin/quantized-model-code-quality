from typing import List

def unique_digits(x: List[int]) -> List[int]:
    """Given a list of positive integers x. return a sorted list of all 
    elements that hasn't any even digit.

    Note: Returned list should be sorted in increasing order.
    
    For example:
    >>> unique_digits([15, 33, 1422, 1])
    [1, 15, 33]
    >>> unique_digits([152, 323, 1422, 10])
    []
    """


    def has_even_digit(n: int) -> bool:
        while n > 0:
            digit = n % 10
            if digit % 2 == 0:
                return True
            n = n // 10
        return False

    return sorted([i for i in x if not has_even_digit(i)])
