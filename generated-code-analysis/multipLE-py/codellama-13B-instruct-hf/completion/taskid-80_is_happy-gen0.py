def is_happy(s: str) -> bool:
    """You are given a string s.
    Your task is to check if the string is happy or not.
    A string is happy if its length is at least 3 and every 3 consecutive letters are distinct
    For example:
    >>> is_happy('a')
    False
    >>> is_happy('aa')
    False
    >>> is_happy('abcd')
    True
    >>> is_happy('aabb')
    False
    >>> is_happy('adb')
    True
    >>> is_happy('xyy')
    False
    """

    if len(s) < 3:
        return False

    # If every 3 consecutive letters are distinct, return True
    # If the length is less than 3, return False
    for i in range(len(s) - 2):
        if s[i : i + 3] in s[i + 1 :]:
            return False
    return True
