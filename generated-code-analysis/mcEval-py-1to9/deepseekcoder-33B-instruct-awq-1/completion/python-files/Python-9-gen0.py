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

    # Generate all permutations of digits 1 to 9
    perms = permutations(range(1, 10))

    # Filter the permutations to find the valid number combinations
    results = []
    for perm in perms:
        # Check if the second number is twice the first and the third is three times the first
        if perm[1] == 2 * perm[0] and perm[2] == 3 * perm[0]:
            # Convert the digits to a number and append to the results
            results.append((int("".join(map(str, perm[0:3]))),
                            int("".join(map(str, perm[3:6]))),
                            int("".join(map(str, perm[6:9])))))

    # Sort the results based on the first number
    results.sort()

    return results
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