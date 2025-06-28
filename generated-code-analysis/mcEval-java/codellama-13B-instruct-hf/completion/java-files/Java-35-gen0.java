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

    // Map to hold the counts of each integer
    Map<Integer, Integer> count = new HashMap<>();

    // Loop through the input array
    for (int i : nums) {

      // Check if the number is already in the map
      if (count.containsKey(i)) {

        // If it is, increment its count
        count.put(i, count.get(i) + 1);
      } else {

        // If it's not, add it with a count of 1
        count.put(i, 1);
      }
    }

    // Loop through the map
    for (Integer key : count.keySet()) {

      // If the count is 1, return the key
      if (count.get(key) == 1) {
        return key;
      }
    }

    // Return -1 if none of the numbers were only present once
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