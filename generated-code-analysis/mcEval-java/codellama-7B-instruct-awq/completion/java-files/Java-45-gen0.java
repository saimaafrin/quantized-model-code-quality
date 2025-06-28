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

    // Find the number of digits in the input number
    int numberOfDigits = 0;
    while (n > 0) {
      n /= 10;
      numberOfDigits++;
    }

    // Initialize the smallest number
    int smallestNumber = -1;

    // Start with the input number
    int number = n;

    // Iterate through each digit in the input number
    for (int i = 0; i < numberOfDigits; i++) {

      // Find the last digit in the current number
      int lastDigit = number % 10;

      // Remove the last digit from the current number
      number = number / 10;

      // Add the last digit to the end of the number
      number = number * 10 + lastDigit;

      // Check if the current number is greater than the smallest number
      if (number > smallestNumber) {

        // Update the smallest number
        smallestNumber = number;
      }
    }

    // Return the smallest number
    return smallestNumber;
  }
  public static void main(String[] args) {
    assert findSmallestInteger(123) == 132;
    assert findSmallestInteger(531) == -1;
    assert findSmallestInteger(2071) == 2107;

    System.out.println("All tests passed");
  }
}