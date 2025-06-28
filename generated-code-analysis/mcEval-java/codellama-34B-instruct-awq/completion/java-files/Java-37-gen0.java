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
    if (n <= 0) {
      return 0;
    }

    String str = Integer.toString(n);
    char[] digits = str.toCharArray();
    int i = 0;
    int count = 0;
    for (; i < digits.length - 1; i++) {
      if (digits[i] == '0') {
        continue;
      }

      if (digits[i] == '1') {
        count += (int) Math.pow(10, digits.length - i - 1) + (digits[i + 1] - '0') * (int) Math.pow(10, digits.length - i - 2);
      } else {
        count += (digits[i] - '0') * (int) Math.pow(10, digits.length - i - 1);
      }
    }

    if (digits[i] == '1') {
      count += 1;
    } else {
      count += (digits[i] - '0');
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