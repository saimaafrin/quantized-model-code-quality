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

    # Check if all elements of the first list are even:
    if all(i % 2 == 0 for i in lst1):
        return "YES"

    # Check if the second list contains only even elements:
    if all(i % 2 == 0 for i in lst2):
        return "NO"

    # Check if there are elements in the second list that are even:
    even_in_lst2 = [i for i in lst2 if i % 2 == 0]
    if not even_in_lst2:
        return "NO"

    # Make a list of the even elements of the second list:
    even_elements = [i for i in even_in_lst2 if i % 2 == 0]

    # Check if the second list has the same number of even elements
    # as the first list:
    if len(lst1) == len(even_elements):
        return "YES"

    # Check if there is enough elements in the second list:
    if len(lst1) > len(even_elements):
        return "NO"

    # Make a list of the odd elements of the first list:
    odd_elements = [i for i in lst1 if i % 2 != 0]

    # Check if there are elements in the second list that can
    # be used to make the first list even:
    if odd_elements and even_elements:
        return "YES"

    # Check if there are enough elements in the second list:
    if len(lst1) > len(lst2):
        return "NO"

    # If the first list has only odd elements, check if there
    # are enough elements in the second list:
    if not odd_elements:
        if len(lst1) > len(lst2):
            return "NO"
        return "YES"

    # Make a list of the even elements of the first list:
    even_elements = [i for i in lst1 if i % 2 == 0]

    # Check if the second list has enough elements to make
    # the first list even:
    if len(lst1) > len(even_elements):
        return "NO"

    return "YES"
