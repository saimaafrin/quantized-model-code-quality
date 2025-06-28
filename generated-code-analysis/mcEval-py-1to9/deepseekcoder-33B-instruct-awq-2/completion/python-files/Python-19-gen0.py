
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
    if len(beads) == 1:
        return 0

    from collections import defaultdict

    # Store the max energy for each segment length
    dp = defaultdict(lambda: defaultdict(int))
    beads_count = len(beads)
    # iterate over length of segment
    for length in range(1, beads_count):
        # iterate over start index of segment
        for start in range(beads_count):
            end = (start + length) % beads_count
            # iterate over split point of segment
            for split in range(length):
                # calculate energy of split segment
                energy = dp[start][(split + length - 1) % length] + dp[(start + split + 1) % beads_count][(length + start - split - 1) % length] + beads[start] * beads[(start + split + 1) % beads_count] * beads[end]
                # update max energy for segment length
                if dp[start][length] < energy:
                    dp[start][length] = energy
    return max(dp[0].values())
def test_max_energy():
    assert max_energy([2, 3, 5, 10]) == 710, "Testcase 1 failed"
    assert max_energy([1, 2, 3, 4]) == 80, "Testcase 2 failed"
    assert max_energy([4, 4, 4, 4]) == 192, "Testcase 3 failed"
    assert max_energy([30, 40, 50, 60]) == 372000, "Testcase 4 failed"
    print("All testcases passed")

# Call the test function
test_max_energy()