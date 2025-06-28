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
        char[] a = s.toCharArray();
        int n = a.length;
        int[] count = new int[26];
        for (char c : a) count[c - 'a']++;
        int[] order = new int[n];
        for (int i = 0, j = 0; j < n; ) {
            order[j++] = i;
            if (count[i] > 0) count[i]--;
            i = (i + 1) % 26;
        }
        for (int i = 0; i < n - 1; i++) {
            int a = order[i], b = order[i + 1];
            if (a != b) order[i] = b;
            else {
                if (i + 1 >= n || order[i + 1] != order[i + 2])
                    order[i] = (a + 26) % 26;
                else order[i + 1] = (order[i + 1] + 26) % 26;
            }
        }
        StringBuilder res = new StringBuilder();
        for (int i = 0; i < order.length; ) {
            res.append(a[order[i]]);
            order[i] = (order[i] + 1) % 26;
            i++;
            int nxt = order[i];
            while (nxt == order[i - 1]) {
                nxt = (nxt + 1) % 26;
                order[i] = nxt;
                i++;
            }
        }
        return res.toString();
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