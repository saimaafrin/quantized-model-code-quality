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

    diff = l[1] - l[0]
    for i in range(2, len(l)):
        if diff == 0:
            diff = l[i] - l[i - 1]
        if diff > 0:
            if l[i] <= l[i - 1]:
                return False
        else:
            if l[i] >= l[i - 1]:
                return False
    return True
