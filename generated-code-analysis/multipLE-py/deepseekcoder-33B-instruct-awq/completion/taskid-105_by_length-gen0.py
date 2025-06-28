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

    if len(arr) == 0:
        return []
    else:
        new_arr = []
        for i in arr:
            if i > 0 and i < 10:
                if i == 1:
                    new_arr.append("One")
                elif i == 2:
                    new_arr.append("Two")
                elif i == 3:
                    new_arr.append("Three")
                elif i == 4:
                    new_arr.append("Four")
                elif i == 5:
                    new_arr.append("Five")
                elif i == 6:
                    new_arr.append("Six")
                elif i == 7:
                    new_arr.append("Seven")
                elif i == 8:
                    new_arr.append("Eight")
                elif i == 9:
                    new_arr.append("Nine")
        new_arr.sort(reverse=True)
        return new_arr
