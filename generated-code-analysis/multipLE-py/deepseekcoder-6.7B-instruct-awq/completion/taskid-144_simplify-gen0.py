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


    import fractions
    x_num, x_den = map(int, x.split('/'))
    n_num, n_den = map(int, n.split('/'))
    x_frac = fractions.Fraction(x_num, x_den)
    n_frac = fractions.Fraction(n_num, n_den)
    result = x_frac * n_frac
    return result.numerator % result.denominator == 0
