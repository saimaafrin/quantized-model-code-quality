def min_groups(w, n, prices):
    """
    Determines the minimum number of groups needed to distribute souvenirs with a constraint on the group's total price.
    
    The souvenirs are grouped in pairs such that the total price of each group does not exceed the limit `w`. 
    The function aims to minimize the number of groups created under this constraint.
    
    Args:
    w (int): The maximum allowed sum of prices for any group of souvenirs.
    n (int): The total number of souvenirs.
    prices (list): A list of integers representing the price of each souvenir.
    
    Returns:
    int: The minimum number of groups required to distribute all souvenirs.

    Examples:
    >>> min_groups(100, 9, [90, 20, 20, 30, 50, 60, 70, 80, 90])
    6
    >>> min_groups(80, 4, [30, 30, 20, 10])
    2
    """
    prices.sort(reverse=True)  # Sort prices in descending order
    i, j = 0, n-1  # Initialize pointers for the start and end of the prices list
    count = 0  # Initialize count of groups

    # Group souvenirs in pairs
    while i <= j:
        if prices[i] + prices[j] <= w:  # Check if current group can fit within the limit w
            i += 1  # Increase start pointer
            j -= 1  # Decrease end pointer
        else:
            i += 1  # If current group exceeds limit, only increase start pointer
        count += 1  # Increment group count

    return count
def test_min_groups():
    # Test case 1
    w1 = 100
    n1 = 9
    prices1 = [90, 20, 20, 30, 50, 60, 70, 80, 90]
    expected_output1 = 6
    assert min_groups(w1, n1, prices1) == expected_output1, "Test case 1 failed"

    # Test case 2
    w2 = 200
    n2 = 5
    prices2 = [80, 120, 60, 40, 100]
    expected_output2 = 3
    assert min_groups(w2, n2, prices2) == expected_output2, "Test case 2 failed"

    # Test case 3
    w3 = 80
    n3 = 4
    prices3 = [30, 30, 20, 10]
    expected_output3 = 2
    assert min_groups(w3, n3, prices3) == expected_output3, "Test case 3 failed"

    print("All test cases passed!")

# Run the test function
test_min_groups()