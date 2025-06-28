
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
    # First, add the head value of the first bead to the tail values of all beads
    # to represent the circular necklace
    beads = [beads[0]] + beads[:0] + beads[1:] + [beads[0]]
    n = len(beads)

    # dp[i][j] will contain the maximum energy that can be obtained by merging beads
    # from i to j (inclusive) in the original order
    dp = [[0] * n for _ in range(n)]

    # Iterate over all possible subproblems
    for length in range(2, n):
        for start in range(n - length):
            end = (start + length) % n
            best = 0

            # Try to merge each possible bead at the start and end
            for split in range(1, length):
                energy = dp[start][(start + split) % n] + dp[(start + split) % n][end]
                energy += beads[start] * beads[(start + split) % n] * beads[end]
                best = max(best, energy)

            dp[start][end] = best

    # The maximum energy is in dp[0][n-1]
    return dp[0][n - 1]
def test_max_energy():
    assert max_energy([2, 3, 5, 10]) == 710, "Testcase 1 failed"
    assert max_energy([1, 2, 3, 4]) == 80, "Testcase 2 failed"
    assert max_energy([4, 4, 4, 4]) == 192, "Testcase 3 failed"
    assert max_energy([30, 40, 50, 60]) == 372000, "Testcase 4 failed"
    print("All testcases passed")

# Call the test function
test_max_energy()