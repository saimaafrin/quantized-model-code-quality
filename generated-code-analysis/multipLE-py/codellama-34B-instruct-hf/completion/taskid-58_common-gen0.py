from typing import List

def common(l1: List[int], l2: List[int]) -> List[int]:
    """Return sorted unique common elements for two lists.
    >>> common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
    [1, 5, 653]
    >>> common([5, 3, 2, 8], [3, 2])
    [2, 3]

    """


    common_elements = []
    l1_dict = {}

    for item in l1:
        if item not in l1_dict:
            l1_dict[item] = 1
        else:
            l1_dict[item] += 1

    for item in l2:
        if item in l1_dict:
            common_elements.append(item)
            l1_dict[item] -= 1
            if l1_dict[item] == 0:
                del l1_dict[item]

    return sorted(common_elements)
