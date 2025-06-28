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
    ugly[0] = 1;
    int i2 = 0, i3 = 0, i5 = 0;
    int nextMultipleOf2 = 2;
    int nextMultipleOf3 = 3;
    int nextMultipleOf5 = 5;
    int nextUglyNumber = 1;

    for(int i=1; i<n; i++)
    {
      nextUglyNumber = Math.min(nextMultipleOf2, Math.min(nextMultipleOf3, nextMultipleOf5));
      ugly[i] = nextUglyNumber;
      if(nextUglyNumber == nextMultipleOf2)
      {
        i2 = i2+1;
        nextMultipleOf2 = ugly[i2]*2;
      }
      if(nextUglyNumber == nextMultipleOf3)
      {
        i3 = i3+1;
        nextMultipleOf3 = ugly[i3]*3;
      }
      if(nextUglyNumber == nextMultipleOf5)
      {
        i5 = i5+1;
        nextMultipleOf5 = ugly[i5]*5;
      }
    }

    return nextUglyNumber;
  }
  public static void main(String[] args) {
    assert findNthUglyNumber(1) == 1 : "Test case 1 failed";
    assert findNthUglyNumber(7) == 8 : "Test case 2 failed";
    assert findNthUglyNumber(15) == 24 : "Test case 3 failed";

    System.out.println("All tests passed");
  }
}
