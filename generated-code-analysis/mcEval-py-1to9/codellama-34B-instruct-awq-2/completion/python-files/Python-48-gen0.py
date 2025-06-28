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
    # Sort the prices in descending order
    prices.sort(reverse=True)
    # Initialise the number of groups and total price of each group
    groups = 0
    group_total = 0
    # Loop through the prices
    for i in range(n):
        # If the group has not yet reached the maximum total price and the current price does not exceed the maximum price
        if group_total + prices[i] <= w and group_total + prices[i] <= w:
            # Add the price to the group total
            group_total += prices[i]
        else:
            # If the group has reached the maximum total price, create a new group
            groups += 1
            group_total = prices[i]
    # Return the number of groups needed to distribute all souvenirs
    return groups + 1
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