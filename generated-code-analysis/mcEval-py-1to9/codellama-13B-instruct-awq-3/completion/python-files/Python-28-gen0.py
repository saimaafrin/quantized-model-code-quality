from collections import deque
from typing import Union
def string_transformation(A: str, B: str, rules: list) -> Union[int, str]:
    """
    Perform string transformation from A to B using a set of transformation rules.

    This function takes an initial string A and a target string B, along with a list
    of transformation rules, and attempts to transform A into B using the rules.
    A Breadth-First Search (BFS) algorithm is used to explore the possible transformations
    up to a maximum of 10 steps. If A can be transformed into B within 10 steps, the function
    returns the minimum number of steps required. If it's not possible, the function returns
    "NO ANSWER!".

    Parameters:
    A (str): The initial string to be transformed.
    B (str): The target string to be achieved.
    rules (list of tuples): A list of transformation rules, where each rule is a tuple
                            containing the source substring (to be replaced) and the
                            target substring (to replace with).

    Returns:
    Union[int, str]: The minimum number of transformation steps if possible, otherwise "NO ANSWER!".

    Examples:
    >>> string_transformation("abcd", "xyz", [("abc", "xu"), ("ud", "y"), ("y", "yz")])
    3
    >>> string_transformation("aaa", "bbbb", [("a", "b"), ("aa", "bb"), ("aaa", "bbb")])
    'NO ANSWER!'
    """
    # If B is the same as A, there is no need to transform
    if A == B:
        return 0
    # Initialize the queue to hold the current string and the transformation steps
    # Initialize the transformation dictionary to map source strings to target strings
    queue = deque([(A, 0)])
    transformation_dict = {}
    for rule in rules:
        transformation_dict[rule[0]] = rule[1]
    # Explore the queue until it's empty
    while queue:
        current_string, transformation_steps = queue.popleft()
        # If the current string is the same as B, return the minimum number of steps required
        if current_string == B:
            return transformation_steps
        # If the maximum number of steps is reached, return "NO ANSWER!"
        if transformation_steps >= 10:
            return "NO ANSWER!"
        # Iterate through the possible transformations
        for source_substring in transformation_dict:
            # If the source substring is contained in the current string, perform the transformation
            if source_substring in current_string:
                target_substring = transformation_dict[source_substring]
                new_string = current_string.replace(source_substring, target_substring)
                # Add the new string to the queue with an incremented transformation step count
                queue.append((new_string, transformation_steps + 1))
    # If the queue is empty and the current string is not the same as B, return "NO ANSWER!"
    return "NO ANSWER!"
def test_string_transformation():
    # Test case 1
    A1 = "abcd"
    B1 = "xyz"
    rules1 = [("abc", "xu"), ("ud", "y"), ("y", "yz")]
    expected_result1 = 3
    assert string_transformation(A1, B1, rules1) == expected_result1, "Test case 1 failed"

    # Test case 2
    A2 = "aaa"
    B2 = "bbbb"
    rules2 = [("a", "b"), ("aa", "bb"), ("aaa", "bbb")]
    expected_result2 = "NO ANSWER!"
    assert string_transformation(A2, B2, rules2) == expected_result2, "Test case 2 failed"

    # Test case 3
    A3 = "hello"
    B3 = "world"
    rules3 = [("h", "w"), ("e", "o"), ("l", "r"), ("lol", "ldr")]
    expected_result3 = "NO ANSWER!"
    assert string_transformation(A3, B3, rules3) == expected_result3, "Test case 3 failed"

    print("All test cases passed!")

# Run the test function
test_string_transformation()