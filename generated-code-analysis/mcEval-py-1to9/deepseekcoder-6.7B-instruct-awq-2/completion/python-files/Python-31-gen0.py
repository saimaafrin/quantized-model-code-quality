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

    # Create a queue and add the original number to it
    queue = deque([str(n)])
    seen = {n}  # Store all the unique numbers we have seen

    # Apply each transformation rule one by one
    for x, y in rules:
        # If the rule applies to the original number, add the transformed number to the queue
        if str(n).count(str(x)) > 0:
            new_n = int(str(n).replace(str(x), str(y)))
            if new_n not in seen:
                queue.append(str(new_n))
                seen.add(new_n)

    # Continue to apply transformation rules until there are no more numbers in the queue
    while queue:
        current_n = int(queue.popleft())
        for x, y in rules:
            if str(current_n).count(str(x)) > 0:
                new_n = int(str(current_n).replace(str(x), str(y)))
                if new_n not in seen:
                    queue.append(str(new_n))
                    seen.add(new_n)

    # Return the count of unique numbers
    return len(seen)
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