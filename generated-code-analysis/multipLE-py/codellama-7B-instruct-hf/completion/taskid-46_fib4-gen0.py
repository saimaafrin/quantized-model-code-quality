def fib4(n: int) -> int:
    """The Fib4 number sequence is a sequence similar to the Fibbonacci sequnece that's defined as follows:
    fib4(0) -> 0
    fib4(1) -> 0
    fib4(2) -> 2
    fib4(3) -> 0
    fib4(n) -> fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4).
    Please write a function to efficiently compute the n-th element of the fib4 number sequence.  Do not use recursion.
    >>> fib4(5)
    4
    >>> fib4(6)
    8
    >>> fib4(7)
    14
    """


    # Initialize variables
    a = 0
    b = 0
    c = 2
    count = 0

    # Check if n is zero
    if n == 0:
        return a

    # Check if n is one
    if n == 1:
        return b

    # Check if n is two
    if n == 2:
        return c

    # Iterate through the sequence
    while count < n - 3:
        a, b, c = b, c, a + b + c
        count += 1

    return a + b + c
