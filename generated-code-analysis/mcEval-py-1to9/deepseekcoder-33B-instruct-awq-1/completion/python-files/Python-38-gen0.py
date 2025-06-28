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
    # Create a boolean array to store the maximum volume that can be occupied in the box
    # by any subset of the items up to the current item.
    subset = [False]*(V + 1)

    # Set the first item as True, since it can occupy the box with its own volume.
    subset[volumes[0]] = True

    # Traverse the remaining items.
    for i in range(1, n):
        # Create a temporary array to store the maximum volume that can be occupied in the box
        # by any subset of the items up to the current item.
        temp = subset[:]

        # Traverse the volumes.
        for v in range(1, V + 1):
            # If the current item can fit in the box, update the maximum volume that can be occupied
            # by any subset of the items up to the current item.
            if v >= volumes[i]:
                temp[v] = subset[v] or subset[v - volumes[i]]

        # Update the maximum volume that can be occupied by any subset of the items up to the current item.
        subset = temp

    # Traverse the maximum volumes that can be occupied by any subset of the items.
    for v in range(V, -1, -1):
        if subset[v]:
            # Return the difference between the box's total capacity and the maximum volume that can be occupied
            # by any subset of the items.
            return V - v

    # If no items can fit in the box, return the total capacity of the box.
    return V
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