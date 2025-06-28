
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

    # Calculate the number of beads in the necklace
    num_beads = len(beads)

    # Initialize the list to store the maximum energy for each merge
    # 0th index is for no merge
    # 1st index is for merging the 1st and 2nd beads
    # 2nd index is for merging the 1st and 3rd beads
    # 3rd index is for merging the 1st and 4th beads
    # ...
    # Nth index is for merging the Nth and 1st beads
    max_energy = [0] * (num_beads + 1)

    # Initialize the list to store the minimum value for each bead
    # 0th index is for no merge
    # 1st index is for merging the 1st and 2nd beads
    # 2nd index is for merging the 1st and 3rd beads
    # 3rd index is for merging the 1st and 4th beads
    # ...
    # Nth index is for merging the Nth and 1st beads
    min_value = [0] * (num_beads + 1)

    # Loop through each bead in the necklace
    for i in range(1, num_beads + 1):
        # Initialize the minimum value for the current bead to be the head value
        min_value[i] = beads[i - 1]

        # Loop through each merge combination for the current bead
        for j in range(i):
            # Get the product of the head value of the current bead and the tail value of the
            # previous bead
            product = beads[i - 1] * beads[j]

            # Update the maximum energy for the current merge combination
            max_energy[i] = max(max_energy[i], max_energy[j] + product)

            # Update the minimum value for the current bead
            min_value[i] = min(min_value[i], min_value[j] + product)

    # Return the maximum energy for the final merge combination
    return max_energy[num_beads]
def test_max_energy():
    assert max_energy([2, 3, 5, 10]) == 710, "Testcase 1 failed"
    assert max_energy([1, 2, 3, 4]) == 80, "Testcase 2 failed"
    assert max_energy([4, 4, 4, 4]) == 192, "Testcase 3 failed"
    assert max_energy([30, 40, 50, 60]) == 372000, "Testcase 4 failed"
    print("All testcases passed")

# Call the test function
test_max_energy()