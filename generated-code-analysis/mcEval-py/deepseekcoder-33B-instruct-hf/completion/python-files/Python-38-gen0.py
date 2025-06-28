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
    # Create a matrix to hold the maximum volumes that can be obtained by packing the items up to each index
    max_volumes = [[0] * (V + 1) for _ in range(n + 1)]
    
    # For each item
    for i in range(1, n + 1):
        # For each possible volume
        for v in range(V + 1):
            # If the volume of the current item is less than or equal to the current volume
            if volumes[i - 1] <= v:
                # Consider packing the current item
                # If packing the current item increases the maximum volume, update the max_volumes matrix
                max_volumes[i][v] = max(
                    max_volumes[i - 1][v],  # not packing the current item
                    volumes[i - 1] + max_volumes[i - 1][v - volumes[i - 1]]  # packing the current item
                )
            else:
                # If the volume of the current item is more than the current volume, don't pack the current item
                max_volumes[i][v] = max_volumes[i - 1][v]
    
    # The minimum remaining space is the difference between the box's total capacity and the maximum volume that can be obtained
    min_remaining_space = V - max_volumes[n][V]
    
    return min_remaining_space
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