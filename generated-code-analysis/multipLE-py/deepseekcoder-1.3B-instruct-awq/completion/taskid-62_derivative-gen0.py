from typing import List

def derivative(xs: List[int]) -> List[int]:
    """ xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 + ....
     Return derivative of this polynomial in the same form.
    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    """

    def helper(xs, index):
        if index == len(xs) - 1:
            return [0]
        return [index * xs[index + 1] for index in range(index + 1)]

    derivatives = [1]
    for index in range(len(xs) - 1):
        derivatives.extend(helper(xs, index))

    return derivatives
