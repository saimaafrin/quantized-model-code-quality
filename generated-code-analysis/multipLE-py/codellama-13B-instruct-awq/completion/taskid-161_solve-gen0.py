def solve(s: str) -> str:
    """You are given a string s.
    if s[i] is a letter, reverse its case from lower to upper or vise versa, 
    otherwise keep it as it is.
    If the string contains no letters, reverse the string.
    The function should return the resulted string.
    Examples
    >>> solve('1234')
    '4321'
    >>> solve('ab')
    'AB'
    >>> solve('#a@C')
    '#A@c'
    """

    res = ""
    res_list = []
    res_list.reverse()
    for i in s:
        if i.isalpha():
            if i.islower():
                res_list.append(i.upper())
            else:
                res_list.append(i.lower())
        else:
            res_list.append(i)
    for j in res_list:
        res += j
    return res
