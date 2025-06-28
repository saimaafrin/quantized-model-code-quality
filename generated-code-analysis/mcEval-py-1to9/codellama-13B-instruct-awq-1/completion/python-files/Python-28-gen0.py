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
    def BFS(A, B, rules, max_steps):
        """
        Perform a breadth-first search to find the minimum number of steps to transform A
        into B using the provided rules.

        Parameters:
        A (str): The initial string to be transformed.
        B (str): The target string to be achieved.
        rules (list of tuples): A list of transformation rules, where each rule is a tuple
                                containing the source substring (to be replaced) and the
                                target substring (to replace with).
        max_steps (int): The maximum number of steps allowed before returning "NO ANSWER!".

        Returns:
        Union[int, str]: The minimum number of transformation steps if possible, otherwise "NO ANSWER!".
        """
        if max_steps == 0: return "NO ANSWER!"

        queue = deque([(A, B, 0)])
        visited = set()

        while queue:
            string_A, string_B, steps = queue.popleft()

            if string_A == string_B: return steps
            if (string_A, string_B) in visited: continue
            visited.add((string_A, string_B))

            for rule in rules:
                if string_A == rule[0] and string_B[0] == rule[1]:
                    queue.append((string_A[1:], string_B[1:], steps + 1))
                if string_A[0] == rule[0] and string_B[0] == rule[1]:
                    queue.append((string_A[1:], string_B, steps + 1))
                if string_A == rule[0] and string_B[0] == rule[1]:
                    queue.append((string_A, string_B[1:], steps + 1))
                if string_A[0] == rule[0] and string_B[0] == rule[1]:
                    queue.append((string_A, string_B, steps + 1))

        return "NO ANSWER!"

    return BFS(A, B, rules, 10)
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