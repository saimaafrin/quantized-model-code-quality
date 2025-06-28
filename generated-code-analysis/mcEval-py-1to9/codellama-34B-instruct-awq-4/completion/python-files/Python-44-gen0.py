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
    # initialise some variables for the program
    # monthly_savings is the amount of money Jinjin saves in each month
    # monthly_savings_list is a list containing the amount of money Jinjin saved in each month
    # total_savings is the total amount of money Jinjin saved in the year
    # interest_rate is the yearly interest rate that Jinjin earns on her savings
    # annual_earnings is the amount of money Jinjin earns in the year due to interest
    # total_money is the total amount of money Jinjin has at the end of the year
    monthly_savings, monthly_savings_list, total_savings, interest_rate, annual_earnings, total_money = 0, [], 0, 0.2, 0, 0

    # the for loop checks each item in the list, which represents Jinjin's monthly budget
    # Jinjin can save multiples of 100 from her pocket money if she predicts having at least 100 units remaining after expenses
    # Jinjin saves the money in the list monthly_savings_list
    for i in budgets:
        monthly_savings = i - (i % 100)
        monthly_savings_list.append(monthly_savings)

    # Jinjin saves the total amount of money she saved in the year, which is the sum of all the items in the list monthly_savings_list
    # Jinjin earns 20% interest on the total amount of money she saved in the year
    # Jinjin earns annual earnings of 20% on the total amount of money she saved in the year
    for i in monthly_savings_list:
        total_savings += i
    annual_earnings = total_savings * interest_rate

    # Jinjin earns annual earnings of 20% on the total amount of money she saved in the year
    # Jinjin has the total amount of money she saved in the year plus the annual earnings
    # Jinjin's total amount of money is the sum of the total amount of money she saved in the year and the annual earnings
    total_money = total_savings + annual_earnings

    # Jinjin's total amount of money is the sum of the total amount of money she saved in the year and the annual earnings
    # Jinjin's total amount of money is the total amount of money she has at the end of the year
    return total_money
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