
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
    # Determine the length of the necklace, including the circular connection.
    length = len(beads) + 1

    # Initialize an array of integers to hold the maximum energy that can be obtained by merging all beads
    # for each possible order of merging. The first element represents merging the last bead with the first bead,
    # the second element represents merging the second last bead with the first bead, etc. The last element
    # represents the energy obtained by merging the last bead with the second bead.
    dp = [0] * length

    # Initialize the maximum energy to be zero.
    max_energy = 0

    # Loop through each possible order of merging beads and compute the maximum energy obtainable.
    for i in range(length):
        # Merge the head value of the first bead with the tail value of the last bead.
        dp[i] = dp[i - 1] + beads[0] * beads[-1]

        # Loop through each bead in the necklace except for the first and last beads.
        for j in range(1, length - 1):
            # Merge the head value of the current bead with the tail value of the previous bead.
            dp[i] = max(dp[i], dp[i - j] + beads[j] * beads[j - 1])

        # Update the maximum energy if the current order of merging beads resulted in the maximum energy.
        max_energy = max(max_energy, dp[i])

    # Return the maximum energy that can be obtained by optimally merging all beads.
    return max_energy
def test_max_energy():
    assert max_energy([2, 3, 5, 10]) == 710, "Testcase 1 failed"
    assert max_energy([1, 2, 3, 4]) == 80, "Testcase 2 failed"
    assert max_energy([4, 4, 4, 4]) == 192, "Testcase 3 failed"
    assert max_energy([30, 40, 50, 60]) == 372000, "Testcase 4 failed"
    print("All testcases passed")

# Call the test function
test_max_energy()