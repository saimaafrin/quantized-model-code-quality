import java.util.*;

class Problem {
    /**
     * Given a number of case-sensitive strings, finds the largest string X, such that either X, or its inverse can be found as a substring of any of the given strings.
     * 
     * Example:
     * >>> findLargestSubstring(Arrays.asList("ABCD", "BCDFF", "BRCD"))
     * 2
     * >>> findLargestSubstring(Arrays.asList("rose", "orchid"))
     * 2
     */
    public int findLargestSubstring(List<String> strings)  {
        int longest = 0;

        for (String s : strings) {
            // Find the longest common prefix and suffix, then add them together
            int prefixLength = longestCommonPrefix(s, s);
            int suffixLength = longestCommonSuffix(s, s);
            longest = Math.max(longest, prefixLength + suffixLength);
        }

        // Find the longest substring that can be found in at least one string
        for (String s1 : strings) {
            for (String s2 : strings) {
                if (s1 == s2) {
                    continue;
                }

                // Find the longest common substring between s1 and s2
                int lcsLength = longestCommonSubstring(s1, s2);
                longest = Math.max(longest, lcsLength);
            }
        }

        return longest;
    }
    public static void main(String[] args) {
        Problem solution = new Problem();

        // Test the function with different test cases
        assert solution.findLargestSubstring(Arrays.asList("ABCD", "BCDFF", "BRCD")) == 2;
        assert solution.findLargestSubstring(Arrays.asList("rose", "orchid")) == 2;
        assert solution.findLargestSubstring(Arrays.asList("hello", "world")) == 1;
        System.out.println("All tests passed");
    }
}