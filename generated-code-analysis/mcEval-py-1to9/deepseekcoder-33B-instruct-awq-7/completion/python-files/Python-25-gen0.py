def count_sequences(n: int, last: int, memo: dict) -> int:
    """
    Calculate the number of valid sequences that can be formed according to specific rules.
    
    Each sequence starts with a given number 'n', and a new number can be appended to the sequence
    if it is a positive integer and not greater than half the last number in the sequence. This
    function uses memoization to store previously calculated results to optimize performance.
    
    Args:
        n (int): The starting number of the sequence.
        last (int): The last number in the current sequence.
        memo (dict): A dictionary used for memoization, storing the number of valid sequences
                     for each 'last' value encountered.
    
    Returns:
        int: The total number of valid sequences that can be formed starting with 'n'.
    
    Examples:
        >>> count_sequences(1, 1, {})
        1
        >>> count_sequences(6, 6, {})
        6
    """
    
    # If last is 1, only one sequence is valid
    if last == 1:
        return 1
    
    # If we have already calculated for this 'last', return the stored value
    if last in memo:
        return memo[last]
    
    count = 0
    # Iterate from n to last/2 + 1 (inclusive)
    for i in range(n, last//2 + 1):
        count += count_sequences(i, i, memo)  # Recursive call with new 'last' value
    
    # Store the result in memo and return
    memo[last] = count
    return count
def test_count_sequences():
    test_cases = [
        (6, 6),
        (1, 1),
        (10, 14)
    ]

    for i, (n, expected) in enumerate(test_cases):
        memo = {}
        result = count_sequences(n, n, memo)
        assert result == expected, f"Test case {i+1} failed: expected {expected}, got {result}"
        print(f"Test case {i+1} passed: n = {n}, expected = {expected}, got = {result}")

# Call the test function
test_count_sequences()