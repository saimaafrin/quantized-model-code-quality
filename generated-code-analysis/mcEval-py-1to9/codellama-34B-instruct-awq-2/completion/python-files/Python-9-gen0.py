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
    permutation_list = permutations(range(1, 10))
    valid_combinations = []
    for i in permutation_list:
        for j in permutation_list:
            for k in permutation_list:
                if (i < j and j < k and (i[0] != k[0]) and (i[1] != k[1]) and (i[2] != k[2])):
                    first_number = int("".join(map(str, i)))
                    second_number = int("".join(map(str, j)))
                    third_number = int("".join(map(str, k)))
                    if (second_number == 2 * first_number and third_number == 3 * first_number):
                        valid_combinations.append((first_number, second_number, third_number))
    return sorted(valid_combinations, key=lambda x: x[0])
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