class Problem {

  /**
   * Given an integer n, return the minimum number of perfect square numbers that sum up to n.
   *
   * @param n The target integer.
   * @return The minimum number of perfect square numbers.
   *
   * Example:
   * minPerfectSquareSum(12)
   * Output: 3
   *
   * Example:
   * minPerfectSquareSum(13)
   * Output: 2
   */
  public static int minPerfectSquareSum(int n)  {
    // 1. Brute Force (TLE)
    // for (int i = 1; i <= n; i++) {
    //   int sum = 0;
    //   for (int j = 1; j <= i; j++) {
    //     sum += Math.pow(j, 2);
    //   }
    //   if (sum == n) return i;
    // }
    // return 0;

    // 2. Sort + Two Pointers
    int[] squares = new int[n + 1];
    for (int i = 1; i <= n; i++) {
      squares[i] = (int) Math.pow(i, 2);
    }
    Arrays.sort(squares);

    int minSquares = 0;
    int left = 1;
    int right = n;
    while (left <= right) {
      int sum = squares[left] + squares[right];
      if (sum == n) {
        minSquares = Math.min(minSquares, right - left + 1);
        left++;
        right--;
      } else if (sum > n) {
        right--;
      } else {
        left++;
      }
    }

    return minSquares;
  }
  public static void main(String[] args) {
    assert minPerfectSquareSum(26) == 2 : "Test case 1 failed";
    assert minPerfectSquareSum(17) == 2 : "Test case 2 failed";
    assert minPerfectSquareSum(99) == 3 : "Test case 3 failed";
    System.out.println("All tests passed");
  }
}