from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """

    max_number = numbers[0]
    max_numbers = []
    for number in numbers:
        max_number = max(max_number, number)
        max_numbers.append(max_number)
    return max_numbers
