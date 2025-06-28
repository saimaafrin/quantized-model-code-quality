def largest_prime_factor(n: int) -> int:
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """

    for d in range(int(n ** 0.5), 1, -1):
        if n % d == 0 and is_prime(d):
            return d
