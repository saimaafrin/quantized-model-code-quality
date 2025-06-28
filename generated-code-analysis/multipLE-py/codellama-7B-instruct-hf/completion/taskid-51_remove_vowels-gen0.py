def remove_vowels(text: str) -> str:
    """
    remove_vowels is a function that takes string and returns string without vowels.
    >>> remove_vowels('')
    ''
    >>> remove_vowels('abcdef')
    'bcdf'
    >>> remove_vowels('aaaaa')
    ''
    >>> remove_vowels('aaBAA')
    'B'
    >>> remove_vowels('zbcd')
    'zbcd'
    """

    vowels = ['a', 'e', 'i', 'o', 'u']
    text_list = list(text)
    for v in vowels:
        for i in range(len(text_list)):
            if text_list[i] == v:
                text_list[i] = ''
    return ''.join(text_list)
