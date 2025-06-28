import java.util.HashMap;

class Problem {

  /**
   * Calculate the sum of unique elements in the given integer array.
   *
   * @param nums An array of integers.
   * @return The sum of unique elements.
   *
   * Example:
   * calculateUniqueSum(new int[]{1, 2, 3, 2})
   * Output: 4
   */
  public static int calculateUniqueSum(int[] nums)  {
    // Create a HashMap to store unique numbers and their sums
    HashMap<Integer, Integer> uniqueNumbers = new HashMap<>();
    int sum = 0;

    // Loop through each number in the array
    for (int num : nums) {
      // If the number is not in the HashMap, add it with its count 1 (since it is unique)
      // Otherwise, increment the count
      if (uniqueNumbers.containsKey(num)) {
        uniqueNumbers.put(num, uniqueNumbers.get(num) + 1);
      } else {
        uniqueNumbers.put(num, 1);
      }
    }

    // Loop through each entry in the HashMap and add the unique number (the key) times its count (the value) to sum
    for (HashMap.Entry<Integer, Integer> entry : uniqueNumbers.entrySet()) {
      sum += entry.getKey() * entry.getValue();
    }

    return sum;
  }
  public static void main(String[] args) {
    assert calculateUniqueSum(new int[] { 1, 4, 5, 1, 2, 4 }) == 7; // Test Case 1
    assert calculateUniqueSum(new int[] { 0, 0, 0, 0 }) == 0; // Test Case 2
    assert calculateUniqueSum(new int[] { -1, -2, -3, -2 }) == -4; // Test Case 3

    System.out.println("All tests passed");
  }
}