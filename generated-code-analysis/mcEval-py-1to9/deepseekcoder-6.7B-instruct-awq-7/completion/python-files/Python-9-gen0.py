from itertools import permutations

def find_number_combinations():
    """
    Generate all unique combinations of three numbers, each formed from the digits 1 to 9 without repetition,
    such that the second number is twice the first and the third is three times the first.

    Returns:
        list of tuples: A sorted list of tuples, where each tuple contains three integers representing the
                        valid number combinations in ascending order based on the first number.

    Example:
        >>> find_number_combinations()
        [(123, 246, 369), (124, 248, 372), ...]
    """
    all_numbers = []
    for perm in permutations('123456789', 3):
        num1 = int(''.join(perm))
        num2 = num1 * 2
        num3 = num1 * 3
        if num2 > 999 or num3 > 999:
            continue
        num1_digits = set(str(num1))
        num2_digits = set(str(num2))
        num3_digits = set(str(num3))
        if num1_digits == num2_digits == num3_digits == {'1','2','3','4','5','6','7','8','9'}:
            all_numbers.append((num1, num2, num3))
    all_numbers.sort()
    return all_numbers
def test_find_number_combinations():
    # Call the function to get the combinations
    combinations = find_number_combinations()

    # Check that we have at least one valid combination
    assert len(combinations) > 0, "There should be at least one valid combination."

    # Iterate over each combination to perform further checks
    for combo in combinations:
        # Each combination should have exactly three numbers
        assert len(combo) == 3, "Each combination should have three numbers."

        # Check if numbers are 3-digit numbers
        for num in combo:
            assert 100 <= num <= 999, f"Each number should be a 3-digit number, got {num}."

        # Check the 1:2:3 ratio
        assert combo[1] == 2 * combo[0] and combo[2] == 3 * combo[0], "The numbers should be in a 1:2:3 ratio."

    print("All test cases passed!")

# Run the test cases
test_find_number_combinations()