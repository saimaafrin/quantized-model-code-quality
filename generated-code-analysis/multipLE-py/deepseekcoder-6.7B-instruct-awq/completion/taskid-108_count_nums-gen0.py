from typing import List

def count_nums(arr: List[int]) -> int:
    """
    Write a function count_nums which takes an array of integers and returns
    the number of elements which has a sum of digits > 0.
    If a number is negative, then its first signed digit will be negative:
    e.g. -123 has signed digits -1, 2, and 3.
    >>> count_nums([])
    0
    >>> count_nums([-1, 11, -11])
    1
    >>> count_nums([1, 1, 2])
    3
    """

    def sum_digits(n: int) -> int:
        res = 0
        while n:
            res += n % 10
            n //= 10
        return res

    count = 0
    for num in arr:
        if sum_digits(num) > 0:
            count += 1
    return count
