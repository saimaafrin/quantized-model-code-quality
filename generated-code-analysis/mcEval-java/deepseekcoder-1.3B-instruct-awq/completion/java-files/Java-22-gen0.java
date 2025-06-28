import java.util.*;

class Problem {
    /**
     * Given a binary string s and an integer k, return true if every binary string of length k is a substring of s, or false otherwise.
     *
     * Example 1:
     * Input: s = "00110110", k = 2
     * Output: true
     * Explanation: All binary strings of length 2 ("00", "01", "10", and "11") are substrings of s.
     *
     * Example 2:
     * Input: s = "0110", k = 1
     * Output: true
     * Explanation: All binary strings of length 1 ("0" and "1") are substrings of s.
     *
     * Example 3:
     * Input: s = "0110", k = 2
     * Output: false
     * Explanation: The binary string "00" is not a substring of s.
     */
  public boolean hasAllCodes(String s, int k)  {
    int numWays = (int) Math.pow(2, k);
    if (s.length() < k * numWays)
      return false;

    Set<String> set = new HashSet<>();
    for (int i = 0; i <= s.length() - k; i++) {
      set.add(s.substring(i, i + k));
    }

    return set.size() == numWays;
  }
  public static void main(String[] args) {
    Problem solution = new Problem();

    // Test the function with different test cases
    assert solution.hasAllCodes("00110110", 3) == false;
    assert solution.hasAllCodes("00110110", 2) == true;
    assert solution.hasAllCodes(
      "1111111111111111111111111111111111111111111111111111111111111111",
      1
    ) ==
    false;
    System.out.println("All tests passed");
  }
}