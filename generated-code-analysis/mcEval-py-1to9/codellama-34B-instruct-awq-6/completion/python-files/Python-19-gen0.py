
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
    # Set up a dynamic programming table to store the maximum energy obtainable by merging any two
    # adjacent beads and the resulting bead. The top row will represent the original necklace, the
    # bottom row will represent the merging of the two end beads, and the first column will represent
    # the merging of the first and second beads. Each row will have two more entries than the previous
    # row.
    dp_table = [[[0, 0] for _ in range(len(beads) + 2)] for _ in range(2)]

    # Set the top row of the table to represent the original necklace. The first and last beads are
    # not merged, so their energy values are zero.
    dp_table[0][0][0] = 0
    dp_table[0][0][1] = 0
    for i in range(1, len(beads) + 1):
        dp_table[0][i][0] = beads[i - 1]
        dp_table[0][i][1] = beads[i - 1]

    # Set the bottom row of the table to represent the merging of the two end beads.
    dp_table[1][-1][0] = dp_table[0][-1][0]
    dp_table[1][-1][1] = dp_table[0][-1][1]

    # Iterate over each row of the table from the second-to-last row to the first row.
    for i in range(len(dp_table) - 2, -1, -1):
        # Iterate over each column of the row, where each column represents the merging of two adjacent
        # beads. The first and last columns of each row are invalid because they involve merging beads
        # that are not adjacent.
        for j in range(1, len(dp_table[i]) - 1):
            # Iterate over the two possible beads that can be merged with the current bead. The first bead
            # is the one directly to the left of the current bead, and the second bead is the one directly
            # to the right of the current bead.
            for k in range(0, 2):
                # Calculate the energy obtained by merging the two beads. The first bead must match the
                # tail value of the current bead, and the second bead must match the head value of the
                # current bead. The energy is calculated as the product of the head value of the first
                # bead, the matching value, and the tail value of the second bead.
                energy = dp_table[i + 1][j - k][k] * beads[j - 1] * dp_table[i + 1][j - k][1 - k]

                # Update the maximum energy obtainable if the energy obtained by merging the two beads is
                # greater than the current
def test_max_energy():
    assert max_energy([2, 3, 5, 10]) == 710, "Testcase 1 failed"
    assert max_energy([1, 2, 3, 4]) == 80, "Testcase 2 failed"
    assert max_energy([4, 4, 4, 4]) == 192, "Testcase 3 failed"
    assert max_energy([30, 40, 50, 60]) == 372000, "Testcase 4 failed"
    print("All testcases passed")

# Call the test function
test_max_energy()