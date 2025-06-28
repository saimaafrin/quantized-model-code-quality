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
      // Initialize an array to count the frequency of remainders when each number is divided by k
      int[] freq = new int[k];
      // Iterate through the array
      for (int num : arr) {
          // Update the frequency count based on the remainder
          freq[(num % k + k) % k]++;
      }
      // If there is a number with a frequency greater than k/2, it's impossible to form pairs
      if (freq[0] % 2 != 0) {
          return false;
      }
      // Iterate through the remaining numbers (from 1 to k/2)
      for (int i = 1; i <= k / 2; i++) {
          // If the frequency of a number is not equal to the frequency of k-i, it's impossible to form pairs
          if (freq[i] != freq[k - i]) {
              return false;
          }
      }
      // If all checks pass, it's possible to form the desired pairs
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