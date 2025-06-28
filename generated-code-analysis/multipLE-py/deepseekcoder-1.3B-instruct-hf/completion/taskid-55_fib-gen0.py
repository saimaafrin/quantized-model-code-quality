def fib(n: int) -> int:
    """Return n-th Fibonacci number.
    >>> fib(10)
    55
    >>> fib(1)
    1
    >>> fib(8)
    21
    """

    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        fib_list = [0, 1]
        while len(fib_list) < n:
            fib_list.append(fib_list[-1] + fib_list[-2])
        return fib_list[-1]
