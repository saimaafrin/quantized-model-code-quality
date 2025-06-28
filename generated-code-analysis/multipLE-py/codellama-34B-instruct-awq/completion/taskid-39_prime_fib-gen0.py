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

    fib_num = [0, 1]
    while len(fib_num) <= n:
        fib_num.append(fib_num[-1] + fib_num[-2])
    return fib_num[n]
