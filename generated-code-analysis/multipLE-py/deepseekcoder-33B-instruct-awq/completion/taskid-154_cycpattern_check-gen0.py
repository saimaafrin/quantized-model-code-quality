def cycpattern_check(a: str, b: str) -> bool:
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    >>> cycpattern_check('abcd', 'abd')
    False
    >>> cycpattern_check('hello', 'ell')
    True
    >>> cycpattern_check('whassup', 'psus')
    False
    >>> cycpattern_check('abab', 'baa')
    True
    >>> cycpattern_check('efef', 'eeff')
    False
    >>> cycpattern_check('himenss', 'simen')
    True

    """


    # length of both the strings
    n = len(a)
    m = len(b)

    # all cyclic rotations of the second word
    cyclic_rots = [b[i:] + b[:i] for i in range(m)]

    for rot in cyclic_rots:
        if rot in a:
            return True

    return False
