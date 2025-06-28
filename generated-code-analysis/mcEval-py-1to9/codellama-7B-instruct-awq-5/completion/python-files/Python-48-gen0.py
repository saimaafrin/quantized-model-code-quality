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
    if n == 1:
        return 1

    # Sort the list of prices from least expensive to most expensive.
    # The goal is to pair the most expensive souvenir with the cheapest.
    # This ensures that the group with the most expensive souvenir has a smaller contribution to the group's price.
    prices.sort()

    # A list to keep track of the sum of the prices in each group.
    # A group's price is calculated by summing the prices of all the souvenirs in the group.
    prices_sum = [0] * (n // 2 + 1)

    # Keep track of the minimum number of groups required.
    min_groups_required = n // 2

    # Iterate over the list of prices.
    for i in range(n):
        # The index of the current group.
        group = i // 2

        # The current group's price.
        group_price = prices[i]

        # If the current group's price plus the price of the next souvenir is less than or equal to the maximum price,
        # then add the price of the next souvenir to the current group's price.
        # Otherwise, start a new group and add the current group's price to the list of prices for the new group.
        if group_price + prices[i + 1] <= w:
            prices_sum[group] += prices[i + 1]
        else:
            min_groups_required += 1
            prices_sum.append(group_price)

    return min_groups_required
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