class Problem {

  /**
   * Calculate the number of times the digit 1 appears in all non-negative integers less than or equal to n.
   *
   * @param n An integer representing the upper limit.
   * @return The number of times the digit 1 appears.
   *
   * Example:
   * countDigitOne(13)
   * Output: 6
   *
   * Example:
   * countDigitOne(0)
   * Output: 0
   */
  public static int countDigitOne(int n)  {
    long k = 1;
    int c = 0;
    while (n >= k) {
      c += (n / (k * 10)) * k + Math.min(Math.max(n % (k * 10) - k + 1, 0), k);
      k *= 10;
    }
    return c;
  }
  public static void main(String[] args) {
    assert countDigitOne(20) == 12 : "Test case 1 failed";
    assert countDigitOne(55) == 16 : "Test case 2 failed";
    assert countDigitOne(99) == 20 : "Test case 3 failed";
    System.out.println("All tests passed");
  }
}