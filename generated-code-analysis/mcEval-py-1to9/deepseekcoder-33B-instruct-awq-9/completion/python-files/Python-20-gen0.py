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

    # This list will contain the formatted strings for each term.
    terms = []

    # Iterate over the coefficients from highest to lowest degree.
    for i in range(n, -1, -1):
        # If the coefficient is zero, skip this term.
        if coeffs[i] == 0:
            continue

        # Format the coefficient part of the term.
        # If the coefficient is 1 and the term includes the variable `x`, omit it.
        if coeffs[i] == 1 and i > 0:
            coefficient_part = ""
        elif coeffs[i] == -1 and i > 0:
            coefficient_part = "-"
        else:
            coefficient_part = str(abs(coeffs[i]))

        # Format the variable part of the term.
        # If the degree is 0, omit the variable part.
        # If the degree is 1, just include the variable `x`.
        # If the degree is > 1, include the variable `x^degree`.
        if i == 0:
            variable_part = ""
        elif i == 1:
            variable_part = "x"
        else:
            variable_part = "x^" + str(i)

        # Add the formatted term to the list of terms.
        terms.append(coefficient_part + variable_part)

    # Join the terms with '+' between them, omitting the '+' before the first term.
    return "+".join(terms)
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