def fibfib(n: int) -> int:
    """The FibFib number sequence is a sequence similar to the Fibbonacci sequnece that's defined as follows:
    fibfib(0) == 0
    fibfib(1) == 0
    fibfib(2) == 1
    fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3).
    Please write a function to efficiently compute the n-th element of the fibfib number sequence.
    >>> fibfib(1)
    0
    >>> fibfib(5)
    4
    >>> fibfib(8)
    24
    """

    if n == 0 or n == 1:
        return 0
    elif n == 2:
        return 1

    fibfib_sequence = [0, 0, 1] + [0] * (n-3)
    for i in range(3, n):
        fibfib_sequence[i] = fibfib_sequence[i-1] + fibfib_sequence[i-2] + fibfib_sequence[i-3]
    return fibfib_sequence[-1]
