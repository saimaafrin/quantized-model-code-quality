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

    import math
    x_num, x_den = map(int, x.split('/'))
    n_num, n_den = map(int, n.split('/'))

    common_den = x_den * n_den
    new_num = x_num * n_num

    # Find the greatest common divisor of the new numerator and the common denominator
    gcd = math.gcd(new_num, common_den)

    # The expression x * n simplifies if the numerator divided by the greatest common divisor equals a whole number
    return (new_num / gcd).is_integer()
