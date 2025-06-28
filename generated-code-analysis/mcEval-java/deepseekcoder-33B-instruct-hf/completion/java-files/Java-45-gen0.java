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
    char[] nums = (n + "").toCharArray();

    int i = nums.length - 1;
    while (i > 0 && nums[i - 1] >= nums[i]) {
      i--;
    }
    if (i == 0) {
      return -1;
    }

    int j = nums.length - 1;
    while (j > 0 && nums[j] <= nums[i - 1]) {
      j--;
    }

    swap(nums, i - 1, j);

    reverse(nums, i, nums.length - 1);

    try {
      return Integer.parseInt(new String(nums));
    } catch (NumberFormatException e) {
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