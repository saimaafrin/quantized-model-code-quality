
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
    # Check that the input list is not empty
    if not beads:
        return 0

    # Define a helper function to compute the maximum energy release for a sequence of length n.
    # This function uses dynamic programming to compute the maximum energy obtainable by merging
    # all beads in a sequence of length n.
    def max_energy_for_length(n):
        # Compute the maximum energy for each possible order of merging
        energies = [0] * (n + 1)

        # Compute the maximum energy for each possible order of merging
        for i in range(1, n + 1):
            for j in range(i, n + 1):
                energy = 0

                # Merge the beads between i and j in each possible order
                for k in range(i, j):
                    energy += beads[k] * beads[k + 1]

                energies[i] = max(energies[i], energy)

        return energies[1]

    # Compute the maximum energy for all possible orders of merging
    return max(max_energy_for_length(n) for n in range(1, len(beads) + 1))
def test_max_energy():
    assert max_energy([2, 3, 5, 10]) == 710, "Testcase 1 failed"
    assert max_energy([1, 2, 3, 4]) == 80, "Testcase 2 failed"
    assert max_energy([4, 4, 4, 4]) == 192, "Testcase 3 failed"
    assert max_energy([30, 40, 50, 60]) == 372000, "Testcase 4 failed"
    print("All testcases passed")

# Call the test function
test_max_energy()