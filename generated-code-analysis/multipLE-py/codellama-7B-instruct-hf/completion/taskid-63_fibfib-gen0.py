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

    # The FibFib sequence can be found here https://oeis.org/A001982
    if n == 0:
        return 0
    if n == 1:
        return 0
    if n == 2:
        return 1
    if n == 3:
        return 1
    if n == 4:
        return 3
    return fibfib(n-1) + fibfib(n-2) + fibfib(n-3)
