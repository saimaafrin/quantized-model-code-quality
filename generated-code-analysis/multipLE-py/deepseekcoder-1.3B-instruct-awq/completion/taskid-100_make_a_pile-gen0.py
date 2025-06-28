from typing import List

def make_a_pile(n: int) -> List[int]:
    """
    Given a positive integer n, you have to make a pile of n levels of stones.
    The first level has n stones.
    The number of stones in the next level is:
        - the next odd number if n is odd.
        - the next even number if n is even.
    Return the number of stones in each level in a list, where element at index
    i represents the number of stones in the level (i+1).

    Examples:
    >>> make_a_pile(3)
    [3, 5, 7]
    """


    # Initialize pile with n stones
    pile = [n]
    # While we still have more than 0 stones
    while pile[-1] > 0:
        # If pile is odd
        if pile[-1] % 2 == 1:
            # Add the next odd number to pile
            pile.append(pile[-1] + 1)
        else:
            # Otherwise, add the next even number
            pile.append(pile[-1] + 2)
    # Return the number of stones in each level
    return pile
