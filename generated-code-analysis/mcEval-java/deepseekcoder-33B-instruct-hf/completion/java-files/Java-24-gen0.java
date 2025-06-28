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
     int res = 0, right = 0;
     for (int i = 0; i < n; ++i) {
         if (s.charAt(i) == '(') {
             if (right % 2 > 0) {
                 right--;
                 res++;
             }
             right += 2;
         } else {
             right--;
             if (right < 0) {
                 right += 2;
                 res++;
             }
         }
     }
     return right + res;
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