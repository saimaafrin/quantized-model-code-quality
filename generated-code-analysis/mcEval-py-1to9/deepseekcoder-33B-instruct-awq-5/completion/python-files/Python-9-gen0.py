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
    digits = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    combinations = list(permutations(digits, 3))

    valid_combinations = []

    for comb in combinations:
        if comb[1] == 2 * comb[0] and comb[2] == 3 * comb[0]:
            valid_combinations.append((comb[0]*100 + comb[1]*10 + comb[2], 
                                       comb[0]*100 + comb[1]*10*2 + comb[2]*2, 
                                       comb[0]*100 + comb[1]*10*3 + comb[2]*3))

    return sorted(valid_combinations)
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