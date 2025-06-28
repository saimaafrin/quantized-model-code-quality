
def max_energy(beads):
    """
    Calculate the maximum energy that can be released by merging beads on a necklace.

    The function takes a list of integers representing the energy beads on a necklace, where
    each bead has a head and a tail value. The head value of each bead must match the tail
    value of the next bead in the sequence. The necklace is circular, and merging two adjacent
    beads releases energy equal to the product of the head value of the first bead, the matching
    value, and the tail value of the second bead.

    To find the maximum energy release, the function considers all possible orders of merging beads
    and uses dynamic programming to compute the maximum energy obtainable.

    Args:
        beads: A list of integers where each integer represents the head value of a bead and
               the tail value of the previous bead. The tail value of the last bead is assumed
               to match the head value of the first bead due to the circular nature of the necklace.

    Returns:
        An integer representing the maximum energy that can be obtained by optimally merging all beads.

    Examples:
        >>> max_energy([2, 3, 5, 10])
        710
        >>> max_energy([1, 2, 3, 4])
        48
    """

    # Get the length of the beads list
    n = len(beads)

    # Create a 2D array dp to store the maximum energy that can be obtained
    # by merging the beads in range [i, j]
    dp = [[0] * n for _ in range(n)]

    # Initialize the base case: a single bead has zero energy release
    for i in range(n):
        dp[i][i] = 0

    # Iterate over the possible lengths of the ranges
    for length in range(2, n + 1):
        # Iterate over the starting indices of the ranges
        for i in range(n):
            # Compute the ending index of the range
            j = (i + length - 1) % n
            # Initialize the maximum energy release to a very small value
            dp[i][j] = float('-inf')
            # Iterate over the possible locations to partition the range
            for k in range(i, j):
                # Compute the energy release for the partition
                energy = dp[i][k] + dp[k + 1][j] + beads[i] * beads[(k + 1) % n] * beads[(j + 1) % n]
                # Update the maximum energy release if necessary
                dp[i][j] = max(dp[i][j], energy)

    # The maximum energy is the maximum energy release obtained by merging all beads
    max_energy = max(dp[i][(i + n - 1) % n] for i in range(n))

    return max_energy
def test_max_energy():
    assert max_energy([2, 3, 5, 10]) == 710, "Testcase 1 failed"
    assert max_energy([1, 2, 3, 4]) == 80, "Testcase 2 failed"
    assert max_energy([4, 4, 4, 4]) == 192, "Testcase 3 failed"
    assert max_energy([30, 40, 50, 60]) == 372000, "Testcase 4 failed"
    print("All testcases passed")

# Call the test function
test_max_energy()