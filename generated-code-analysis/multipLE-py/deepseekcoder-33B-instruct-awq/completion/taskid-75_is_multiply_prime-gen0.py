def is_multiply_prime(a: int) -> bool:
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    >>> is_multiply_prime(30)
    True
    30 = 2 * 3 * 5
    """

    primes = []
    for i in range(2, a + 1):
        primes.append(i)
        for j in range(2, i):
            if i % j == 0:
                primes.remove(i)
                break
    print(primes)
    for prime in primes:
        if a % prime == 0:
            a = a / prime
            if a in primes:
                return True
    return False
