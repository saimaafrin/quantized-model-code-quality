def total_smoked_cigarettes(n, k):
    """
    Calculates the total number of cigarettes Peter can smoke.
    Peter starts with n cigarettes and can exchange k butts for one new cigarette.
    The function takes two arguments, n and k, where n is the initial number of cigarettes,
    and k is the number of cigarette butts needed to exchange for one new cigarette.
    The function returns the total number of cigarettes Peter can smoke.
    Example:
    >>> total_smoked_cigarettes(4, 3)
        5
    >>> total_smoked_cigarettes(10, 3)
        14
    """
    # Initialize the total number of cigarettes
    total_cigarettes = n
    # Initialize the number of butts
    butts = n
    # Loop until there are no more butts to exchange
    while butts >= k:
        # Calculate the number of new cigarettes that can be exchanged
        new_cigarettes = butts // k
        # Add the new cigarettes to the total
        total_cigarettes += new_cigarettes
        # Calculate the remaining butts that can't be exchanged
        butts = butts % k + new_cigarettes
    # Return the total number of cigarettes
    return total_cigarettes
assert total_smoked_cigarettes(4, 3) == 5
assert total_smoked_cigarettes(10, 3) == 14
assert total_smoked_cigarettes(1, 2) == 1  # Peter cannot exchange butts as he starts with less than k
assert total_smoked_cigarettes(20, 4) == 26
assert total_smoked_cigarettes(0, 5) == 0  # Peter starts with no cigarettes