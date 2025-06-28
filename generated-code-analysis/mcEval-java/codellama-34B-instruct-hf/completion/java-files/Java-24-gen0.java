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
        /*
        * 1. calculate number of left brackets and right brackets
        * 2. use two pointers to keep track of index of ( and )
        * 3. If left pointer > right pointer, add a right bracket
        * 4. If right pointer > left pointer, add a left bracket
        * 5. If left pointer == right pointer, add a left or right bracket
        * 6. Continue to loop until end of string
        */

        int len = s.length();
        if (len == 0) return 0;
        int leftCount = 0;
        int rightCount = 0;
        for (char c : s.toCharArray()) {
            if (c == '(') leftCount++;
            else rightCount++;
        }

        int left = 0;
        int right = 0;
        int count = 0;
        while (left < len || right < len) {
            if (left == len) {
                count += rightCount - right;
                right++;
                continue;
            }

            if (right == len) {
                count += leftCount - left;
                left++;
                continue;
            }

            if (s.charAt(left) == '(') {
                left++;
                if (s.charAt(right) == ')') right++;
                else count++;
                continue;
            }

            if (s.charAt(right) == '(') {
                right++;
                count++;
                continue;
            }

            right++;
            count++;
        }
        return count;
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