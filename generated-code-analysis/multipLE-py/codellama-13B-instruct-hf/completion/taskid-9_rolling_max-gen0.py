from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """

    result: List[int] = []

    for i in range(0, len(numbers)):
        if not result:
            result.append(numbers[i])
            continue
        
        if numbers[i] > result[-1]:
            result.append(numbers[i])
            continue
        result.append(result[-1])
    
    return result
