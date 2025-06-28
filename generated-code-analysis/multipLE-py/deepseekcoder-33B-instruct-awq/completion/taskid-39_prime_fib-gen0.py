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
        raise ValueError("n must be a positive integer")
    count, num = 0, 2
    while count < n:
        if is_prime(num) and is_fibonacci(num):
            count += 1
        num += 1
    return num - 1
