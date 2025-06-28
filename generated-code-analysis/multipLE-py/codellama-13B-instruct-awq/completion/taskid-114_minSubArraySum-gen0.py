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

    n = len(nums)
    minSum = float('inf')
    windowSum = 0
    for i in range(n):
        windowSum += nums[i]
        for j in range(i + 1, n):
            windowSum += nums[j]
            minSum = min(minSum, windowSum)
            windowSum -= nums[j]

    return minSum
