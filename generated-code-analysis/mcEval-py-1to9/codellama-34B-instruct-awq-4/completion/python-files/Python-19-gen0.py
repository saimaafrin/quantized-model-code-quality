
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
    # Define an empty 2d list to store the maximum energy obtainable from each valid sequence of beads
    dp = [[0] * len(beads) for _ in range(len(beads))]

    # For each sequence of beads of length 1, the maximum energy is the head value
    # of the only bead in the sequence
    for i in range(len(beads)):
        dp[i][0] = beads[i]

    # For each sequence of beads of length 2, the maximum energy is the maximum of the
    # product of the head and tail values of the beads, or the product of the head
    # value of the first bead and the tail value of the second bead.
    for i in range(len(beads)):
        dp[i][1] = max(beads[i] * beads[(i + 1) % len(beads)], beads[i] * beads[i + 1])

    # For each sequence of beads of length 3 or greater, the maximum energy is the maximum of
    # the maximum energy obtainable from each possible order of merging two adjacent beads,
    # which is the maximum of the following three cases:
    # 1. The maximum energy of the sequence minus the energy of the first two beads merged
    #    together (if the first bead has a tail value equal to the head value of the second bead)
    # 2. The maximum energy of the sequence minus the energy of the second two beads merged
    #    together (if the second bead has a tail value equal to the head value of the third bead)
    # 3. The maximum energy of the sequence minus the energy of the first and third beads merged
    #    together (if the first bead has a tail value equal to the head value of the third bead)
    for i in range(2, len(beads)):
        for j in range(len(beads)):
            if j + i < len(beads):
                dp[j][i] = max(dp[j][i], dp[j][i - 1] + beads[j] * beads[(j + i) % len(beads)])
                dp[j][i] = max(dp[j][i], dp[(j + 1) % len(beads)][i - 1] +
                                beads[(j + 1) % len(beads)] * beads[(j + i) % len(beads)])
                dp[j][i] = max(dp[j][i], dp[j][i - 2] + beads[j] * beads[(j + 2) % len(beads)])

    return max(dp[i][-1] for i in range(len(beads)))
def test_max_energy():
    assert max_energy([2, 3, 5, 10]) == 710, "Testcase 1 failed"
    assert max_energy([1, 2, 3, 4]) == 80, "Testcase 2 failed"
    assert max_energy([4, 4, 4, 4]) == 192, "Testcase 3 failed"
    assert max_energy([30, 40, 50, 60]) == 372000, "Testcase 4 failed"
    print("All testcases passed")

# Call the test function
test_max_energy()