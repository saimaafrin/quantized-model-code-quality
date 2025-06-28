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


    count = 0
    even_nums = [2, 4, 6, 8, 10]
    for num in lst1:
        if num not in even_nums:
            count += 1

    if len(lst2) < count:
        return 'NO'

    lst2_copy = lst2[:]
    for num in lst1:
        if num not in even_nums:
            if num in lst2_copy:
                lst2_copy.remove(num)
            else:
                return 'NO'

    return 'YES'
