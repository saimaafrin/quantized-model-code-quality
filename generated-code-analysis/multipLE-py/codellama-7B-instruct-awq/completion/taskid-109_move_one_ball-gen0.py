from typing import List

def move_one_ball(arr: List[int]) -> bool:
    """We have an array 'arr' of N integers arr[1], arr[2], ..., arr[N].The
    numbers in the array will be randomly ordered. Your task is to determine if
    it is possible to get an array sorted in non-decreasing order by performing 
    the following operation on the given array:
        You are allowed to perform right shift operation any number of times.
    
    One right shift operation means shifting all elements of the array by one
    position in the right direction. The last element of the array will be moved to
    the starting position in the array i.e. 0th index. 

    If it is possible to obtain the sorted array by performing the above operation
    then return True else return False.
    If the given array is empty then return True.

    Note: The given list is guaranteed to have unique elements.

    For Example:
    
    >>> move_one_ball([3, 4, 5, 1, 2])
    True
    Explanation: By performin 2 right shift operations, non-decreasing order can
                 be achieved for the given array.
    >>> move_one_ball([3, 5, 4, 1, 2])
    False
    Explanation:It is not possible to get non-decreasing order for the given
                array by performing any number of right shift operations.
                
    """


    # Solution:
    # It is enough to check if there is a subsequence 
    # in the array which can be sorted in non-decreasing order.
    # A subsequence can be sorted in non-decreasing order if there is a subarray
    # that can be sorted in non-decreasing order.

    # Example: If the array is [4,5,2,1,3], then we can get the
    # subsequence [1,2,3] and it can be sorted in non-decreasing order.

    # Thus, we can check if there is a subsequence that can be sorted in
    # non-decreasing order.
    # If there is such a subsequence then we can return True else False.

    # Time Complexity: O(n) where n is the length of the given array.
    # Space Complexity: O(1)

    # Code:
    if not arr:
        return True
    arr.sort()
    return arr == list(reversed(arr))
