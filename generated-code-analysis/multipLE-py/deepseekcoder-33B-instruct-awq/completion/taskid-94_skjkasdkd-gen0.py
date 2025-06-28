from typing import List

def skjkasdkd(lst: List[int]) -> int:
    """You are given a list of integers.
    You need to find the largest prime value and return the sum of its digits.

    Examples:
    >>> skjkasdkd([0, 3, 2, 1, 3, 5, 7, 4, 5, 5, 5, 2, 181, 32, 4, 32, 3, 2, 32, 324, 4, 3])
    10
    >>> skjkasdkd([1, 0, 1, 8, 2, 4597, 2, 1, 3, 40, 1, 2, 1, 2, 4, 2, 5, 1])
    25
    >>> skjkasdkd([1, 3, 1, 32, 5107, 34, 83278, 109, 163, 23, 2323, 32, 30, 1, 9, 3])
    13
    >>> skjkasdkd([0, 724, 32, 71, 99, 32, 6, 0, 5, 91, 83, 0, 5, 6])
    11
    >>> skjkasdkd([0, 81, 12, 3, 1, 21])
    3
    >>> skjkasdkd([0, 8, 1, 2, 1, 7])
    7
    """


    def is_prime(n: int) -> bool:
        """Check if n is a prime number.

        Parameters:
        n (int): number to check

        Returns:
        bool: True if n is a prime number, False otherwise.
        """
        if n <= 1:
            return False

        if n == 2:
            return True

        if n % 2 == 0:
            return False

        i = 3
        while i * i <= n:
            if n % i == 0:
                return False
            i += 2

        return True

    def sum_of_digits(n: int) -> int:
        """Calculate the sum of the digits of n.

        Parameters:
        n (int): number to calculate the sum of its digits

        Returns:
        int: sum of the digits of n.
        """
        return sum(int(i) for i in str(n))

    max_prime = 0
    for num in lst:
        if is_prime(num) and num > max_prime:
            max_prime = num

    return sum_of_digits(max_prime)
