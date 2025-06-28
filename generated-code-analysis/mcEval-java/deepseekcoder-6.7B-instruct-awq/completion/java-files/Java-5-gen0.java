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
        if(strings.size() == 0) return 0;

        int maxLen = 0;
        Set<String> set = new HashSet<>();
        for(String s : strings){
            for(int i = 0; i < s.length(); i++){
                for(int j = i + 1; j <= s.length(); j++){
                    set.add(s.substring(i, j));
                }
            }
        }
        for(String s : set){
            boolean found = false;
            for(String str : strings){
                if(str.contains(s) || str.contains(new StringBuilder(s).reverse().toString())){
                    found = true;
                    break;
                }
            }
            if(found && s.length() > maxLen){
                maxLen = s.length();
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