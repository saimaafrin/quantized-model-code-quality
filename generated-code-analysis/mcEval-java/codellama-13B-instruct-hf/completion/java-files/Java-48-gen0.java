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
    int[] ugly = new int[n];
    int i2 = 0, i3 = 0, i5 = 0;
    int next_ugly = 1;
    int min = 1;
    for (int i = 0; i < n; i++) {
      ugly[i] = next_ugly;
      next_ugly = min * 2;
      min = Math.min(next_ugly, min);
      i2++;
      while (ugly[i2] * 2 <= min) {
        i2++;
      }
      i3++;
      while (ugly[i3] * 3 <= min) {
        i3++;
      }
      i5++;
      while (ugly[i5] * 5 <= min) {
        i5++;
      }
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
