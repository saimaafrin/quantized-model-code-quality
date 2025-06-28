from typing import Union

def compare_one(a: Union[int, float, str], b: Union[int, float, str]) -> Union[int, float, str, None]:
    """
    Create a function that takes integers, floats, or strings representing
    real numbers, and returns the larger variable in its given variable type.
    Return None if the values are equal.
    Note: If a real number is represented as a string, the floating point might be . or ,

    >>> compare_one(1, 2.5)
    2.5
    >>> compare_one(1, '2,3')
    '2,3'
    >>> compare_one('5,1', '6')
    '6'
    >>> compare_one('1', 1)
    None
    """


    # check if equal
    if a == b:
        return None

    # check if string
    if type(a) == str and type(b) == str:
        # check if a is bigger
        if a.replace(',','.') > b.replace(',','.'):
            return a
        # check if b is bigger
        else:
            return b

    # check if int/float
    if type(a) == int and type(b) == int:
        # check if a is bigger
        if a > b:
            return a
        # check if b is bigger
        else:
            return b

    if type(a) == float and type(b) == float:
        # check if a is bigger
        if a > b:
            return a
        # check if b is bigger
        else:
            return b

    raise TypeError("Invalid argument types")
