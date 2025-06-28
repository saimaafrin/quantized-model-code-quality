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
    int len = (int)(Math.log10(n)) + 1;
    int[] digits = new int[len];
    int i = 0;
    while (n > 0) {
      digits[i++] = n % 10;
      n /= 10;
    }

    for (int k = 0; k < len; k++) {
      for (int j = k + 1; j < len; j++) {
        if (digits[j] < digits[k]) {
          int temp = digits[j];
          digits[j] = digits[k];
          digits[k] = temp;
        }
      }
    }
    int num = 0;
    for (int j = 0; j < len; j++) {
      num = num * 10 + digits[j];
    }
    if (num > n) {
      return num;
    } else {
      return -1;
    }
  }
  public static void main(String[] args) {
    assert findSmallestInteger(123) == 132;
    assert findSmallestInteger(531) == -1;
    assert findSmallestInteger(2071) == 2107;

    System.out.println("All tests passed");
  }
}