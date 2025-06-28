def solve(N: int) -> str:
    """Given a positive integer N, return the total sum of its digits in binary.
    
    Example
    >>> solve(1000)
    '1'
    >>> solve(150)
    '110'
    >>> solve(147)
    '1100'
    
    Variables:
        @N integer
             Constraints: 0 ≤ N ≤ 10000.
    Output:
         a string of binary number
    """

    if N == 0:
        return "0"
    sum_bin = "0"
    while N > 0:
        N, remainder = divmod(N, 2)
        sum_bin += str(remainder)
    return sum_bin
