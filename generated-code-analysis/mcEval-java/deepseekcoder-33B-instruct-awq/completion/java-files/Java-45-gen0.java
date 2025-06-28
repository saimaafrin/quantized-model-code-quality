class Problem {

  /**
   * Find the smallest integer that can be formed by rearranging the digits of the given positive integer n, which is greater than n.
   *
   * @param n The input positive integer.
   * @return The smallest rearranged integer greater than n, or -1 if not possible.
   *
   * Example:
   * findSmallestInteger(12)
   * Output: 21
   */
  public static int findSmallestInteger(int n)  {
    int[] digits = new int[10];
    int numDigits = 0;

    // Count the frequency of each digit in the input number
    while (n > 0) {
      int digit = n % 10;
      digits[digit]++;
      n /= 10;
      numDigits++;
    }

    int result = 0;
    int multiplier = 1;

    // Find the first digit that can be decreased
    for (int i = 1; i < 10; i++) {
      if (digits[i] > 0) {
        digits[i]--;
        result += i * multiplier;
        multiplier *= 10;
        break;
      }
    }

    // Fill the remaining digits in increasing order
    for (int i = 0; i < 10; i++) {
      while (digits[i] > 0) {
        result += i * multiplier;
        multiplier *= 10;
        digits[i]--;
      }
    }

    // Check if the result has the same number of digits as the input number
    return (int) (result / Math.pow(10, numDigits - 1)) > 0 ? result : -1;
  }
  public static void main(String[] args) {
    assert findSmallestInteger(123) == 132;
    assert findSmallestInteger(531) == -1;
    assert findSmallestInteger(2071) == 2107;

    System.out.println("All tests passed");
  }
}