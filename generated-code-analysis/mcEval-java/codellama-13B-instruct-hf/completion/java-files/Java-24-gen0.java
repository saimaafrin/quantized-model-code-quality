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
  int n = s.length();
  int[] dp = new int[n + 1];
  for (int i = n - 1; i >= 0; i--) {
   if (s.charAt(i) == ')') {
    if (i < n - 1 && s.charAt(i + 1) == ')') {
     dp[i] = dp[i + 2] + 1;
    } else {
     dp[i] = 0;
    }
   } else {
    dp[i] = dp[i + 1];
   }
  }
  return dp[0];
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