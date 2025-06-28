from typing import List
def jinjin_savings_plan(budgets: List[int]) -> int:
    """
    Calculates the total amount of money Jinjin will have by the end of the year
    after following her savings plan with her mother. Each month, she can save
    multiples of 100 from her pocket money (300 per month) if she predicts having
    at least 100 units remaining after expenses. The saved money will gain 20%
    interest at the end of the year.

    Parameters:
    budgets (List[int]): A list of 12 integers representing Jinjin's monthly budget.

    Returns:
    int: The total amount of money Jinjin will have at the end of the year after interest.
         If Jinjin runs out of money in any given month, returns the negative value of
         that month (-X, where X is the month number).

    Examples:
    >>> jinjin_savings_plan([290, 230, 280, 200, 300, 170, 340, 50, 90, 80, 200, 60])
    -7
    
    >>> jinjin_savings_plan([290, 230, 280, 200, 300, 170, 330, 50, 90, 80, 200, 60])
    1580
    """
    savings = 0
    for i in range(len(budgets)):
        # if budget is less than 100, break the loop and return the month number
        if budgets[i] < 100:
            return -(i+1)
        # if budget is more than or equal to 100, save 300 per month
        else:
            savings += 300
            # subtract 100 from budget to cover expenses
            budgets[i] -= 100
            # subtract remaining budget from savings
            savings -= budgets[i]
    # calculate 20% interest at the end of the year
    savings += savings * 0.2
    return savings
def test_jinjin_savings_plan():
    # Test case 1: Jinjin runs out of money in July (the 7th month)
    budgets1 = [290, 230, 280, 200, 300, 170, 340, 50, 90, 80, 200, 60]
    assert jinjin_savings_plan(budgets1) == -7, "Test case 1 failed"

    # Test case 2: Jinjin has 1580 units of currency by the end of the year
    budgets2 = [290, 230, 280, 200, 300, 170, 330, 50, 90, 80, 200, 60]
    assert jinjin_savings_plan(budgets2) == 1580, "Test case 2 failed"

    # Test case 3: Jinjin manages her budget perfectly and has a specific amount by the end
    budgets3 = [300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300]
    assert jinjin_savings_plan(budgets3) == 0, "Test case 3 failed"

    # Test case 4: Jinjin does not need to save any money and spends exactly the amount she receives
    budgets4 = [300, 290, 280, 270, 260, 250, 240, 230, 220, 210, 200, 190]
    assert jinjin_savings_plan(budgets4) == 780, "Test case 4 failed"

    # Test case 5: Jinjin runs out of money in the first month
    budgets5 = [350, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200]
    assert jinjin_savings_plan(budgets5) == -1, "Test case 5 failed"

    print("All test cases passed.")


# Run the test function
test_jinjin_savings_plan()