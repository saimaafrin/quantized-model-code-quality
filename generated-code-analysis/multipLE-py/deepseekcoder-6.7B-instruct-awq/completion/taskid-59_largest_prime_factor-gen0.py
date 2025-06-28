def largest_prime_factor(n: int) -> int:
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """

    def prime_divisor(n: int) -> int:
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return i
        return n

    factor = prime_divisor(n)
    while n != factor:
        n = n // factor
        factor = prime_divisor(n)

    return factor
