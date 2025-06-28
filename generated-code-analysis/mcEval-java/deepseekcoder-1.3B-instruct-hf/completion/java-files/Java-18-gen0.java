import java.util.*;

class Problem {
    /**
     * Given a string s. You should re-order the string using the following algorithm:
     * 1. Pick the smallest character from s and append it to the result.
     * 2. Pick the smallest character from s which is greater than the last appended character to the result and append it.
     * 3. Repeat step 2 until you cannot pick more characters.
     * 4. Pick the largest character from s and append it to the result.
     * 5. Pick the largest character from s which is smaller than the last appended character to the result and append it.
     * 6. Repeat step 5 until you cannot pick more characters.
     * 7. Repeat the steps from 1 to 6 until you pick all characters from s.
     * In each step, If the smallest or the largest character appears more than once you can choose any occurrence and append it to the result.
     * Return the result string after sorting s with this algorithm.
     */
    public String sortString(String s) {
        // Write your code here
        Map<Character, Integer> count = new HashMap<>();
        for(char c : s.toCharArray()){
            count.put(c, count.getOrDefault(c, 0) + 1);
        }
        
        StringBuilder result = new StringBuilder();
        while(!count.isEmpty()){
            char minChar = getMinChar(count, true);
            result.append(minChar);
            count.put(minChar, count.get(minChar) - 1);
            if(count.get(minChar) == 0){
                count.remove(minChar);
            }
            
            if(!count.isEmpty()){
                char maxChar = getMaxChar(count, false);
                result.append(maxChar);
                count.put(maxChar, count.get(maxChar) - 1);
                if(count.get(maxChar) == 0){
                    count.remove(maxChar);
                }
            }
        }
        return result.toString();
    }
    public static void main(String[] args) {
        Problem solution = new Problem();

        // Test the function with different test cases
        assert solution.sortString("aaaabbbbcccc").equals("abccbaabccba");
        assert solution.sortString("rat").equals("art");
        assert solution.sortString("leetcode").equals("cdelotee");
        System.out.println("All tests passed");
    }
}