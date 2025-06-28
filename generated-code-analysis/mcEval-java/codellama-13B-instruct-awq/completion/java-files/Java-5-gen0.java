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
        int length = strings.get(0).length();
        for (String s : strings) {
            length = Math.max(length, s.length());
        }
        String candidate = "";
        int current = 0;
        for (int i = 0; i < length; i++) {
            candidate = "";
            for (String s : strings) {
                String sub = s.substring(i, i+1);
                if (!sub.equals(candidate)) {
                    candidate = "";
                    break;
                }
                candidate += sub;
            }
            if (!candidate.isEmpty()) {
                if (candidate.length() > current) {
                    current = candidate.length();
                }
            }
        }
        return current;
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