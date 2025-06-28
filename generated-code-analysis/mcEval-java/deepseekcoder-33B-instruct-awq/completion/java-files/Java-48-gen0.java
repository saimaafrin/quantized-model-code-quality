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

    int nextMultipleOf2 = 2;
    int nextMultipleOf3 = 3;
    int nextMultipleOf5 = 5;

    for (int i = 1; i < n; i++) {
      int nextUglyNumber = Math.min(nextMultipleOf2, Math.min(nextMultipleOf3, nextMultipleOf5));

      uglyNumbers[i] = nextUglyNumber;

      if (nextUglyNumber == nextMultipleOf2) {
        index2++;
        nextMultipleOf2 = uglyNumbers[index2] * 2;
      }

      if (nextUglyNumber == nextMultipleOf3) {
        index3++;
        nextMultipleOf3 = uglyNumbers[index3] * 3;
      }

      if (nextUglyNumber == nextMultipleOf5) {
        index5++;
        nextMultipleOf5 = uglyNumbers[index5] * 5;
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
