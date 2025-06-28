def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """


    # Map the numbers to integers
    numbers_dict = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}

    # Split the string into a list of words
    words = numbers.split()

    # Sort the list of words and map each word to its corresponding integer
    sorted_words = sorted(numbers_dict.get(word, word) for word in words)

    # Join the sorted list of words back into a string
    sorted_numbers = ' '.join(words)

    return sorted_numbers
