def largest_prime_factor(n: int) -> int:
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """

    i = 2
    while i <= n ** 0.5:
        if n % i == 0:
            return i if n // i == 1 else largest_prime_factor(n // i)
        i += 1
    raise ValueError(f"Can't find largest prime factor of {n}")
