import java.util.HashMap;
import java.util.Map;

class Problem {

  /**
   * Given an integer array nums where every element appears three times except for one, which appears only once. Find and return the element that appears only once.
   *
   * @param nums An integer array where every element appears three times except for one.
   * @return The element that appears only once.
   *
   * Example:
   * singleNumber(new int[]{2,2,3,2})
   * Output: 3
   *
   * Example:
   * singleNumber(new int[]{0,1,0,1,0,1,99})
   * Output: 99
   */
  public static int singleNumber(int[] nums)  {
    int xor = 0;
    for (int i = 0; i < nums.length; i++) {
      xor ^= nums[i];
    }
    return xor;
  }
  public static void main(String[] args) {
    assert singleNumber(new int[] { 6, 1, 6, 6 }) == 1 : "Test case 1 failed";
    assert singleNumber(new int[] { 22, 22, 22, 11, 11, 11, 55 }) ==
    55 : "Test case 2 failed";
    assert singleNumber(new int[] { -1, 3, -1, 3, -1, 3, 99 }) ==
    99 : "Test case 3 failed";
    System.out.println("All tests passed");
  }
}