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

    assert a > 0
    assert b > 0

    # If a is greater than b, swap them so a is always the smaller number
    if a > b:
        a, b = b, a

    # We only want to return even numbers
    if a % 2 == 1:
        a += 1

    if b % 2 == 1:
        b -= 1

    # We can't use range() because we need to be able to handle cases
    # where a is greater than b
    result = []
    for num in range(a, b + 1):
        if num % 2 == 0:
            result.append(num)

    return result
