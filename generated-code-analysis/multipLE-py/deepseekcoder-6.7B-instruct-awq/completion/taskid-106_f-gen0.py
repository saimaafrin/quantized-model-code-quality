from typing import List

def f(n: int) -> List[int]:
    """ Implement the function f that takes n as a parameter,
    and returns a list of size n, such that the value of the element at index i is the factorial of i if i is even
    or the sum of numbers from 1 to i otherwise.
    i starts from 1.
    the factorial of i is the multiplication of the numbers from 1 to i (1 * 2 * ... * i).
    Example:
    >>> f(5)
    [1, 2, 6, 24, 15]
    """


    def factorial(x: int) -> int:
        if x == 0:
            return 1
        else:
            return x * factorial(x - 1)

    def sum_to_n(x: int) -> int:
        return sum(range(1, x + 1))

    return [factorial(i) if i % 2 == 0 else sum_to_n(i) for i in range(1, n + 1)]
