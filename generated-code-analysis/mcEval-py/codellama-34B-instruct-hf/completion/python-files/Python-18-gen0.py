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
    # Initialize a 2D table to store the maximum value achievable with each possible combination of 
    # items. The rows of the table will represent the budget and the columns will represent the items.
    # The table will be initialized to zeroes except for the first row which will represent the 
    # maximum value achievable when there is no budget and no items.
    table = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
    
    # Loop through each possible budget and each possible item.
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            # Determine the maximum value achievable for the current budget and item. If the price of 
            # the current item is greater than the current budget, then the maximum value is 0. 
            # Otherwise, the maximum value is the maximum of the following:
            # - The maximum value achievable with the previous item and the previous budget.
            # - The maximum value achievable with the previous item and the current budget minus the 
            #   price of the current item, plus the importance value of the current item.
            table[i][j] = max(table[i][j - 1], table[i - items[j - 1][0]][j - 1] + items[j - 1][1])
    
    # Return the maximum value achievable with the last row of the table.
    return table[-1][-1]
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