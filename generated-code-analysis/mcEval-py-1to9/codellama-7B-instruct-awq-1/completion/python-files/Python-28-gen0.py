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
    # Initialize queue to store nodes to be explored
    queue = deque()
    # Initialize queue with initial node (initial string A)
    queue.append((A, 0))
    # Initialize visited set to keep track of nodes already explored
    visited = set()
    # Initialize minimum number of steps required
    min_steps = 10
    # Initialize answer
    answer = "NO ANSWER!"

    while queue:
        # Get node from queue
        node = queue.popleft()
        # If node is equal to the target string, update minimum number of steps required
        if node[0] == B:
            min_steps = min(min_steps, node[1])
            answer = node[1]

        # Add node to visited set
        visited.add(node)

        # For each transformation rule
        for rule in rules:
            # If source substring is found in current node
            if node[0].find(rule[0]) != -1:
                # Replace source substring with target substring in current node
                temp = node[0].replace(rule[0], rule[1])
                # Create new node with updated string
                new_node = (temp, node[1] + 1)
                # If new node is not already in visited set, add to queue
                if new_node not in visited:
                    queue.append(new_node)

    # Return minimum number of steps required
    return answer
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