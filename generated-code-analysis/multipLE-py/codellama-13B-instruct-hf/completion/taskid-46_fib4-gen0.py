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


    fib4s = {0: 0, 1: 0, 2: 2, 3: 0}
    fib4s[4] = 4

    def fib4(n: int) -> int:
        if n in fib4s:
            return fib4s[n]
        else:
            fib4s[n] = fib4(n - 1) + fib4(n - 2) + fib4(n - 3) + fib4(n - 4)
            return fib4s[n]

    return fib4(n)
