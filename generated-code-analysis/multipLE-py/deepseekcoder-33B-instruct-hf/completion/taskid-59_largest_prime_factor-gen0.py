def largest_prime_factor(n: int) -> int:
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """

    if n % 2 == 0:
        return largest_prime_factor(n // 2)
    else:
        p = 3
        while n % p != 0 or n == p:
            p += 2
        if p < n:
            return largest_prime_factor(n // p)
        else:
            return n
