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
    if (n <= 0) {
      return 0;
    }

    int[] dp = new int[n + 1];
    dp[0] = 0;
    dp[1] = 1;

    for (int i = 2; i <= n; i++) {
      int sqrt = (int) Math.sqrt(i);
      if (sqrt * sqrt == i) {
        dp[i] = 1;
      } else {
        int min = Integer.MAX_VALUE;
        for (int j = 1; j * j <= i; j++) {
          min = Math.min(min, dp[i - j * j]);
        }
        dp[i] = min + 1;
      }
    }

    return dp[n];
  }
  public static void main(String[] args) {
    assert minPerfectSquareSum(26) == 2 : "Test case 1 failed";
    assert minPerfectSquareSum(17) == 2 : "Test case 2 failed";
    assert minPerfectSquareSum(99) == 3 : "Test case 3 failed";
    System.out.println("All tests passed");
  }
}