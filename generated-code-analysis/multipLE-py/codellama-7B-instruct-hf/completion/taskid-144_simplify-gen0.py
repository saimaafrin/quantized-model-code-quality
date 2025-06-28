def simplify(x: str, n: str) -> bool:
    """Your task is to implement a function that will simplify the expression
    x * n. The function returns True if x * n evaluates to a whole number and False
    otherwise. Both x and n, are string representation of a fraction, and have the following format,
    <numerator>/<denominator> where both numerator and denominator are positive whole numbers.

    You can assume that x, and n are valid fractions, and do not have zero as denominator.

    >>> simplify('1/5', '5/1')
    True
    >>> simplify('1/6', '2/1')
    False
    >>> simplify('7/10', '10/2')
    False
    """


    def is_whole_number(fraction: str) -> bool:
        return int(fraction.split("/")[0]) == fraction.split("/")[0]

    n = n.split("/")
    x = x.split("/")

    if is_whole_number(x[0]) and is_whole_number(x[1]) and is_whole_number(n[0]) and is_whole_number(n[1]):
        return True
    return False
