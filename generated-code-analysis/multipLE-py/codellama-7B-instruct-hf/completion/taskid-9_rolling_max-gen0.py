from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """

    rolling = []
    max_ = None

    for num in numbers:
        if max_ is None:
            max_ = num
            rolling.append(num)
        else:
            if num > max_:
                rolling.append(num)
            else:
                rolling.append(max_)
            max_ = max(max_, num)

    return rolling
