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
    # Keep a set of all unique numbers generated, including the original number.
    numbers = {n}
    # Keep a queue of numbers to explore.
    to_explore = deque([n])
    # Keep applying rules until the queue is empty.
    while to_explore:
        # Extract the next number from the queue.
        num = to_explore.popleft()
        # Apply all possible rules to the number.
        for x, y in rules:
            # If the number contains the digit that we are going to replace.
            if str(x) in str(num):
                # Generate the new number by applying the rule.
                new_num = int(str(num).replace(str(x), str(y)))
                # If the new number is not in the set of unique numbers yet, add it to the set.
                if new_num not in numbers:
                    numbers.add(new_num)
                    # Add the new number to the queue to explore.
                    to_explore.append(new_num)
    # Return the total count of unique numbers generated, including the original number.
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