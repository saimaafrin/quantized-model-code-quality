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

    if n <= 0:
        raise ValueError("n should be a positive integer.")
    else:
        fib_seq = fib(n)
        for i in fib_seq:
            if is_prime(i):
                return i
        return fib_seq[-1]
