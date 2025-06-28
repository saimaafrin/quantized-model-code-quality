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

    binary_num = bin(N)[2:]  # Convert to binary and remove the '0b' prefix
    total_sum = sum(int(digit) for digit in binary_num)
    return bin(total_sum)[2:]  # Convert back to binary and remove the '0b' prefix
