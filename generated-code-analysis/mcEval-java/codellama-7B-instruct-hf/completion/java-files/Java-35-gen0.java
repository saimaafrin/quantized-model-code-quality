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
    // Map to store the counts of the integers in nums.
    // If we are seeing an integer for the first time, set the count to 1.
    // If we are seeing an integer a second time, set the count to 2.
    // If we are seeing an integer a third time, set the count to 3.
    // If the count is 2, then we have seen this integer a second time, and it does not appear only once.
    // If the count is 3, then we have seen this integer a third time, and it does not appear only once.
    Map<Integer, Integer> counts = new HashMap<>();
    for (int i = 0; i < nums.length; i++) {
      if (!counts.containsKey(nums[i])) {
        counts.put(nums[i], 1);
      } else {
        counts.put(nums[i], counts.get(nums[i]) + 1);
      }
    }

    // Find the count for the integer that appears only once.
    int once = -1;
    for (int count : counts.values()) {
      if (count == 2) {
        once = -1;
        break;
      }
      if (count == 1) {
        once = counts.keySet().iterator().next();
        break;
      }
    }

    return once;
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