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
    if (n <= 0) {
      return 0;
    }
    int[] uglyNumbers = new int[n];
    uglyNumbers[0] = 1;
    int nextIndex = 1;
    int i2 = 0, i3 = 0, i5 = 0;
    while (nextIndex < n) {
      uglyNumbers[nextIndex] = Math.min(uglyNumbers[i2] * 2, Math.min(uglyNumbers[i3] * 3, uglyNumbers[i5] * 5));
      if (uglyNumbers[nextIndex] == uglyNumbers[i2] * 2) {
        i2++;
      }
      if (uglyNumbers[nextIndex] == uglyNumbers[i3] * 3) {
        i3++;
      }
      if (uglyNumbers[nextIndex] == uglyNumbers[i5] * 5) {
        i5++;
      }
      nextIndex++;
    }
    return uglyNumbers[nextIndex - 1];
  }
  public static void main(String[] args) {
    assert findNthUglyNumber(1) == 1 : "Test case 1 failed";
    assert findNthUglyNumber(7) == 8 : "Test case 2 failed";
    assert findNthUglyNumber(15) == 24 : "Test case 3 failed";

    System.out.println("All tests passed");
  }
}
