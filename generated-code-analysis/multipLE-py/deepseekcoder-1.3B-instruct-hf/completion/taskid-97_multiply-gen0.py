def multiply(a: int, b: int) -> int:
    """Complete the function that takes two integers and returns 
    the product of their unit digits.
    Assume the input is always valid.
    Examples:
    >>> multiply(148, 412)
    16
    >>> multiply(19, 28)
    72
    >>> multiply(2020, 1851)
    0
    >>> multiply(14, -15)
    20
    """

    def extract_units(n: int) -> int:
        return n % 10
    
    def multiply_by_one(a: int, b: int) -> int:
        return a * b
    
    def sum_of_units(a: int, b: int, base: int) -> int:
        return multiply(a, extract_units(b)) + multiply(b, extract_units(a)) + multiply(extract_units(a), extract_units(b))
    
    if a < 10 or b < 10:
        return multiply_by_one(a, b)
    
    if a == 1 or b == 1:
        return sum_of_units(a, b, 10)
    
    a_units = extract_units(a)
    b_units = extract_units(b)
    
    if a_units == 1 and b_units == 1:
        return sum_of_units(a, b, 10)
    elif a_units == 1:
        return multiply(a, b_units) + multiply(b, extract_units(a))
    elif b_units == 1:
        return multiply(b, a_units) + multiply(a, extract_units(b))
    else:
        return multiply(a, b)
