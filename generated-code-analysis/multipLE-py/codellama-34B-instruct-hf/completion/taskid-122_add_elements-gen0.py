from typing import List

def add_elements(arr: List[int], k: int) -> int:
    """
    Given a non-empty array of integers arr and an integer k, return
    the sum of the elements with at most two digits from the first k elements of arr.

    Example:

    >>> add_elements([111, 21, 3, 4000, 5, 6, 7, 8, 9], 4)
    24

    Constraints:
        1. 1 <= len(arr) <= 100
        2. 1 <= k <= len(arr)
    """


    # Initialize counter for elements with <= 2 digits
    # Initialize maximum value of element with 2 digits
    counter, max_two_digit = 0, 100

    # Iterate over first k elements of array
    for i in range(k):

        # If element is less than 10, count it
        if arr[i] < 10:
            counter += 1

        # If element is less than 100, update max_two_digit
        elif arr[i] < max_two_digit:
            max_two_digit = arr[i]

    # Initialize result
    result = counter

    # Iterate over rest of the elements
    for i in range(k, len(arr)):

        # If element is greater than max_two_digit, ignore it
        if arr[i] > max_two_digit:
            continue

        # If element is less than 10, count it
        elif arr[i] < 10:
            result += 1

        # If element is less than 100, update max_two_digit
        elif arr[i] < max_two_digit:
            max_two_digit = arr[i]

    return result
