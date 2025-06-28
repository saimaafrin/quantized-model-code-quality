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

    # Initialize a 2D table, where dp[i][j] will be the maximum total importance value that can 
    # be achieved considering the first i items and a budget of j.
    dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
    
    # Fill the table in bottom-up manner.
    for i in range(1, m+1):
        for j in range(1, n+1):
            # If the price of the i-th item is more than the current budget, we can't include 
            # this item, so we take the maximum importance value from the previous item.
            if items[i-1][0] > j:
                dp[i][j] = dp[i-1][j]
            else:
                # If we can include the i-th item, we take the maximum of two choices:
                # 1. Including the i-th item and getting the maximum importance value from the
                # remaining budget (j - price of i-th item) and previous items.
                # 2. Not including the i-th item and getting the maximum importance value from
                # the current budget and previous items.
                dp[i][j] = max(dp[i-1][j], items[i-1][1] + dp[i-1][j-items[i-1][0]])
    
    # The maximum total importance value that can be achieved considering all items and the 
    # given budget is stored at dp[m][n].
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