from typing import List

def median(l: List[int]) -> float:
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """

    l.sort()
    llen = len(l)
    if llen % 2 == 0:
        return (l[llen // 2 - 1] + l[llen // 2]) / 2
    return l[llen // 2]
