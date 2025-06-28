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
    # If the result for the current 'last' value has been calculated before,
    # use it to avoid recalculating it
    if last in memo:
        return memo[last]
    
    # If the last number is a power of 2, the only possible sequence is 'last' itself
    if (last & (last - 1)) == 0:
        return 1
    
    # Count the total number of valid sequences
    total = 0
    for i in range(1, int(last / 2) + 1):
        total += count_sequences(n, i, memo) * count_sequences(n + i, i, memo)
    
    # Store the result for the current 'last' value
    memo[last] = total
    
    return total
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