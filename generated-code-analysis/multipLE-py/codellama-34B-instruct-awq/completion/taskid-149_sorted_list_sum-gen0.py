from typing import List

def sorted_list_sum(lst: List[str]) -> List[str]:
    """Write a function that accepts a list of strings as a parameter,
    deletes the strings that have odd lengths from it,
    and returns the resulted list with a sorted order,
    The list is always a list of strings and never an array of numbers,
    and it may contain duplicates.
    The order of the list should be ascending by length of each word, and you
    should return the list sorted by that rule.
    If two words have the same length, sort the list alphabetically.
    The function should return a list of strings in sorted order.
    You may assume that all words will have the same length.
    For example:
    >>> list_sort(['aa', 'a', 'aaa'])
    ['aa']
    >>> list_sort(['ab', 'a', 'aaa', 'cd'])
    ['ab', 'cd']
    """


    def sort_by_len(lst: List[str]) -> List[str]:
        return sorted(lst, key=len)

    def sort_by_word(lst: List[str]) -> List[str]:
        return sorted(lst)

    def sort_by_len_and_word(lst: List[str]) -> List[str]:
        return sort_by_len(sort_by_word(lst))

    def remove_odd_length(lst: List[str]) -> List[str]:
        return [word for word in lst if len(word) % 2 == 0]

    def sorted_list_sum(lst: List[str]) -> List[str]:
        return sort_by_len_and_word(remove_odd_length(lst))
