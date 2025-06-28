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
    # Create a DP table of size (n+1) x (V+1) and initialize all elements to False
    dp = [[False]*(V+1) for _ in range(n+1)]
    
    # If the volume of the box is 0, it's always possible to fit items such that the volume remaining is 0
    for i in range(n+1):
        dp[i][0] = True
    
    # Iterate over the items and their volumes
    for i in range(1, n+1):
        for v in range(1, V+1):
            # If the volume of the current item is greater than the current volume,
            # we can't fit the item into the box, so we inherit the previous solution
            if volumes[i-1] > v:
                dp[i][v] = dp[i-1][v]
            else:
                # If we can fit the item into the box, we can either fit it or not fit it
                # If either is possible, we have a solution
                dp[i][v] = dp[i-1][v] or dp[i-1][v-volumes[i-1]]
    
    # Find the maximum volume we can fit into the box
    max_volume = next((v for v in range(V, -1, -1) if dp[n][v]), 0)
    
    # Return the minimum remaining space in the box after fitting the items
    return V - max_volume
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