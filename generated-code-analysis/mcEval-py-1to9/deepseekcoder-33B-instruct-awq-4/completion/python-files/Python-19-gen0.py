
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
    # initialize dynamic programming table with zeros
    dp = [[0 for _ in range(len(beads))] for _ in range(len(beads))]

    # fill in dynamic programming table
    for length in range(2, len(beads) + 1):
        for i in range(len(beads)):
            j = (i + length - 1) % len(beads)
            for k in range(i, j + 1):
                left_value = beads[i] if i < j else beads[j - len(beads)]
                right_value = beads[j] if j < len(beads) else beads[j - len(beads)]
                dp[i][j] = max(dp[i][j], dp[(k + 1) % len(beads)][(j + len(beads) - 1) % len(beads)] + left_value * beads[k] * right_value)

    # find maximum energy
    max_energy = max(dp[i][i - 1] for i in range(len(beads)))

    return max_energy
def test_max_energy():
    assert max_energy([2, 3, 5, 10]) == 710, "Testcase 1 failed"
    assert max_energy([1, 2, 3, 4]) == 80, "Testcase 2 failed"
    assert max_energy([4, 4, 4, 4]) == 192, "Testcase 3 failed"
    assert max_energy([30, 40, 50, 60]) == 372000, "Testcase 4 failed"
    print("All testcases passed")

# Call the test function
test_max_energy()