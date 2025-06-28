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

    def is_power_of_3(n: int) -> bool:
        return n > 0 and 3 ** (n.bit_length() - 1) == n

    count = 0
    for i in range(1, n):
        for j in range(i + 1, n):
            k = (3 * i + j) // 2
            if i < k <= j and is_power_of_3(i + j + k):
                count += 1
    return count
