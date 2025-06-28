from typing import List

def generate_integers(a: int, b: int) -> List[int]:
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    >>> generate_integers(2, 8)
    [2, 4, 6, 8]
    >>> generate_integers(8, 2)
    [2, 4, 6, 8]
    >>> generate_integers(10, 14)
    []
    """

    # The problem is ambiguous, as it doesn't specify what to do if a is greater than b.
    # I'm going to assume that if a is greater than b, it's a mistake and should return an empty list.
    if a > b:
        return []

    # We start with an empty list.
    result = []

    # We loop over all the integers from a to b.
    for i in range(a, b+1):
        # If the integer is even, we add it to the result list.
        if i % 2 == 0:
            result.append(i)

    # We return the result list.
    return result
