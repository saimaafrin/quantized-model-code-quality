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
    # Initialize the number of disc pairs on the A pole
    n_discs_a = n
    
    # Initialize the number of disc pairs on the B pole
    n_discs_b = 0
    
    # Initialize the number of disc pairs on the C pole
    n_discs_c = 0
    
    # Initialize the total number of moves
    total_moves = 0
    
    # Initialize the number of moves to transfer the disc pairs from A to B
    a_to_b_moves = 0
    
    # Initialize the number of moves to transfer the disc pairs from A to C
    a_to_c_moves = 0
    
    # Initialize the number of moves to transfer the disc pairs from B to C
    b_to_c_moves = 0
    
    # While there are disc pairs on the A pole
    while n_discs_a > 0:
        # Calculate the number of disc pairs on the B pole
        n_discs_b = n_discs_a - n_discs_c
        
        # Calculate the number of disc pairs on the C pole
        n_discs_c = n_discs_b
        
        # If there are at least two disc pairs on the A pole
        if n_discs_a >= 2:
            # Calculate the number of moves to transfer the disc pairs from A to B
            a_to_b_moves = hanoi_double_iterative(n_discs_a - 1)
            
            # Calculate the number of moves to transfer the disc pairs from A to C
            a_to_c_moves = hanoi_double_iterative(n_discs_a - 2)
            
            # Calculate the number of moves to transfer the disc pairs from B to C
            b_to_c_moves = hanoi_double_iterative(n_discs_b)
            
        # If there is only one disc pair on the A pole
        else:
            # Calculate the number of moves to transfer the disc pair from A to B
            a_to_b_moves = hanoi_double_iterative(n_discs_a - 1)
            
            # Calculate the number of moves to transfer the disc pair from A to C
            a_to_c_moves = hanoi_double_iterative(n_discs_a - 2)
        
        # Calculate the total number of moves
        total_moves = a_to_b_moves + a_to_c_moves + b_to_c_moves + n_discs_a
        
        # Reduce the number of disc pairs on the A pole by 1
        n_discs_a = n_discs_a - 1
    
    # Return the total number of moves
    return total_moves
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