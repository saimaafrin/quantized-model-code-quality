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

    min_sum = 1000000000
    start = 0
    end = 0
    sum_num = 0
    for i in range(len(nums)):
        end = i
        sum_num += nums[end]
        while sum_num >= 0:
            min_sum = min(min_sum, sum_num)
            sum_num -= nums[start]
            start += 1
    return min_sum
