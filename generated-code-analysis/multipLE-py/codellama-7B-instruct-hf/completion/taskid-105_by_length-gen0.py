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

    if len(arr) == 0: return []
    arr.sort()
    arr.reverse()
    arr = map(lambda x: str(x), arr)
    arr = map(lambda x: "One" if x == "1" else "Two" if x == "2" else "Three" if x == "3" else "Four" if x == "4" else "Five" if x == "5" else "Six" if x == "6" else "Seven" if x == "7" else "Eight" if x == "8" else "Nine" if x == "9" else "Ten", arr)
    return list(arr)
