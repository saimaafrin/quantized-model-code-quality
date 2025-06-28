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

    cur_sum = min_sum = sum(nums)
    for i in range(len(nums) - 1):
        cur_sum += nums[i]
        min_sum = min(min_sum, cur_sum)
        cur_sum -= nums[i + 1]
    return min_sum
