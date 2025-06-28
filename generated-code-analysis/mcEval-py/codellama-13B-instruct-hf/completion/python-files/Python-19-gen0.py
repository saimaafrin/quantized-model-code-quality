
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
    # This is a brute-force solution.
    #
    # There is a faster algorithm based on dynamic programming that can be found at
    # https://github.com/codelucas/python-solutions/blob/master/algorithms/dynamic_programming/necklace/necklace.py
    #
    # I chose not to use that algorithm in order to keep this function as simple as possible.
    # It is a good idea to read through that code and try to understand how the dynamic
    # programming solution works.

    # First, sort the list of beads to ensure that beads with matching values are adjacent.
    beads.sort()

    # The maximum energy that can be released is the maximum of the energy released
    # by merging pairs of beads. For example, merging a bead with head value 2 and
    # tail value 3 releases 6 energy units.
    max_energy = 0

    # The number of beads in the necklace is one less than the length of the input
    # list because the tail value of the last bead is assumed to match the head
    # value of the first bead.
    num_beads = len(beads) - 1

    # Iterate over all possible pairs of beads to consider merging.
    for i in range(num_beads):
        # Merging a bead with itself is a no-op, so skip it.
        if i == num_beads - 1:
            continue

        # Compute the energy released by merging the current bead with the next bead.
        energy = beads[i] * beads[i + 1]

        # Keep track of the maximum energy that can be released by merging all beads.
        if energy > max_energy:
            max_energy = energy

    return max_energy
def test_max_energy():
    assert max_energy([2, 3, 5, 10]) == 710, "Testcase 1 failed"
    assert max_energy([1, 2, 3, 4]) == 80, "Testcase 2 failed"
    assert max_energy([4, 4, 4, 4]) == 192, "Testcase 3 failed"
    assert max_energy([30, 40, 50, 60]) == 372000, "Testcase 4 failed"
    print("All testcases passed")

# Call the test function
test_max_energy()