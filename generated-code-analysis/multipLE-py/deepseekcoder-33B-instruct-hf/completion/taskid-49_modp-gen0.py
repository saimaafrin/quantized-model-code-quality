def modp(n: int, p: int) -> int:
    """Return 2^n modulo p (be aware of numerics).
    >>> modp(3, 5)
    3
    >>> modp(1101, 101)
    2
    >>> modp(0, 101)
    1
    >>> modp(3, 11)
    8
    >>> modp(100, 101)
    1
    """

    if n < 0:
        raise ValueError("n must be nonnegative.")
    if p < 1:
        raise ValueError("p must be positive.")
    r = 1
    for _ in range(n):
        r = (r << 1) % p
    return r
