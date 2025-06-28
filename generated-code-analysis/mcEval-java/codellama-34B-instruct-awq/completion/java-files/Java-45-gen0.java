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
    int[] digits = String.valueOf(n).chars().map(Character::getNumericValue).sorted().toArray();
    int smallestNumber = 0;
    while (n != 0) {
      smallestNumber = smallestNumber * 10 + n % 10;
      n /= 10;
    }
    smallestNumber = Arrays.stream(digits).reduce(0, (i, j) -> i * 10 + j);
    return smallestNumber;
  }
  public static void main(String[] args) {
    assert findSmallestInteger(123) == 132;
    assert findSmallestInteger(531) == -1;
    assert findSmallestInteger(2071) == 2107;

    System.out.println("All tests passed");
  }
}