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
    if n < 0:
        raise ValueError("Invalid argument: n cannot be negative")

    if n == 0:
        return 1

    if len(rules) == 0:
        return 1

    # Use a breadth-first search to explore all possible transformations
    transformations = deque([(n, 1)])

    # Keep track of already visited numbers
    visited = set([n])
    count = 1
    while transformations:
        number, multiplier = transformations.popleft()

        # Try transforming each digit in the current number
        for i, digit in enumerate(str(number)):
            # Find the corresponding transformation rule
            rule = None
            for r in rules:
                if r[0] == digit:
                    rule = r
                    break
            if rule is None:
                continue

            # Add the transformation result to the queue
            result = number[:i] + rule[1] + number[i+1:]
            transformations.append((int(result), multiplier * rule[1]))
            visited.add(int(result))
            count += multiplier * rule[1]

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