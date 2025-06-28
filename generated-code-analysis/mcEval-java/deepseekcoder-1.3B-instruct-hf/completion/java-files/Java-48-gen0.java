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
      throw new IllegalArgumentException("Input must be a positive integer");
    }

    int[] ugly = new int[n];
    ugly[0] = 1;

    int i2 = 0, i3 = 0, i5 = 0;
    int nextUgly = 1;

    while (nextUgly < n) {
      ugly[nextUgly] = Math.min(ugly[i2] * 2, Math.min(ugly[i3] * 3, ugly[i5] * 5));

      if (ugly[nextUgly] == ugly[i2] * 2) {
        i2++;
      }
      if (ugly[nextUgly] == ugly[i3] * 3) {
        i3++;
      }
      if (ugly[nextUgly] == ugly[i5] * 5) {
        i5++;
      }

      nextUgly++;
    }

    return ugly[n - 1];
  }
  public static void main(String[] args) {
    assert findNthUglyNumber(1) == 1 : "Test case 1 failed";
    assert findNthUglyNumber(7) == 8 : "Test case 2 failed";
    assert findNthUglyNumber(15) == 24 : "Test case 3 failed";

    System.out.println("All tests passed");
  }
}
