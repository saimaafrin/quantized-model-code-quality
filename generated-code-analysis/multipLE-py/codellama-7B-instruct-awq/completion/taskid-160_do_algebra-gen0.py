from typing import List

def do_algebra(operator: List[str], operand: List[int]) -> int:
    """
    Given two lists operator, and operand. The first list has basic algebra operations, and 
    the second list is a list of integers. Use the two given lists to build the algebric 
    expression and return the evaluation of this expression.

    The basic algebra operations:
    Addition ( + ) 
    Subtraction ( - ) 
    Multiplication ( * ) 
    Floor division ( // ) 
    Exponentiation ( ** ) 

    Example:
    operator['+', '*', '-']
    array = [2, 3, 4, 5]
    result = 2 + 3 * 4 - 5
    => result = 9

    Note:
        The length of operator list is equal to the length of operand list minus one.
        Operand is a list of of non-negative integers.
        Operator list has at least one operator, and operand list has at least two operands.

    """

    if len(operator) != len(operand) - 1:
        return -1
    result = 0
    for i, value in enumerate(operand):
        if i == 0:
            result += int(value)
        else:
            operation = operator[i-1]
            if operation == '+':
                result += int(value)
            elif operation == '-':
                result -= int(value)
            elif operation == '*':
                result *= int(value)
            elif operation == '//':
                result //= int(value)
            elif operation == '**':
                result **= int(value)
            else:
                return -1
    return result
