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
        // sort strings by length
        strings.sort((s1, s2) -> s2.length() - s1.length());
        // create a set to hold all reversed strings
        Set<String> reversedStrings = new HashSet<>();
        for (String s: strings) {
            reversedStrings.add(new StringBuilder(s).reverse().toString());
        }
        // try to find substring for each string
        for (String s: strings) {
            for (int i = 0; i < s.length(); i++) {
                for (int j = i + 1; j <= s.length(); j++) {
                    if (reversedStrings.contains(s.substring(i, j)))
                        return j - i;
                }
            }
        }
        return 0;
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