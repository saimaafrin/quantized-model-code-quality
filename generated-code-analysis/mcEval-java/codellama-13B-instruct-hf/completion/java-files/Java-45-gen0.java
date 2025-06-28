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
    int smallestInteger = -1;

    int nDigits = (int) Math.log10(n) + 1;
    int[] nDigitsArray = new int[nDigits];

    for (int i = 0; i < nDigits; i++) {
      nDigitsArray[i] = n % 10;
      n /= 10;
    }

    // Check if any of the digits are 0
    if (Arrays.stream(nDigitsArray).anyMatch(digit -> digit == 0)) {
      return -1;
    }

    // Arrange the digits in descending order
    Arrays.sort(nDigitsArray);

    int largestDigit = nDigitsArray[nDigitsArray.length - 1];

    int smallestPossibleInteger = 0;
    for (int i = 0; i < nDigitsArray.length; i++) {
      if (i == 0) {
        smallestPossibleInteger += largestDigit;
      } else {
        smallestPossibleInteger += nDigitsArray[i];
      }
    }

    smallestInteger = smallestPossibleInteger;

    return smallestInteger;
  }
  public static void main(String[] args) {
    assert findSmallestInteger(123) == 132;
    assert findSmallestInteger(531) == -1;
    assert findSmallestInteger(2071) == 2107;

    System.out.println("All tests passed");
  }
}