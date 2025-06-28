from typing import List

def by_length(arr: List[int]) -> List[str]:
    """
    Given an array of integers, sort the integers that are between 1 and 9 inclusive,
    reverse the resulting array, and then replace each digit by its corresponding name from
    "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine".

    For example:
    >>> by_length([2, 1, 1, 4, 5, 8, 2, 3])
    ['Eight', 'Five', 'Four', 'Three', 'Two', 'Two', 'One', 'One']
    
      If the array is empty, return an empty array:
    >>> by_length([])
    []
    
      If the array has any strange number ignore it:
    >>> by_length([1, -1, 55])
    ['One']
    """

    temp = []
    for i in arr:
        if i in range(1, 10):
            temp.append(i)
    temp.sort()
    temp.reverse()
    temp2 = []
    for i in temp:
        if i == 1:
            temp2.append("One")
        elif i == 2:
            temp2.append("Two")
        elif i == 3:
            temp2.append("Three")
        elif i == 4:
            temp2.append("Four")
        elif i == 5:
            temp2.append("Five")
        elif i == 6:
            temp2.append("Six")
        elif i == 7:
            temp2.append("Seven")
        elif i == 8:
            temp2.append("Eight")
        elif i == 9:
            temp2.append("Nine")
        else:
            pass
    return temp2
