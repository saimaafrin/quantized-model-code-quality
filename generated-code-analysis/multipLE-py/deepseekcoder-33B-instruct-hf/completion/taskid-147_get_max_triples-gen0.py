def get_max_triples(n: int) -> int:
    """
    You are given a positive integer n. You have to create an integer array a of length n.
        For each i (1 ≤ i ≤ n), the value of a[i] = i * i - i + 1.
        Return the number of triples (a[i], a[j], a[k]) of a where i < j < k, 
    and a[i] + a[j] + a[k] is a multiple of 3.

    Example :
    >>> get_max_triples(5)
    1
        Explanation: 
        a = [1, 3, 7, 13, 21]
        The only valid triple is (1, 7, 13).
    """

    triples = [i * i - i + 1 for i in range(1, n + 1)]
    counter = 0
    for i in range(len(triples)):
        for j in range(i + 1, len(triples)):
            for k in range(j + 1, len(triples)):
                if (triples[i] + triples[j] + triples[k]) % 3 == 0:
                    counter += 1
    return counter
