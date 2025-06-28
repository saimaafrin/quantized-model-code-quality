from typing import List

def sort_third(l: List[int]) -> List[int]:
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indicies that are not divisible by three, while its values at the indicies that are divisible by three are equal
    to the values of the corresponding indicies of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    """

    length = len(l)
    l_ind = 0
    l_ind_two = 1
    l_ind_three = 2
    i = 0
    while l_ind < length:
        if i % 3 != 0:
            l[l_ind] = l[l_ind_two]
            l[l_ind_two] = l[l_ind_three]
            l[l_ind_three] = l[l_ind]
            i += 1
            l_ind += 1
            l_ind_two += 1
            l_ind_three += 1
        else:
            i += 1
            l_ind += 1
            l_ind_two += 1
            l_ind_three += 1
    return l
