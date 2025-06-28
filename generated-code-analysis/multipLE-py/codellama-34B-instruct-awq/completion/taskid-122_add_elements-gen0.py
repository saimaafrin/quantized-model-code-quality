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

    # Time: O(n); Space: O(1)
    # Two pointers
    # Maintain a window of size k to check the number of digits
    # and the sum of the elements with at most two digits
    n = len(arr)

    # Edge case
    if k == n:
        return sum([x for x in arr if 9 < x < 100])

    # Initialize the window
    window = [arr[0]]
    sum_of_elements = arr[0]
    for i in range(1, k):
        window.append(arr[i])
        if 9 < arr[i] < 100:
            sum_of_elements += arr[i]
    result = sum_of_elements

    # Maintain the window
    for i in range(k, n):
        for j in range(len(window)):
            if window[j] == arr[i-k+j]:
                if 9 < window[j] < 100:
                    sum_of_elements -= window[j]
                window[j] = arr[i]
                if 9 < arr[i] < 100:
                    sum_of_elements += arr[i]
                break

        result = max(result, sum_of_elements)

    return result
