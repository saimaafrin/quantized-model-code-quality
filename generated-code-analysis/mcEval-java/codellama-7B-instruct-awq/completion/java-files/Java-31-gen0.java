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
    int n = s.length();
    int maxUnique = 0;
    Map<Character, Integer> charFreq = new HashMap<>();

    for (int i = 0; i < n; i++) {
      charFreq.put(s.charAt(i), charFreq.getOrDefault(s.charAt(i), 0) + 1);
    }

    // calculate the maximum number of unique substrings
    // the substrings are reconstructed from the original string
    // each substring must be unique
    // therefore we can count the number of characters that can be used to form the substring
    // and the number of characters that can be used to form the substrings that contain a given character
    // if we are able to form a substring with a given character, then it means that we can form any substring that contains that character
    for (Map.Entry<Character, Integer> entry : charFreq.entrySet()) {
      Character c = entry.getKey();
      int cFreq = entry.getValue();
      int unique = 1;

      // find the maximum number of characters that can be used to form substrings that contain the given character
      for (int i = 1; i < cFreq; i++) {
        // we are able to form a substring with the given character
        // and it means that we can form any substring that contains the given character
        unique += i;
      }

      // the maximum number of unique substrings is the maximum number of unique substrings that can be formed
      // using the given character
      maxUnique = Math.max(maxUnique, unique);
    }

    return maxUnique;
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