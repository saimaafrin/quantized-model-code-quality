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
    // Check for edge case of n=1, which will just return 1 as the 1st ugly number
    if (n == 1) {
      return 1;
    }

    // Start by initializing the first ugly number
    int currentUglyNumber = 1;
    // Keep track of the current number of ugly numbers found
    int foundUglyNumbers = 1;

    while (foundUglyNumbers < n) {
      // Increment the current ugly number by 1
      currentUglyNumber++;

      // Check if the current number is divisible by any of 2, 3, or 5
      // If it is, then it is an ugly number
      if (currentUglyNumber % 2 == 0 || currentUglyNumber % 3 == 0 || currentUglyNumber % 5 == 0) {
        foundUglyNumbers++;
      }
    }

    return currentUglyNumber;
  }
  public static void main(String[] args) {
    assert findNthUglyNumber(1) == 1 : "Test case 1 failed";
    assert findNthUglyNumber(7) == 8 : "Test case 2 failed";
    assert findNthUglyNumber(15) == 24 : "Test case 3 failed";

    System.out.println("All tests passed");
  }
}
