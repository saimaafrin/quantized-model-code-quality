from typing import List

def median(l: List[int]) -> float:
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """

    l.sort()
    n = len(l)
    m1 = l[n//2]
    m2 = l[-(n+1)//2]
    return (m1 + m2) / 2.0
