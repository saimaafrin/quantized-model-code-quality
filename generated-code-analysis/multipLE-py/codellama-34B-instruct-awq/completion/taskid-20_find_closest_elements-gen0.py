from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """

    # Sort list in ascending order
    numbers.sort()
    # Initialise closest_so_far and closest_pair
    closest_so_far = abs(numbers[0] - numbers[1])
    closest_pair = (numbers[0], numbers[1])
    # Loop through remaining numbers
    for i in range(len(numbers) - 1):
        # Calculate difference between current number and next number
        difference = abs(numbers[i] - numbers[i + 1])
        # If difference is less than closest_so_far, replace closest_so_far and closest_pair
        if difference < closest_so_far:
            closest_so_far = difference
            closest_pair = (numbers[i], numbers[i + 1])
    # Return closest_pair
    return closest_pair
