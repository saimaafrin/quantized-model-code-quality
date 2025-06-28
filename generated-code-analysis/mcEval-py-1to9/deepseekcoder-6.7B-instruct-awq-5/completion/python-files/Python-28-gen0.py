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
    if len(A) != len(B):
        raise ValueError("The lengths of the initial and target strings must be equal.")
    if not all(len(rule) == 2 for rule in rules):
        raise ValueError("All rules must be tuples of length 2.")
    queue = deque([(A, 0)])  # using a queue to store the current state and steps
    visited = {A: 0}  # using a dictionary to record the visited states
    while queue:
        current_str, steps = queue.popleft()
        if current_str == B:  # if the current string is equal to B, return the steps
            return steps
        if steps == 10:  # if the steps are more than 10, continue
            continue
        for rule in rules:
            source, target = rule
            i = current_str.find(source)
            while i != -1:  # while there are more matches of source
                new_str = current_str[:i] + target + current_str[i+len(source):]
                if new_str not in visited or steps+1 < visited[new_str]:
                    queue.append((new_str, steps+1))
                    visited[new_str] = steps+1
                i = current_str.find(source, i+1)
    return "NO ANSWER!"  # if no path is found, return "NO ANSWER!"
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