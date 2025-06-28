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
    int[] digits = new int[10];
    int count = 0;
    int smallest = -1;

    while (n > 0) {
      digits[count++] = n % 10;
      n = n / 10;
    }

    for (int i = 9; i >= 0; i--) {
      if (digits[i] > 0) {
        for (int j = i + 1; j < 10; j++) {
          if (digits[j] > 0) {
            digits[i]--;
            digits[j]++;
            smallest = digits[0] * 10 + digits[1] * 100 + digits[2] * 1000 + digits[3] * 10000;
          }
        }
      }
    }

    return smallest;
  }
  public static void main(String[] args) {
    assert findSmallestInteger(123) == 132;
    assert findSmallestInteger(531) == -1;
    assert findSmallestInteger(2071) == 2107;

    System.out.println("All tests passed");
  }
}