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

    # check if the list is empty
    if not lst:
        return 0

    # initialize the sum
    lst_sum = 0

    # iterate through the list
    for i, val in enumerate(lst):
        # square value if index is a multiple of 3
        if i % 3 == 0:
            val **= 2
        # cube value if index is a multiple of 4 and not a multiple of 3
        elif i % 4 == 0:
            val **= 3
        # add the value to the sum
        lst_sum += val

    return lst_sum
