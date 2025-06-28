from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    """ For a given list of input numbers, calculate Mean Absolute Deviation
    around the mean of this dataset.
    Mean Absolute Deviation is the average absolute difference between each
    element and a centerpoint (mean in this case):
    MAD = average | x - x_mean |
    >>> mean_absolute_deviation([1.0, 2.0, 3.0, 4.0])
    1.0
    """

    # Check that input is a list
    if type(numbers) != list:
        raise ValueError("Input should be a list")
    # Check if list is not empty
    if len(numbers) == 0:
        raise ValueError("Input list should not be empty")
    # Calculate mean
    mean = sum(numbers) / len(numbers)
    # Calculate MAD
    return sum(abs(mean - x) for x in numbers) / len(numbers)
