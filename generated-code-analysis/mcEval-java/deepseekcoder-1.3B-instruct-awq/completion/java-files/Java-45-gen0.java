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
    if (n < 10) {
      return n + 1;
    }

    String numStr = String.valueOf(n);
    char[] numChars = numStr.toCharArray();
    int[] numCount = new int[10];

    for (char c : numChars) {
      numCount[Character.getNumericValue(c)]++;
    }

    for (int i = 0; i < 10; i += 2) {
      if (numCount[i] > 0 && numCount[i + 1] > 0) {
        numCount[i]--;
        numCount[i + 1]--;
        numStr = String.valueOf(i) + numStr.replace("0", String.valueOf(i + 1));
      }
   
      if (numStr.charAt(0) != '0') {
        break;
      }
    }

    if (numStr.charAt(0) == '0') {
      return -1;
    }

    return Integer.parseInt(numStr);
  }
  public static void main(String[] args) {
    assert findSmallestInteger(123) == 132;
    assert findSmallestInteger(531) == -1;
    assert findSmallestInteger(2071) == 2107;

    System.out.println("All tests passed");
  }
}