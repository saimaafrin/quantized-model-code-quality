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
        int maxLen = 0;
        for (String string : strings) {
            for (int i = 0; i < string.length(); i++) {
                for (int j = i + 1; j <= string.length(); j++) {
                    String substring = string.substring(i, j);
                    int count = 0;
                    for (String s : strings) {
                        if (s.contains(substring) || s.contains(new StringBuilder(substring).reverse().toString())) {
                            count++;
                        }
                    }
                    if (count == strings.size() && substring.length() > maxLen) {
                        maxLen = substring.length();
                    }
                }
            }
        }
        return maxLen;
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