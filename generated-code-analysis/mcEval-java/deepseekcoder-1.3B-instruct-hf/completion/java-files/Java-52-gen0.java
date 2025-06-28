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
    // base case
    if(n <= 0) return 0;
    
    // Initialize dp[] array
    int[] dp = new int[n+1];
    
    // Initialize dp[0] to 0
    dp[0] = 0;
    
    // Initialize the dp[1] to 1
    dp[1] = 1;
    
    // Fill the dp[] array in a bottom-up manner
    for(int i=2; i<=n; i++) {
      dp[i] = i;
      for(int j=2; j*j<=i; j++) {
        dp[i] = Math.min(dp[i], dp[i-j*j]+1);
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