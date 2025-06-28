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
        raise ValueError("n must be greater than 0")

    def is_prime(num: int) -> bool:
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def fibonacci(num: int) -> int:
        a, b = 0, 1
        for _ in range(num):
            a, b = b, a + b
        return a

    i = 1
    count = 0
    while count < n:
        fib = fibonacci(i)
        if is_prime(fib):
            count += 1
        i += 1
    return fibonacci(i - 1)
