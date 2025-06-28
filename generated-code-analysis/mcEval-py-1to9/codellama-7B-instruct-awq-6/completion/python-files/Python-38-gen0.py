from typing import List
def min_remaining_space(V: int, n: int, volumes: List[int]) -> int:
    """
    Calculate the minimum remaining space in a box after trying to fit a number of items with given volumes.
    
    This function uses a dynamic programming approach to determine the maximum volume that can be occupied
    in the box by any subset of the given items. It then returns the difference between the box's total capacity
    and this maximum occupied volume, which is the minimum remaining space.

    Args:
    - V (int): The total capacity of the box.
    - n (int): The number of items to consider for packing into the box.
    - volumes (List[int]): A list of the volumes of the n items.

    Returns:
    - int: The minimum remaining space in the box after fitting the items.

    Examples:
    - min_remaining_space(24, 6, [8, 3, 12, 7, 9, 7]) -> 0
    - min_remaining_space(5, 3, [6, 7, 8]) -> 5

    """
    # Initialize the maximum volume array with the values from the given volumes.
    max_vol = [0] * n
    max_vol[0] = volumes[0]
    for i in range(1, n):
        max_vol[i] = max(max_vol[i-1], volumes[i])
    # Initialize the maximum volume array with the values from the given volumes.
    max_vol_i = [0] * n
    max_vol_i[n-1] = volumes[n-1]
    for i in range(n-2, -1, -1):
        max_vol_i[i] = max(max_vol_i[i+1], volumes[i])

    # Initialize the dp array with the values from the given volumes.
    dp = [0] * n
    dp[n-1] = volumes[n-1]
    for i in range(n-2, -1, -1):
        dp[i] = max(dp[i+1], volumes[i])

    # Initialize the result array with the values from the given volumes.
    result = [0] * n
    result[n-1] = volumes[n-1]
    for i in range(n-2, -1, -1):
        result[i] = max(result[i+1], volumes[i])

    # Initialize the volume array with the values from the given volumes.
    volume = [0] * n
    volume[n-1] = volumes[n-1]
    for i in range(n-2, -1, -1):
        volume[i] = max(volume[i+1], volumes[i])

    # Iterate through the items.
    for i in range(n-2, -1, -1):
        # Check if the current volume is smaller than the previous volume.
        if volume[i] < volume[i+1]:
            # Check if the current dp array value is smaller than the previous dp array value.
            if dp[i] < dp[i+1]:
                # Set the dp array value to the maximum of the dp array value and the current volume.
                dp[i] = max(dp[i], volume[i])
            else:
                # Set the dp array value to the maximum of the dp array value and the previous volume.
                dp[i] = max(dp[i], volume[i+1])
        else:
            # Check if the current dp array value is smaller than the previous dp array value.
            if dp[i] < dp[i+1]:
                # Set the dp array value to the maximum of the dp array value and the current volume.
                dp[i] = max(dp[i], volume[i])
            else:
                # Set the dp array value to the maximum of the dp array value and the previous volume.
                dp[i] = max(dp[i], volume[i+1])

        # Check if the current dp array value is smaller than the maximum volume.
        if dp[i] < max_vol[i]:
            # Set the dp array
def test_min_remaining_space():
    # Test case 1: Sample provided in the problem statement where all items can fit perfectly
    V1, n1 = 24, 6
    volumes1 = [8, 3, 12, 7, 9, 7]
    expected1 = 0
    assert min_remaining_space(V1, n1,
                               volumes1) == expected1, f"Test case 1 failed: expected {expected1}, got {min_remaining_space(V1, n1, volumes1)}"

    # Test case 2: Some space is expected to remain in the box
    V2, n2 = 10, 4
    volumes2 = [3, 5, 3, 2]
    expected2 = 0  # Possible packing: 3, 5, and 3, leaves 2 units of space
    assert min_remaining_space(V2, n2,
                               volumes2) == expected2, f"Test case 2 failed: expected {expected2}, got {min_remaining_space(V2, n2, volumes2)}"

    # Test case 3: No items can fit due to the items being larger than the box capacity
    V3, n3 = 5, 3
    volumes3 = [6, 7, 8]
    expected3 = 5  # No items fit, so all 5 units of space remain
    assert min_remaining_space(V3, n3,
                               volumes3) == expected3, f"Test case 3 failed: expected {expected3}, got {min_remaining_space(V3, n3, volumes3)}"

    # If all tests pass, print this:
    print("All test cases passed!")


# Run the test function
test_min_remaining_space()