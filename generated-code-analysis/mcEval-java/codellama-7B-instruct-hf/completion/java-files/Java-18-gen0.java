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
        char[] cs = s.toCharArray();
        int n = cs.length;
        int[] count = new int[26];
        for (char c : cs) {
            count[c - 'a']++;
        }
        int last = -1;
        boolean ascend = true;
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < n; i++) {
            int c = cs[i] - 'a';
            if (count[c]-- > 0) {
                if (c < last || ascend && c == last) {
                    ascend = false;
                    int c1 = -1;
                    for (int j = 25; j >= 0; j--) {
                        if (count[j] > 0 && (c1 < 0 || j < c1)) {
                            c1 = j;
                        }
                    }
                    sb.append((char) (c1 + 'a'));
                    last = c1;
                } else {
                    sb.append((char) (c + 'a'));
                    last = c;
                }
            }
        }
        return sb.toString();
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