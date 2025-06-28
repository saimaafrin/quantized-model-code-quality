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

    def check_rotation(s1, s2):
        return s1 in s2

    def rotate_string(s):
        return s[-1] + s[:-1]

    rotated_b = b
    for _ in range(len(b)):
        if check_rotation(a, rotated_b):
            return True
        rotated_b = rotate_string(rotated_b)
    return False
