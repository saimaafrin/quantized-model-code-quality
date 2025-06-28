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

    a = [i * i - i + 1 for i in range(1, n + 1)]
    mod_count = [0] * 3
    for num in a:
        mod_count[num % 3] += 1
    total_count = mod_count[0] * (mod_count[0] - 1) * (mod_count[0] - 2) // 6
    total_count += mod_count[1] * (mod_count[1] - 1) // 2 * mod_count[2]
    total_count += mod_count[2] * (mod_count[2] - 1) // 2 * mod_count[1]
    return total_count
