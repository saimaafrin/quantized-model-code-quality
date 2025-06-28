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

    ### Canonical solution
    #
    # We can simply multiply the two fractions and check if the result is an integer.
    #
    # Let's create a helper function for that:
    def multiply_fractions(a: str, b: str) -> str:
        """Multiply two fractions."""
        num_a, denom_a = map(int, a.split('/'))
        num_b, denom_b = map(int, b.split('/'))
        return f'{num_a * num_b}/{denom_a * denom_b}'

    # Now we can simply multiply the fractions and check if the result is an integer:
    result = multiply_fractions(x, n)
    return '/' not in result
    ### /Canonical solution

    ### Clever solution
    #
    # You can also do this in one line by using a list comprehension:
    return all(i % 1 == 0 for i in [eval(x)*eval(n)])
    ### /Clever solution

    ### Pythonic solution
    #
    # And in one line using Python's `eval` built-in function:
    return eval(x)*eval(n) % 1 == 0
    ### /Pythonic solution
