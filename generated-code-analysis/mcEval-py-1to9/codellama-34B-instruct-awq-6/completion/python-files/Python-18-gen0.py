from typing import List, Tuple
def max_happiness(n: int, m: int, items: List[Tuple[int, int]]) -> int:
    """
    Calculates the maximum total importance value of items that can be bought within a given budget.
    
    This function solves a variant of the 0-1 knapsack problem where each item has a price and an 
    associated importance value. The goal is to maximize the sum of the importance values of a 
    selection of items without the total price exceeding the budget.
    
    Args:
    n (int): The total budget available for purchasing items.
    m (int): The number of different items to choose from.
    items (List[Tuple[int, int]]): A list of tuples, where each tuple contains two integers:
        - The first integer represents the price of the item.
        - The second integer represents the importance value of the item.
    
    Returns:
    int: The maximum total importance value that can be achieved without exceeding the budget.
    
    Examples:
    >>> max_happiness(1000, 5, [(800, 2), (400, 5), (300, 5), (400, 3), (200, 2)])
    3900
    
    >>> max_happiness(50, 3, [(10, 1), (20, 2), (30, 3)])
    80
    """
    # Initialize a 2D array to store the maximum total importance value of each item
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Populate the first row and column of the dp array
    for i in range(m + 1):
        dp[i][0] = 0
    for j in range(n + 1):
        dp[0][j] = 0
    
    # Iterate over the items
    for i in range(1, m + 1):
        price, importance = items[i - 1]
        # Iterate over the budget
        for j in range(1, n + 1):
            # If the current price is less than the budget, calculate the maximum total
            # importance value for the current item and the remaining budget
            if price <= j:
                dp[i][j] = max(dp[i - 1][j - price] + importance, dp[i - 1][j])
            # Otherwise, the maximum total importance value is the same as the previous item
            else:
                dp[i][j] = dp[i - 1][j]
    
    # Return the maximum total importance value for the last item and the remaining budget
    return dp[m][n]
def test_max_happiness():
    # Test case 1: Sample provided in the problem
    assert max_happiness(1000, 5, [(800, 2), (400, 5), (300, 5), (400, 3), (200, 2)]) == 3900, "Test case 1 failed"

    # Test case 2: Small budget with one item
    assert max_happiness(50, 1, [(60, 3)]) == 0, "Test case 2 failed"

    # Test case 4: Exact budget
    assert max_happiness(100, 2, [(50, 2), (50, 3)]) == 250, "Test case 4 failed"

    # Test case 5: No items
    assert max_happiness(100, 0, []) == 0, "Test case 5 failed"

    # Test case 6: All items exceed the budget
    assert max_happiness(10, 3, [(20, 1), (30, 2), (40, 3)]) == 0, "Test case 6 failed"

    # Test case 7: Multiple items with the same price and importance
    assert max_happiness(100, 4, [(25, 2), (25, 2), (25, 2), (25, 2)]) == 200, "Test case 7 failed"

    # Test case 8: Large number of items
    assert max_happiness(1000, 10, [(100, i) for i in range(1, 11)]) == 5500, "Test case 8 failed"

    print("All test cases passed!")

# Run the test function
test_max_happiness()