from typing import List

def monotonic(l: List[int]) -> bool:
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """

    if len(l) < 2:
        return True
    direction = l[1] - l[0]
    if direction == 0:
        return monotonic(l[1:])
    for i in range(len(l) - 1):
        if (l[i+1] - l[i]) * direction < 0:
            return False
    return True
