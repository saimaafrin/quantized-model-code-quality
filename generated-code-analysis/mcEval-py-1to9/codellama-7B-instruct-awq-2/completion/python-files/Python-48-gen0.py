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

    # If there are no souvenirs, return 0.
    if n == 0:
        return 0

    # If the maximum price of the souvenirs does not exceed the limit, return 1.
    if sum(prices) <= w:
        return 1

    # Initialize a list to store the maximum price for each group.
    prices_max = [0] * (n + 1)

    # Initialize a list to store the minimum number of groups for each group size.
    groups = [float('inf')] * (n + 1)

    # The first group can have at most n - 1 items, and its maximum price is the maximum price of all the items.
    groups[1] = max(prices)
    prices_max[1] = groups[1]

    # For each size of the group, starting from the second group.
    for i in range(2, n + 1):
        # Initialize the maximum price of the current group to 0.
        price_max = 0

        # Initialize the minimum number of groups for the current size to infinity.
        groups[i] = float('inf')

        # For each possible size of the previous group.
        for j in range(1, i):
            # If the sum of the maximum price of the previous group and the price of the item is less than or equal to the limit,
            # add the previous group size and the current item to the current group, and update the maximum price of the current group.
            if sum(prices_max[:j]) + prices[i - 1] <= w:
                price_max = max(price_max, sum(prices_max[:j]) + prices[i - 1])
                groups[i] = min(groups[i], j + 1)

        # Store the maximum price of the current group.
        prices_max[i] = price_max

    # Return the minimum number of groups required to distribute all the souvenirs.
    return groups[n]
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