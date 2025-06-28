import java.lang.Math;

class Problem {

  /**
   * Find and return the nth ugly number.
   *
   * @param n The index of the ugly number to find.
   * @return The nth ugly number.
   *
   * Example:
   * findNthUglyNumber(10)
   * Output: 12
   */
  public static int findNthUglyNumber(int n)  {
    // Initialize a new array with a size of n to store the ugly numbers.
    int[] uglyNumbers = new int[n];
    // Set the first ugly number to 1.
    uglyNumbers[0] = 1;

    int nextUglyIndex = 1;
    int multiply2 = 0;
    int multiply3 = 0;
    int multiply5 = 0;

    while (nextUglyIndex < n) {
      int min = Math.min(uglyNumbers[multiply2] * 2, Math.min(uglyNumbers[multiply3] * 3, uglyNumbers[multiply5] * 5));

      uglyNumbers[nextUglyIndex] = min;

      while (uglyNumbers[multiply2] * 2 <= min) multiply2++;
      while (uglyNumbers[multiply3] * 3 <= min) multiply3++;
      while (uglyNumbers[multiply5] * 5 <= min) multiply5++;

      nextUglyIndex++;
    }
    return uglyNumbers[n - 1];
  }
  public static void main(String[] args) {
    assert findNthUglyNumber(1) == 1 : "Test case 1 failed";
    assert findNthUglyNumber(7) == 8 : "Test case 2 failed";
    assert findNthUglyNumber(15) == 24 : "Test case 3 failed";

    System.out.println("All tests passed");
  }
}
