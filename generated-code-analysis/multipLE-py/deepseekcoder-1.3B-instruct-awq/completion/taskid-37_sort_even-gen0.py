from typing import List

def sort_even(l: List[int]) -> List[int]:
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """

    # sort the elements at even indices
    even_sorted = sorted(l[::2])

    # copy the elements at odd indices, but replace the ones at even indices
    result = [None]*len(l)
    for i in range(len(l)):
        if i % 2 == 0:
            result[i] = l[i]
        else:
            result[i] = even_sorted.pop(0)
    return result
