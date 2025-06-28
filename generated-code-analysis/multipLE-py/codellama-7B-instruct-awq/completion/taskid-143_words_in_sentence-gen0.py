def words_in_sentence(sentence: str) -> str:
    """
    You are given a string representing a sentence,
    the sentence contains some words separated by a space,
    and you have to return a string that contains the words from the original sentence,
    whose lengths are prime numbers,
    the order of the words in the new string should be the same as the original one.

    Example 1:
    >>> words_in_sentence('This is a test')
    'is'

    Example 2:
    >>> words_in_sentence('lets go for swimming')
    'go for'
    
    Constraints:
        * 1 <= len(sentence) <= 100
        * sentence contains only letters
    """

    def is_prime_number(number: int) -> bool:
        if number <= 1:
            return False
        for i in range(2, number):
            if number % i == 0:
                return False
        return True

    def get_prime_words(sentence: str) -> str:
        words = sentence.split()
        prime_words = []
        for word in words:
            if is_prime_number(len(word)):
                prime_words.append(word)
        return ' '.join(prime_words)

    return get_prime_words(sentence)
