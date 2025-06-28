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
    // Convert the integer to a string array of digits
    char[] digits = Integer.toString(n).toCharArray();

    // Sort the digits in ascending order
    Arrays.sort(digits);

    // Try each permutation from the smallest to the largest
    for (int i = 1; i < digits.length; i++) {
      if (digits[i - 1] != digits[i]) {
        // Swap the first digit that is greater than its successor
        char temp = digits[i - 1];
        digits[i - 1] = digits[i];
        digits[i] = temp;

        // Convert the string back to an integer
        try {
          return Integer.parseInt(new String(digits));
        } catch (NumberFormatException e) {
          // Ignore any exception and try the next permutation
        }
      }
    }

    // No valid permutation found, return -1
    return -1;
  }
  public static void main(String[] args) {
    assert findSmallestInteger(123) == 132;
    assert findSmallestInteger(531) == -1;
    assert findSmallestInteger(2071) == 2107;

    System.out.println("All tests passed");
  }
}