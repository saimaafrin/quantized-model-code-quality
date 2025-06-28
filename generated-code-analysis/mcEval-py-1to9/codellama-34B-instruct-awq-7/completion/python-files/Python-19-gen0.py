
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
    # Initialize two arrays to hold the maximum energy for each bead and the previous bead
    # that was merged with it. The arrays will be the same length as the number of beads.
    energy = [0] * len(beads)
    prev = [-1] * len(beads)

    # To obtain the maximum energy, we consider all possible orders of merging beads.
    # For each possible order, we calculate the maximum energy obtainable, using
    # dynamic programming to consider all possible combinations of merging beads.
    for i in range(len(beads)):
        # For each bead, we consider merging all possible adjacent pairs of beads.
        # We start by considering the first bead and merging it with the second bead.
        for j in range(len(beads) - 1):
            # Calculate the energy obtainable by merging the current bead with the next bead
            # using the formula from the problem description.
            e = beads[j] * beads[(j + 1) % len(beads)] * beads[(j + 2) % len(beads)]
            # If the energy obtained by merging the current bead with the next bead is greater
            # than the energy obtainable for the previous bead, we update the energy and
            # previous bead arrays accordingly.
            if e > energy[j]:
                energy[j] = e
                prev[j] = j + 1

    # We repeat the process above for all possible adjacent pairs of beads in the sequence.
    # At this point, we have found the maximum energy obtainable for each bead. We now need
    # to find the sequence of merges that maximizes the energy. We do this by tracing back
    # through the previous bead array and merging beads until we have merged all of the beads.
    i = 0
    while i != -1:
        # Merge the current bead with the previous bead and remove the previous bead from the sequence.
        beads[i] = beads[i] * beads[(i - 1) % len(beads)] * beads[(i + 1) % len(beads)]
        beads.pop(i - 1)
        # Update the previous bead array to reflect the removal of the previous bead.
        for k in range(i, len(prev)):
            prev[k] -= 1
        # Update the current bead to the previous bead we just merged with.
        i = prev[i] - 1

    # Return the maximum energy obtainable for the given sequence of beads.
    return energy[-1]
def test_max_energy():
    assert max_energy([2, 3, 5, 10]) == 710, "Testcase 1 failed"
    assert max_energy([1, 2, 3, 4]) == 80, "Testcase 2 failed"
    assert max_energy([4, 4, 4, 4]) == 192, "Testcase 3 failed"
    assert max_energy([30, 40, 50, 60]) == 372000, "Testcase 4 failed"
    print("All testcases passed")

# Call the test function
test_max_energy()