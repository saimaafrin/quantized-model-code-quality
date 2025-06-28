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
    int count = 0;
    String strN = Integer.toString(n);
    for(int i = 0; i < strN.length(); i++) {
      if (strN.charAt(i) == '1') {
        count++;
      }
   
      if (strN.charAt(i) > '0' && strN.charAt(i) <= '9') {
        return count;
      }
    }
    return count;
  }
  public static void main(String[] args) {
    assert countDigitOne(20) == 12 : "Test case 1 failed";
    assert countDigitOne(55) == 16 : "Test case 2 failed";
    assert countDigitOne(99) == 20 : "Test case 3 failed";
    System.out.println("All tests passed");
  }
}