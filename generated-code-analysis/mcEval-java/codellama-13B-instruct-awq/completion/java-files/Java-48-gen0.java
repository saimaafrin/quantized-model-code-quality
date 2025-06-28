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
    // Initialize variables
    int[] ugly = new int[n];
    int currentIndex = 0;

    // Find the first ugly number
    int number = 1;
    ugly[currentIndex] = number;
    currentIndex++;

    // Find the remaining ugly numbers
    while (currentIndex < n) {
      number = ugly[0] * 2;
      for (int i = 1; i < currentIndex; i++) {
        int nextNumber = ugly[i] * 2;
        if (nextNumber < number) {
          number = nextNumber;
        }
      }
      ugly[currentIndex] = number;
      currentIndex++;
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
