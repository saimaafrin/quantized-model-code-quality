from typing import List

def exchange(lst1: List[int], lst2: List[int]) -> str:
    """In this problem, you will implement a function that takes two lists of numbers,
    and determines whether it is possible to perform an exchange of elements
    between them to make lst1 a list of only even numbers.
    There is no limit on the number of exchanged elements between lst1 and lst2.
    If it is possible to exchange elements between the lst1 and lst2 to make
    all the elements of lst1 to be even, return "YES".
    Otherwise, return "NO".
    For example:
    >>> exchange([1, 2, 3, 4], [1, 2, 3, 4])
    'YES'
    >>> exchange([1, 2, 3, 4], [1, 5, 3, 4])
    'NO'
    It is assumed that the input lists will be non-empty.
    """

    # Split the lists into odd and even numbers
    lst1_odd, lst1_even = partition_by_parity(lst1)
    lst2_odd, lst2_even = partition_by_parity(lst2)

    # If the number of odd numbers in lst1_even is more than the number of even numbers in lst2_odd,
    # then it is impossible to make lst1 a list of only even numbers by exchanging numbers.
    if len(lst1_even) > len(lst2_odd):
        return 'NO'

    # If the number of odd numbers in lst1_odd is more than the number of even numbers in lst2_even,
    # then it is impossible to make lst1 a list of only even numbers by exchanging numbers.
    if len(lst1_odd) > len(lst2_even):
        return 'NO'

    # If it is possible to make lst1 a list of only even numbers by exchanging numbers,
    # return "YES"
    return 'YES'
