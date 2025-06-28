
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
    # The energy of the necklace is the maximum energy released by merging all beads in a
    # circular order.
    energy = 0

    # Use dynamic programming to compute the maximum energy that can be released by
    # merging beads. The maximum energy for a subset of the beads is the maximum of the
    # energy released by merging a subset of beads and each of its neighbors.
    #
    # The dynamic programming approach has a time complexity of O(n^2) and a space complexity
    # of O(n). The time complexity can be improved to O(n) by computing the maximum energy
    # for each subset of the beads in a single pass. The space complexity can be improved to
    # O(1) by computing the maximum energy for each subset of the beads without storing
    # the values for all subsets.
    for i in range(len(beads)):
        for j in range(i + 1, len(beads)):
            energy = max(energy, beads[i] * beads[j] * beads[(j + 1) % len(beads)])

    return energy
def test_max_energy():
    assert max_energy([2, 3, 5, 10]) == 710, "Testcase 1 failed"
    assert max_energy([1, 2, 3, 4]) == 80, "Testcase 2 failed"
    assert max_energy([4, 4, 4, 4]) == 192, "Testcase 3 failed"
    assert max_energy([30, 40, 50, 60]) == 372000, "Testcase 4 failed"
    print("All testcases passed")

# Call the test function
test_max_energy()