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
        Map<String, Integer> stringFrequencies = new HashMap<>();
        for (String string : strings) {
            for (int i = 0; i < string.length(); i++) {
                String substring = string.substring(i);
                if (stringFrequencies.containsKey(substring)) {
                    stringFrequencies.put(substring, stringFrequencies.get(substring) + 1);
                } else {
                    stringFrequencies.put(substring, 1);
                }
            }
        }
        
        int max = 0;
        for (String key : stringFrequencies.keySet()) {
            int value = stringFrequencies.get(key);
            if (value > max) {
                max = value;
            }
        }
        return max;
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