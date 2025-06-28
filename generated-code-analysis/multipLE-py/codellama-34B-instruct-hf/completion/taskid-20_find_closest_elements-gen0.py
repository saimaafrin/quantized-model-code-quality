from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """

    # Sort the list in place
    numbers.sort()
    # Set the initial closest gap
    closest_gap = 1e10
    # Set the initial closest pair
    closest_pair = (0.0, 0.0)
    # Walk the sorted list
    for i in range(len(numbers) - 1):
        # Calculate the absolute difference
        gap = abs(numbers[i] - numbers[i+1])
        # If the gap is less than the closest gap
        if gap < closest_gap:
            # Set the new closest gap
            closest_gap = gap
            # Set the new closest pair
            closest_pair = (numbers[i], numbers[i+1])
    # Return the closest pair
    return closest_pair
