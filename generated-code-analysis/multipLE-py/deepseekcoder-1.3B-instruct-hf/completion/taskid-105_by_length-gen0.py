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

    # filter out the numbers that are not between 1 and 9
    arr = [x for x in arr if 1 <= x <= 9]
    
    # sort the array first by length, then by value
    arr.sort(key=lambda x: (len(str(x)), x))

    # map each number to its corresponding name
    arr = list(map(lambda x: ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine'][x - 1], arr))

    # reverse the array
    arr = arr[::-1]

    return arr
