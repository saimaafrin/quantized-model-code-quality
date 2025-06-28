def is_bored(S: str) -> int:
    """
    You'll be given a string of words, and your task is to count the number
    of boredoms. A boredom is a sentence that starts with the word "I".
    Sentences are delimited by '.', '?' or '!'.
   
    For example:
    >>> is_bored('Hello world')
    0
    >>> is_bored('The sky is blue. The sun is shining. I love this weather')
    1
    """

    total_boredoms = 0
    for sentence in S.split('.'):
        if sentence.startswith('I'):
            total_boredoms += 1
        for delim in ['.', '?', '!']:
            if sentence.endswith(delim):
                sentence = sentence[:-1]
    return total_boredoms
