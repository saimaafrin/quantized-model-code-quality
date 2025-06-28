from typing import List

def add_elements(arr: List[int], k: int) -> int:
    """
    Given a non-empty array of integers arr and an integer k, return
    the sum of the elements with at most two digits from the first k elements of arr.

    Example:

    >>> add_elements([111, 21, 3, 4000, 5, 6, 7, 8, 9], 4)
    24

    Constraints:
        1. 1 <= len(arr) <= 100
        2. 1 <= k <= len(arr)
    """


    # get the sum of the numbers with 2 digits
    two_digit = 0
    for num in arr[:k]:
        two_digit += num % 100

    # get the sum of the numbers with one digit
    one_digit = 0
    for num in arr[:k]:
        if num // 100 == 0:
            one_digit += num

    # sum of all the numbers with 2 digits is always greater than the sum of all numbers with 1 digit
    # so if the sum of all the numbers with 1 digit is greater than or equal to the sum of all the
    # numbers with 2 digits, then we just need to sum the numbers with 1 digit
    if one_digit >= two_digit:
        return one_digit

    # sum of all the numbers with 1 digit and all the numbers with 2 digits
    return one_digit + two_digit
