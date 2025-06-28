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

    # Initialize the number of moves as the minimum number of moves required for n-1 discs
    moves = 2 * n - 1

    # Initialize the number of discs that have been moved from the A pole to the C pole
    moved_discs = n - 1

    # While the A pole still has discs and the number of moved discs is less than the total number of discs on the A pole
    while (moved_discs < n) and (n > 0):
        # The number of discs that need to be moved to the C pole is 2n - 1
        moves += 2 * n - 1

        # The number of discs that have been moved from the A pole to the C pole is increased by n - 1
        moved_discs += n - 1

        # If the number of discs on the A pole is greater than the number of moved discs, then the number of discs on the A pole is decreased by n - 1
        if n > moved_discs:
            n -= 1

    # Return the total number of moves required to transfer all the discs from the A pole to the C pole
    return moves
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