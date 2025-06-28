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
        int longestMatchLength = 0;
        int lengthOfStrings = strings.size();
        for (int i = 0; i < lengthOfStrings - 1; i++) {
            String string = strings.get(i);
            for (int j = i + 1; j < lengthOfStrings; j++) {
                String otherString = strings.get(j);
                int matchLength = 0;
                for (int k = 0; k < string.length() && k < otherString.length(); k++) {
                    if (string.charAt(k) == otherString.charAt(k)) {
                        matchLength++;
                    } else {
                        break;
                    }
                }
                longestMatchLength = Math.max(longestMatchLength, matchLength);
            }
        }
        return longestMatchLength;
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