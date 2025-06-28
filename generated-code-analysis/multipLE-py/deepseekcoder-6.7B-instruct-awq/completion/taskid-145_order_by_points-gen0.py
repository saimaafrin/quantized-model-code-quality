from typing import List

def order_by_points(nums: List[int]) -> List[int]:
    """
    Write a function which sorts the given list of integers
    in ascending order according to the sum of their digits.
    Note: if there are several items with similar sum of their digits,
    order them based on their index in original list.

    For example:
    >>> order_by_points([1, 11, -1, -11, -12])
    [-1, -11, 1, -12, 11]
    >>> order_by_points([])
    []
    """

    nums_with_indices = [(i, num) for i, num in enumerate(nums)]
    nums_with_points = [(num, sum(int(digit) for digit in str(abs(num)))) for num in nums]
    nums_with_points_and_indices = sorted(nums_with_points, key=lambda x: (x[1], x[0]))
    sorted_nums = [num for _, num in sorted(nums_with_points_and_indices, key=lambda x: x[1])]
    return sorted_nums
