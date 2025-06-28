def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """

    xor_bin = int(a, 2) ^ int(b, 2)
    return format(xor_bin, '0' + str(max(len(a), len(b))) + 'b')
