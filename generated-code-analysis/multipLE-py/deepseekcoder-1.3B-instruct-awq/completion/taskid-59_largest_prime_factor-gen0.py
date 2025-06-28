def largest_prime_factor(n: int) -> int:
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """


    def is_prime(n: int) -> bool:
        if n == 2 or n == 3:
            return True
        if n % 2 == 0 or n <= 1:
            return False
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True

    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
    return n
