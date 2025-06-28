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
    // Create a map to store the number of occurrences of each element in nums.
    Map<Integer, Integer> numCounts = new HashMap<>();

    // Iterate over nums and update the count of each element in numCounts.
    for (int num : nums) {
      numCounts.put(num, numCounts.getOrDefault(num, 0) + 1);
    }

    // Iterate over the keys in numCounts. The key that has a count of 1 is the element that appears only once.
    for (int key : numCounts.keySet()) {
      if (numCounts.get(key) == 1) {
        return key;
      }
    }

    // If no such key is found, return -1.
    return -1;
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