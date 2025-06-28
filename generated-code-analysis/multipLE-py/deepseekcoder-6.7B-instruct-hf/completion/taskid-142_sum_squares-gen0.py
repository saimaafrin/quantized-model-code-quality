from typing import List

def sum_squares(lst: List[int]) -> int:
    """"
    This function will take a list of integers. For all entries in the list, the function shall square the integer entry if its index is a 
    multiple of 3 and will cube the integer entry if its index is a multiple of 4 and not a multiple of 3. The function will not 
    change the entries in the list whose indexes are not a multiple of 3 or 4. The function shall then return the sum of all entries. 
    
    Examples:
    >>> lst
    [1, 2, 3]
    >>> lst
    []
    >>> lst
    [-1, -5, 2, -1, -5]
    """

    sum_total = 0
    for index in range(len(lst)):
        if index % 3 == 0 and index % 4 != 0:
            sum_total += lst[index] ** 2
        elif index % 4 == 0:
            sum_total += lst[index] ** 3
        else:
            sum_total += lst[index]
    return sum_total
