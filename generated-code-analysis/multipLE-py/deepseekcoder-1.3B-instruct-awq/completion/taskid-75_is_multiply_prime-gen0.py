def is_multiply_prime(a: int) -> bool:
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    >>> is_multiply_prime(30)
    True
    30 = 2 * 3 * 5
    """

    def is_prime(n: int) -> bool:
        if n <= 1:
            return False
        elif n <= 3:
            return True
        elif n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    factors = []
    for i in range(2, int(a**0.5) + 1):
        if a % i == 0 and is_prime(i):
            factors.append(i)
        if a % (i + 2) == 0 and is_prime(i + 2):
            factors.append(i + 2)

    return len(factors) == 3
