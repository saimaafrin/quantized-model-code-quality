def hanoi_double_iterative(n: int) -> int:
    """
    Calculate the minimum number of moves required to solve the double-disc Hanoi Towers problem for n pairs of discs.
    
    This function implements an iterative algorithm to determine the minimum number of moves necessary to transfer
    2n discs from the A pole to the C pole in a double-disc Hanoi Towers setup, following the rules that only one disc 
    can be moved at a time and no disc may be placed on top of a smaller disc. The function uses a known recursive relation 
    and iteratively computes the total number of moves for n pairs of discs.
    
    Args:
    n (int): The number of disc pairs (each of two identical discs) on the A pole.

    Returns:
    int: The minimum number of moves required to transfer all the discs from the A pole to the C pole.

    Cases:
    - For n=1, the function should return 2.
    - For n=2, the function should return 6.
    - For n=3, the function should return 14.
    """

    # Initialize an empty list to hold the total number of moves for each number of pairs of discs.
    total_moves = []

    # Initialize the number of moves for the first number of pairs of discs.
    total_moves.append(0)

    # Initialize the number of moves for the second number of pairs of discs.
    total_moves.append(1)

    # Initialize the number of moves for the third number of pairs of discs.
    total_moves.append(3)

    # Initialize the number of moves for the fourth number of pairs of discs.
    total_moves.append(7)

    # If the number of pairs of discs exceeds 4, then use the recurrence relation to calculate the total number of moves.
    if n > 4:
        for i in range(5, n+1):
            total_moves.append(2*total_moves[i-1] + total_moves[i-2])

    # Return the total number of moves for the given number of pairs of discs.
    return total_moves[n]
def test_hanoi_double_iterative():
    # Test case 1: n = 1
    assert hanoi_double_iterative(1) == 2, "Test case 1 failed"

    # Test case 2: n = 2
    assert hanoi_double_iterative(2) == 6, "Test case 2 failed"

    # Test case 3: n = 3
    assert hanoi_double_iterative(3) == 14, "Test case 3 failed"

    # Additional test cases can be added based on computed or known results
    # Test case 4: n = 4 (computed using the formula)
    assert hanoi_double_iterative(4) == 30, "Test case 4 failed"

    # Test case 5: n = 5 (computed using the formula)
    assert hanoi_double_iterative(5) == 62, "Test case 5 failed"

    # Test case 6: Large n, n = 10 (computed using the formula or a trusted source)
    assert hanoi_double_iterative(10) == 2046, "Test case 6 failed"

    print("All test cases passed!")


# Run the test function
test_hanoi_double_iterative()