from typing import List 
def polynomial_to_string(n: int, coeffs: List[int]) -> str:
    """
    Converts a list of polynomial coefficients into a formatted string representation.

    The function takes in the highest degree `n` of the polynomial and a list of coefficients `coeffs`,
    which are ordered from the highest degree term to the constant term. It returns a string that
    represents the polynomial with the following rules:
    - Terms with a coefficient of zero are omitted.
    - The sign of each term is determined (+ for positive, - for negative), with no leading '+' for the first term.
    - The absolute value of the coefficient is shown unless it's 1 and the term includes the variable `x`.
    - The variable part is formatted based on its degree; `x^degree` for degree > 1, `x` for degree 1, and
      nothing for degree 0 (constant term).
    - Terms are joined without additional spaces, starting with the highest degree term.

    Args:
        n (int): The highest degree of the polynomial.
        coeffs (List[int]): A list of coefficients, starting with the coefficient of the highest degree term.

    Returns:
        str: The string representation of the polynomial.

    Examples:
        >>> polynomial_to_string(5, [100, -1, 1, -3, 0, 10])
        '100x^5-x^4+x^3-3x^2+10'

        >>> polynomial_to_string(3, [-50, 0, 0, 1])
        '-50x^3+1'
    """
    # convert the coefficient list to a list of tuples, with each tuple containing the coeff and the degree
    coeff_degree_pairs = [(c, i) for i, c in enumerate(coeffs, 1)]
    # filter out the terms with zero coeff
    nonzero_coeffs_degree_pairs = filter(lambda t: t[0] != 0, coeff_degree_pairs)
    # convert the pairs back to a list of tuples
    nonzero_coeffs_degree_pairs = list(nonzero_coeffs_degree_pairs)
    # reverse the list so that the highest degree terms are printed first
    nonzero_coeffs_degree_pairs.reverse()

    result = ''
    for coeff, degree in nonzero_coeffs_degree_pairs:
        # get the sign of the term
        sign = '+' if coeff > 0 else '-'
        # get the absolute value of the coefficient
        abs_coeff = abs(coeff)
        # get the variable part of the term
        var_part = 'x^' + str(degree) if degree > 1 else ('x' if degree == 1 else '')
        # get the coefficient part of the term
        coeff_part = '' if abs_coeff == 1 and degree > 0 else str(abs_coeff)

        result += sign + coeff_part + var_part

    return result[1:]
def test_polynomial_to_string():
    test_cases = [
        (4, [3, -2, 0, 1, -5], "3x^4-2x^3+x-5"),
        (2, [0, 4, -1], "+4x-1"),
        (0, [7], "7"),
        (3, [1, -1, 0, 1], "x^3-x^2+1"),
    ]

    for i, (n, coeffs, expected) in enumerate(test_cases):
        result = polynomial_to_string(n, coeffs)

        assert result == expected, f"Test case {i + 1} failed: expected {expected}, got {result}"
        print(f"Test case {i + 1} passed: expected {expected}, got {result}")


test_polynomial_to_string()