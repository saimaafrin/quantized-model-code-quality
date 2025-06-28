from typing import List

def minSubArraySum(nums: List[int]) -> int:
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    >>> minSubArraySum([2, 3, 4, 1, 2, 4])
    1
    >>> minSubArraySum([-1, -2, -3])
    -6
    """

    current_min = nums[0]
    min_sum = nums[0]
    for num in nums[1:]:
        current_min = min(num, current_min + num)
        min_sum = min(current_min, min_sum)
    return min_sum
