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

    # Your code here
    l_prime = []
    for i in range(len(l)):
        if i % 3 == 0:
            l_prime.append(l[i])
        else:
            l_prime.append(l[i])
    l_prime.sort()
    l_prime_prime = []
    for i in range(len(l)):
        if i % 3 == 0:
            l_prime_prime.append(l_prime[i])
        else:
            l_prime_prime.append(l[i])
    return l_prime_prime
