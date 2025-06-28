def hex_key(num: str) -> int:
    """You have been tasked to write a function that receives 
    a hexadecimal number as a string and counts the number of hexadecimal 
    digits that are primes (prime number, or a prime, is a natural number 
    greater than 1 that is not a product of two smaller natural numbers).
    Hexadecimal digits are 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E, F.
    Prime numbers are 2, 3, 5, 7, 11, 13, 17,...
    So you have to determine a number of the following digits: 2, 3, 5, 7, 
    B (=decimal 11), D (=decimal 13).
    Note: you may assume the input is always correct or empty string, 
    and symbols A,B,C,D,E,F are always uppercase.
    Examples:
    >>> hex_key('AB')
    1
    >>> hex_key('1077E')
    2
    >>> hex_key('ABED1A33')
    4
    >>> hex_key('123456789ABCDEF0')
    6
    >>> hex_key('2020')
    2
    """

    primes = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97}
    hex_dict = {'0': 0, '1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0,
                'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0}

    for digit in num:
        if digit in hex_dict:
            hex_dict[digit] += 1

    count = 0
    for value in hex_dict.values():
        if value in primes:
            count += 1

    return count
