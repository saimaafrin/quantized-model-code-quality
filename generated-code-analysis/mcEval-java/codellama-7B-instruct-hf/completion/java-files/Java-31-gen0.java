import java.util.*;

class Problem {

  /**
   * Given a string s, split the string and return the maximum number of unique substrings.
   * The split substrings should be able to reconstruct the original string, and each substring must be unique.
   *
   * Example:
   * Input: s = "ababccc"
   * Output: 5
   * Explanation: One possible way to split the string is ['a', 'b', 'ab', 'c', 'cc'].
   *              Splitting the string as ['a', 'b', 'a', 'b', 'c', 'cc'] is not valid, because both 'a' and 'b' appear more than once.
   *
   * Note:
   * - The length of s is between 1 and 16.
   * - s only contains lowercase English letters.
   */
  public int maxUniqueSplit(String s)  {
    // Initialize dp table with 0 and set the maximum value to 0.
    int[] dp = new int[s.length()];
    int max = 0;

    // For each index i, calculate the maximum value based on the previous
    // values in the dp table and then update the maximum value.
    for (int i = 0; i < s.length(); i++) {
      dp[i] = 1;

      for (int j = 0; j < i; j++) {
        // The maximum value is the maximum of the current value
        // and the previous value + 1 if the current substring is unique.
        if (s.substring(j, i + 1).compareTo(s.substring(j, i + 1)) != 0) {
          dp[i] = Math.max(dp[i], dp[j] + 1);
        }
      }

      max = Math.max(max, dp[i]);
    }

    return max;
  }
  public static void main(String[] args) {
    Problem solution = new Problem();

    // Test the function with different test cases
    assert solution.maxUniqueSplit("ababccc") == 5;
    assert solution.maxUniqueSplit("abcabcabc") == 6;
    assert solution.maxUniqueSplit("abcdefg") == 7;
    assert solution.maxUniqueSplit("aaaaaaa") == 3;
    System.out.println("All tests passed");
  }
}