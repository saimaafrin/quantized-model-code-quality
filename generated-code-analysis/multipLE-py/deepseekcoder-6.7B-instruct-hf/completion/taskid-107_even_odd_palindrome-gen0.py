from typing import Tuple

def even_odd_palindrome(n: int) -> Tuple[int, int]:
    """
    Given a positive integer n, return a tuple that has the number of even and odd
    integer palindromes that fall within the range(1, n), inclusive.

    Example 1:

    >>> even_odd_palindrome(3)
    (1, 2)
        Explanation:
        Integer palindrome are 1, 2, 3. one of them is even, and two of them are odd.

    Example 2:

    >>> even_odd_palindrome(12)
    (4, 6)
        Explanation:
        Integer palindrome are 1, 2, 3, 4, 5, 6, 7, 8, 9, 11. four of them are even, and 6 of them are odd.

    Note:
        1. 1 <= n <= 10^3
        2. returned tuple has the number of even and odd integer palindromes respectively.
    """

    def is_palindrome(num: int) -> bool:
        return str(num) == str(num)[::-1]

    def count_palindrome(length: int, even_odd: int) -> int:
        if length == 1:
            return 1 if even_odd == 1 else 2
        if length % 2 == 0:
            return 5 ** (length // 2) if even_odd == 1 else 5 ** (length // 2) * 3
        return 5 ** ((length + 1) // 2) * 2 if even_odd == 1 else 5 ** ((length + 1) // 2) * 5

    even, odd = 0, 0
    for length in range(1, len(str(n)) + 1):
        if length % 2 == 0:
            for eo in (1, 2):
                for num in range(10 ** (length - 1), 10 ** length):
                    if is_palindrome(num) and len(str(num)) == length and num % 2 == eo:
                        if eo == 1:
                            even += count_palindrome(length, eo)
                        else:
                            odd += count_palindrome(length, eo)
        else:
            for eo in (1, 2):
                for num in range(10 ** (length - 1), 10 ** length):
                    if is_palindrome(num) and len(str(num)) == length and num % 2 == eo:
                        if eo == 1:
                            even += count_palindrome(length, eo)
                        else:
                            odd += count_palindrome(length, eo)
    return (even, odd)
