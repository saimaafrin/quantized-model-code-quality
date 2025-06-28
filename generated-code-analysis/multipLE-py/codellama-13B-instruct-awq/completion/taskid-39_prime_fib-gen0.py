def prime_fib(n: int) -> int:
    """
    prime_fib returns n-th number that is a Fibonacci number and it's also prime.
    >>> prime_fib(1)
    2
    >>> prime_fib(2)
    3
    >>> prime_fib(3)
    5
    >>> prime_fib(4)
    13
    >>> prime_fib(5)
    89
    """

    if n < 1:
        raise ValueError('n must be greater than or equal to 1.')

    if n == 1:
        return 2

    a, b = 1, 1
    for _ in range(n):
        a, b = b, a + b
        if is_prime(b):
            n -= 1
        if n < 1:
            break

    return b
