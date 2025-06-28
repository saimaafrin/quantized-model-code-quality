class Problem {
    /**
    * Given a string s composed of '(' and ')', the left and right brackets in s may be unbalanced. Each operation can insert a '(' or ')', and calculate the minimum number of insertion operations required. Make the left and right brackets in s balanced.
    *
    * Example 1:
    * Input: s = "(()))"
    * Output: 1
    * Explanation:  We need to add one '(' at the first of the string to make it balanced: "((()))".
    * Example 2:
    * Input: s = "((()))"
    * Output: 0
    *
    * - s consists of '(' and ')' only.
    */
 public int minInsertions(String s)  {
        if (s == null || s.length() == 0) return 0;

        // Maintain the right parentheses
        int rightBracket = 0;
        int res = 0;
        for (char c : s.toCharArray()) {
            if (c == '(') {
                if (rightBracket == 0) {
                    // Add one right parentheses
                    res++;
                }
                rightBracket++;
            } else {
                // Remove one right parentheses
                rightBracket--;
                // Add two parentheses
                res += 2;
            }
        }
        return res;
    }
    public static void main(String[] args) {
        Problem solution = new Problem();

        // Test the function with different test cases
        assert solution.minInsertions("((()))") == 0;
        assert solution.minInsertions("()()()") == 0;
        assert solution.minInsertions("(()))(()") == 2;
        assert solution.minInsertions("))())(((") == 6;
        System.out.println("All tests passed");
    }
}