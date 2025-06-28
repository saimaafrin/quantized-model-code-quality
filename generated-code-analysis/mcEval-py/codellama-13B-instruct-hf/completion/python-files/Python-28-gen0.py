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

    # BFS graph.
    G = {
        "": "abcd"
    }

    # BFS queue.
    Q = deque([""])

    # Mark visited strings.
    V = set([""])

    # Maximum number of steps.
    MAX_STEPS = 10

    # Iterate until all possible transformation have been exhausted.
    for step in range(MAX_STEPS):

        # BFS dequeue.
        while len(Q) > 0:
            # Extract the first string from the queue.
            string = Q.popleft()

            # Apply all transformation rules to the string.
            for rule in rules:
                # Transform the string.
                transformed_string = string.replace(rule[0], rule[1])

                # Check if the transformed string is already in the graph.
                if transformed_string not in G:
                    # Add the string to the graph.
                    G[transformed_string] = string

                    # Add the string to the queue.
                    Q.append(transformed_string)

                    # Mark the string as visited.
                    V.add(transformed_string)

        # Check if the target string is in the graph.
        if B in G:
            # If it's the case, return the minimum number of steps required.
            return step

        # Check if the maximum number of steps has been reached.
        if step == MAX_STEPS - 1:
            # If it's the case, return "NO ANSWER!"
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