from collections import deque
def generate_numbers(n, rules) -> int:
    """
    Generate all unique numbers from the given number by applying transformation rules.

    Each rule allows a single digit to be transformed into another. A breadth-first search
    (BFS) is used to explore all possible transformations. The function returns the count
    of unique numbers that can be generated from the original number, including the number itself.

    Args:
    - n (int): The original integer number to transform.
    - rules (list of tuples): A list of transformation rules, where each rule is represented
                              as a tuple (x, y) indicating that digit x can be transformed into y.

    Returns:
    - int: The total count of unique numbers that can be generated.

    Cases:
    >>> generate_numbers(234, [(2, 5), (3, 6)])
    4
    >>> generate_numbers(100, [(1, 9)])
    2
    """
    # A list of unique integers to explore
    to_explore = deque()
    # The set of all generated integers
    all_integers = set()
    # The count of unique integers
    count = 0

    # Initialize the BFS
    to_explore.append(n)
    all_integers.add(n)

    # Explore all integers
    while to_explore:
        # Get the next integer to explore
        integer = to_explore.popleft()
        count += 1
        # Try all possible transformations
        for x, y in rules:
            # Apply the transformation
            transformed = int(str(integer).replace(str(x), str(y)))
            # Add the transformed integer to the list of unique integers
            if transformed not in all_integers:
                to_explore.append(transformed)
                all_integers.add(transformed)

    # Return the count of all unique integers
    return count
def test_generate_numbers():
    # Test case 1
    n1, k1 = 234, 2
    rules1 = [(2, 5), (3, 6)]
    assert generate_numbers(n1, rules1) == 4, "Test case 1 failed"

    # Test case 2
    n2, k2 = 123, 3
    rules2 = [(1, 9), (2, 8), (3, 7)]
    assert generate_numbers(n2, rules2) == 8, "Test case 2 failed"

    # Test case 3
    n3, k3 = 999, 1
    rules3 = [(9, 1)]
    assert generate_numbers(n3, rules3) == 8, "Test case 3 failed"

    print("All test cases passed!")

# Call the test function
test_generate_numbers()