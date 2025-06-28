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
    // Convert the given number into a char array
    char[] digits = Integer.toString(n).toCharArray();

    // Sort the char array in ascending order
    Arrays.sort(digits);

    // Iterate over the sorted digits
    for (int i = 0; i < digits.length; i++) {
      // If the digit is not '0', it's the start of the rearranged integer
      if (digits[i] != '0') {
        // Swap the first non-zero digit with the first zero (if any)
        if (i > 0) {
          char temp = digits[i];
          digits[i] = digits[0];
          digits[0] = temp;
        }

        // Convert the char array back into an integer and return it
        return Integer.parseInt(new String(digits));
      }
    }

    // If no solution exists, return -1
    return -1;
  }
  public static void main(String[] args) {
    assert findSmallestInteger(123) == 132;
    assert findSmallestInteger(531) == -1;
    assert findSmallestInteger(2071) == 2107;

    System.out.println("All tests passed");
  }
}