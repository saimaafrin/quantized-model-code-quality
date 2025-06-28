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

    # Initialize the queue with the starting node
    q = deque([(A, 0)])

    # Set the maximum number of steps
    max_steps = 10

    # Dictionary to keep track of the number of steps required to transform A into B
    steps = {A: 0}

    # Breadth-First Search (BFS)
    while q:
        # Get the current state
        current_state, current_step = q.popleft()

        # Check if the goal state is reached
        if current_state == B:
            return current_step

        # Maximum number of steps reached
        if current_step == max_steps:
            return "NO ANSWER!"

        # Generate the next states
        for rule in rules:
            # Get the source and target substrings
            source, target = rule

            # Check if the current state can be transformed using the rule
            if current_state.find(source) != -1:
                # Get the transformed state
                transformed_state = current_state.replace(source, target)

                # Check if the transformed state has already been visited
                if transformed_state not in steps:
                    # Add the transformed state to the queue and the number of steps required
                    q.append((transformed_state, current_step + 1))
                    steps[transformed_state] = current_step + 1

    # If the goal state is not found, return "NO ANSWER!"
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