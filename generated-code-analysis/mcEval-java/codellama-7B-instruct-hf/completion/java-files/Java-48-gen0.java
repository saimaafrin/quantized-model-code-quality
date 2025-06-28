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
    int[] uglyNumbers = new int[n];
    uglyNumbers[0] = 1;

    int index2 = 0;
    int index3 = 0;
    int index5 = 0;

    for (int i = 1; i < n; i++) {
      int min = Math.min(Math.min(2 * uglyNumbers[index2], 3 * uglyNumbers[index3]), 5 * uglyNumbers[index5]);
      uglyNumbers[i] = min;

      if (min == 2 * uglyNumbers[index2]) {
        index2++;
      }
      if (min == 3 * uglyNumbers[index3]) {
        index3++;
      }
      if (min == 5 * uglyNumbers[index5]) {
        index5++;
      }
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
