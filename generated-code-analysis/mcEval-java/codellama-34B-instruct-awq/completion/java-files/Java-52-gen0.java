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
    int numSquares = 0;
    for (int i = 1; i <= n; i++) {
      // The number of squares we've already added up.
      int sum = (i * i);
      // If the sum is less than or equal to n, we're done.
      if (sum > n) {
        // We need to add at least one more square.
        numSquares++;
        // Subtract the previous square.
        sum -= ((i - 1) * (i - 1));
        // And add the current square.
        sum += (i * i);
        if (sum <= n) {
          numSquares++;
        }
        break;
      }
      numSquares++;
    }
    return numSquares;
  }
  public static void main(String[] args) {
    assert minPerfectSquareSum(26) == 2 : "Test case 1 failed";
    assert minPerfectSquareSum(17) == 2 : "Test case 2 failed";
    assert minPerfectSquareSum(99) == 3 : "Test case 3 failed";
    System.out.println("All tests passed");
  }
}