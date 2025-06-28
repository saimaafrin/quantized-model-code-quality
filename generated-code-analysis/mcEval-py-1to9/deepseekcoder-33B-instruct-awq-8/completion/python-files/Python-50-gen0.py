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
    if k > n:
        return n
    else:
        # calculate the number of cigarettes can be smoked with initial cigarettes and cigarette butts
        # and the remaining cigarette butts can be exchanged for new cigarettes
        cigarettes = n + (n // k)
        # calculate the remaining cigarette butts after exchanging for new cigarettes
        remaining_butts = (n % k) + (n // k)
        # keep exchanging the remaining cigarette butts for new cigarettes
        while remaining_butts >= k:
            cigarettes += remaining_butts // k
            remaining_butts = (remaining_butts % k) + (remaining_butts // k)
        return cigarettes
assert total_smoked_cigarettes(4, 3) == 5
assert total_smoked_cigarettes(10, 3) == 14
assert total_smoked_cigarettes(1, 2) == 1  # Peter cannot exchange butts as he starts with less than k
assert total_smoked_cigarettes(20, 4) == 26
assert total_smoked_cigarettes(0, 5) == 0  # Peter starts with no cigarettes