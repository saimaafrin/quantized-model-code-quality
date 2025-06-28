
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
    # check that the input is valid
    if not beads:
        raise ValueError('The input cannot be empty.')

    # initialize the values
    max_energy = 0
    dp = [0] * len(beads)

    # process the sequence recursively
    def process(beads, current):
        nonlocal max_energy

        # base case: merge the last two beads
        if current == len(beads) - 1:
            max_energy = max(max_energy, beads[0] * beads[1])
            return

        # process the next bead recursively
        process(beads, current + 1)

        # merge the current bead with the next bead
        if current + 2 < len(beads):
            dp[current] = max(dp[current], process(beads, current + 2) + beads[current] * beads[current + 1])

        # merge the current bead with the previous bead
        if current > 0:
            dp[current] = max(dp[current], process(beads, current - 1) + beads[current] * beads[current - 1])

        # return the maximum energy
        return dp[current]

    # start the recursion
    process(beads, 0)

    return max_energy
def test_max_energy():
    assert max_energy([2, 3, 5, 10]) == 710, "Testcase 1 failed"
    assert max_energy([1, 2, 3, 4]) == 80, "Testcase 2 failed"
    assert max_energy([4, 4, 4, 4]) == 192, "Testcase 3 failed"
    assert max_energy([30, 40, 50, 60]) == 372000, "Testcase 4 failed"
    print("All testcases passed")

# Call the test function
test_max_energy()