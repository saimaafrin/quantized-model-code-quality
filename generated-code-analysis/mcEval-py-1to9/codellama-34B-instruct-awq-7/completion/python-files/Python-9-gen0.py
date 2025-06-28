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

    # Generate permutations of the numbers 1-9 without repetition.
    permutations_of_numbers = permutations(range(1, 10))
    number_combinations = []

    # Iterate over permutations of numbers.
    for permutation in permutations_of_numbers:
        # Skip permutations of numbers that contain a 0.
        if 0 in permutation:
            continue

        # Convert permutation to tuple.
        permutation = tuple(permutation)

        # Find first, second and third numbers based on permutation.
        first_number = int("".join(map(str, permutation)))
        second_number = first_number * 2
        third_number = first_number * 3

        # Check if second and third numbers can be represented by permutation.
        second_number_permutation = tuple(str(second_number))
        third_number_permutation = tuple(str(third_number))
        if second_number_permutation not in permutations_of_numbers or third_number_permutation not in permutations_of_numbers:
            continue

        # Add tuple representing the number combination to list of number combinations.
        number_combinations.append((first_number, second_number, third_number))

    return sorted(number_combinations)
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