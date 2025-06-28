from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """

    max_value: int = numbers[0]
    result: List[int] = []

    for num in numbers:
        max_value = max(num, max_value)
        result.append(max_value)

    return result
