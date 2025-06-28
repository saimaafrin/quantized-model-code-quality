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
    # Initialize the queue to explore the transformation graph.
    queue = deque([n])
    # Keep track of all transformed numbers.
    numbers = set()
    # Add the original number to the set of transformed numbers.
    numbers.add(n)

    # Keep exploring the graph until the queue is empty.
    while queue:
        # Dequeue the next number.
        current_number = queue.popleft()
        # Loop through all transformation rules.
        for rule in rules:
            # Check if the rule applies to the current number.
            if rule[0] in str(current_number):
                # Create a new number by applying the rule.
                new_number = current_number // 10 * 10 + rule[1]
                # Add the new number to the queue for exploration.
                queue.append(new_number)
                # Add the new number to the set of transformed numbers.
                numbers.add(new_number)

    # Return the count of unique numbers.
    return len(numbers)
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