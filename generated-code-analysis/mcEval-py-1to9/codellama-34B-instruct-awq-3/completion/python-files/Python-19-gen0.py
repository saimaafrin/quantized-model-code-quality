
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
    # Store the head and tail of each bead as a tuple.
    beads = [(beads[i-1], beads[i]) for i in range(len(beads))]

    # Initialize the dynamic programming table.
    # `energy` represents the maximum energy that can be obtained by merging the first i beads,
    # while `prev` stores the previous bead that was merged to obtain the maximum energy.
    energy = [0] * len(beads)
    prev = [None] * len(beads)

    # Initialize the first bead.
    energy[0] = beads[0][0] * beads[0][1]
    prev[0] = 0

    # Iterate through all beads and consider all possible merges.
    for i in range(1, len(beads)):
        # Store the current bead as the previous bead.
        prev[i] = i

        # Consider merging the current bead with all previous beads.
        for j in range(i):
            # If the current bead cannot be merged with the previous bead, skip it.
            if beads[j][1] != beads[i][0]:
                continue

            # Calculate the energy that can be obtained by merging the current bead with the previous bead.
            energy_curr = energy[j] + beads[j][0] * beads[j][1] * beads[i][1]

            # If the energy is greater than the maximum, store the previous bead and update the maximum energy.
            if energy_curr > energy[i]:
                energy[i] = energy_curr
                prev[i] = j

    # Find the index of the last bead.
    i = len(beads) - 1
    while prev[i] is not None:
        i = prev[i]

    # Return the maximum energy.
    return energy[i]
def test_max_energy():
    assert max_energy([2, 3, 5, 10]) == 710, "Testcase 1 failed"
    assert max_energy([1, 2, 3, 4]) == 80, "Testcase 2 failed"
    assert max_energy([4, 4, 4, 4]) == 192, "Testcase 3 failed"
    assert max_energy([30, 40, 50, 60]) == 372000, "Testcase 4 failed"
    print("All testcases passed")

# Call the test function
test_max_energy()