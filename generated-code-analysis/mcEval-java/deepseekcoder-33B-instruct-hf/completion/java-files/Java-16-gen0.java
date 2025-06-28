import java.lang.*;
import java.util.*;

class Problem {
    /**
     * Check if it is possible to divide the array into n/2 pairs such that the sum of each pair is divisible by k.
     *
     * @param arr the input integer array
     * @param k the divisor
     * @return true if it is possible, false otherwise
     *
     * Example:
     * Input: arr = [1,2,3,4,5,10,6,7,8,9], k = 5
     * Output: true
     * Explanation: The pairs are (1,9), (2,8), (3,7), (4,6), (5,10), and the sum of each pair is divisible by 5.
     *
     * Input: arr = [1,2,3,4,5,6], k = 7
     * Output: true
     * Explanation: The pairs are (1,6), (2,5), (3,4), and the sum of each pair is divisible by 7.
     *
     * Input: arr = [1,2,3,4,5,6], k = 10
     * Output: false
     * Explanation: It is not possible to divide the array into n/2 pairs such that the sum of each pair is divisible by 10.
     */
  public boolean canArrange(int[] arr, int k)  {
        // Create a HashMap to store the frequency of each remainder
        Map<Integer, Integer> map = new HashMap<>();
        // Iterate through the array
        for (int num : arr) {
            // Calculate the remainder
            int remainder = ((num % k) + k) % k;
            // Increase the frequency of the remainder
            map.put(remainder, map.getOrDefault(remainder, 0) + 1);
        }
        // Check if it is possible to divide the array into n/2 pairs such that the sum of each pair is divisible by k
        for (int key : map.keySet()) {
            if (key == 0) {
                if (map.get(key) % 2 != 0) {
                    return false;
                }
            } else if (2 * key == k) {
                if (map.get(key) % 2 != 0) {
                    return false;
                }
            } else {
                if (!map.get(key).equals(map.get(k - key))) {
                    return false;
                }
            }
        }
        return true;
    }
  public static void main(String[] args) {
    Problem solution = new Problem();

    // Test the function with different test cases
    assert solution.canArrange(new int[]{1,2,3,4,5,10,6,7,8,9}, 5) == true;
    assert solution.canArrange(new int[]{1,2,3,4,5,6}, 7) == true;
    assert solution.canArrange(new int[]{1,2,3,4,5,6}, 10) == false;
    System.out.println("All tests passed");
  }
}