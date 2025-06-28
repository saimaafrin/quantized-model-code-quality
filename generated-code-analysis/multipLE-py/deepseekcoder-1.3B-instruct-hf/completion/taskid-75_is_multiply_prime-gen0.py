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
        if n < 2:
            return False
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                return False
        return True

    factors = []
    for i in range(2, int(a**0.5) + 1):
        if a % i == 0:
            if is_prime(i):
                factors.append(i)
            if is_prime(a // i):
                factors.append(a // i)
    factors.sort()
    return len(factors) == 3 and factors[0]**factors[1]**factors[2] == a
