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

    cur_sum = min_sum = nums[0]
    for num in nums[1:]:
        cur_sum = min(num, cur_sum + num)
        min_sum = min(min_sum, cur_sum)
    return min_sum
