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
    # Base case: No more sequences can be formed.
    if n == 0:
        return 0
    # Base case: Only one valid sequence can be formed.
    if n == last:
        return 1
    # Check if the number of valid sequences has already been calculated.
    if last in memo:
        return memo[last]
    # If the last number is greater than the half of the starting number, then
    # the sequence is invalid.
    if last > n / 2:
        return 0
    # If the sequence is valid, calculate the number of sequences that can be
    # formed with the next number.
    memo[last] = count_sequences(n - 1, last - 1, memo) + count_sequences(n - 1, last + 1, memo)
    return memo[last]
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