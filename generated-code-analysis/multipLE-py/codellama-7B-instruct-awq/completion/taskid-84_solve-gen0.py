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

    if N < 2:
        return str(N)
    else:
        if N % 2 == 0:
            return str(N % 2) + solve(N // 2)
        else:
            return '1' + solve(N // 2)
