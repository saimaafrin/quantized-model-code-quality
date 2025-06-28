import java.util.Map;
import java.util.HashMap;
import java.util.Arrays;

class Problem {
    /**
     * Given an array of integers nums and an integer target,
     * find two numbers such that they add up to target and return their indices.
     * You may assume that each input would have exactly one solution,
     * and you may not use the same element twice.
     * You can return the answer in any order.
     *
     * Example 1:
     * Input: nums = [2,7,11,15], target = 9
     * Output: [0,1]
     * Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
     *
     * Example 2:
     * Input: nums = [3,2,4], target = 6
     * Output: [1,2]
     *
     * Example 3:
     * Input: nums = [3,3], target = 6
     * Output: [0,1]
     */
  public int[] twoSum(int[] nums, int target)  {
      Map<Integer, Integer> map = new HashMap<Integer, Integer>();
      for (int i = 0; i < nums.length; i++) {
          int complement = target - nums[i];
          if (map.containsKey(complement)) {
              return new int[]{map.get(complement), i};
          }
          map.put(nums[i], i);
      }
      throw new IllegalArgumentException("No two sum solution");
  }
  public static void main(String[] args) {
    Problem solution = new Problem();

    // Test the function with different test cases
    assert Arrays.equals(
      solution.twoSum(new int[] { 1, 3, 7, 9, 2 }, 11),
      new int[] { 3, 4 }
    );
    assert Arrays.equals(
      solution.twoSum(new int[] { 1, 5, 3, 7, 8 }, 9),
      new int[] { 0, 4 }
    );
    assert Arrays.equals(
      solution.twoSum(new int[] { 10, 20, 30, 40, 50 }, 90),
      new int[] { 3, 4 }
    );
    System.out.println("All tests passed");
  }
}