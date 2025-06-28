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
    # Initial number of cigarettes
    total_cigarettes = n
    # Number of butts needed for the first cigarette
    butts_needed = k

    while True:
        # Number of cigarettes gotten by exchanging butts
        new_cigarettes = butts_needed
        # Add the new cigarettes to the total
        total_cigarettes += new_cigarettes
        # The new butts needed to get a new cigarette is the number of new cigarettes gotten plus the remaining butts needed for the first cigarette
        butts_needed = new_cigarettes + butts_needed - k
        # If no more cigarettes can be gotten, break the loop
        if new_cigarettes < k:
            break

    return total_cigarettes
assert total_smoked_cigarettes(4, 3) == 5
assert total_smoked_cigarettes(10, 3) == 14
assert total_smoked_cigarettes(1, 2) == 1  # Peter cannot exchange butts as he starts with less than k
assert total_smoked_cigarettes(20, 4) == 26
assert total_smoked_cigarettes(0, 5) == 0  # Peter starts with no cigarettes