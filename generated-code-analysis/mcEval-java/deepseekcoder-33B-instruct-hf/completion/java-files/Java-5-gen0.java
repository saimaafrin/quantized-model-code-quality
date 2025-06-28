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
        int largest = 0;
        for (String s : strings) {
            for (int i = 0; i < s.length(); ++i) {
                for (int j = i+2; j <= s.length(); ++j) {
                    String substring = s.substring(i, j);
                    for (String t : strings) {
                        if (t.contains(substring) || t.contains(new StringBuilder(substring).reverse().toString())) {
                            largest = Math.max(largest, substring.length());
                        }
                    }
                }
            }
        }
        return largest;
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