from typing import List

def below_threshold(l: List[int], t: int) -> bool:
    """Return True if all numbers in the list l are below threshold t.
    >>> below_threshold([1, 2, 4, 10], 100)
    True
    >>> below_threshold([1, 20, 4, 10], 5)
    False
    """

    for num in l:
        if num >= t:
            return False
    return True
