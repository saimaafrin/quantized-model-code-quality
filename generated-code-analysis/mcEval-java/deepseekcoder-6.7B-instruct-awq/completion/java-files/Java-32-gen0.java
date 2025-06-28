class Problem {
    /**
     * Given a list of logs representing folder operations,
     * return the minimum number of steps required to return to the main folder.
     *
     * Example:
     * Input: logs = ["d1/","d2/","../","d21/","./"]
     * Output: 2
     * Explanation: Perform the "../" operation twice to return to the main folder.
     *
     * Input: logs = ["d1/","d2/","./","d3/","../","d31/"]
     * Output: 3
     *
     * Input: logs = ["d1/","../","../","../"]
     * Output: 0
     */
  public int minOperations(String[] logs)  {
        //use stack to track folder depth
        Stack<String> stack = new Stack<>();

        for (String log: logs) {
            if (log.equals("../")) {
                //go up one level
                if (!stack.isEmpty()) {
                    stack.pop();
                }
            }
            else if (!log.equals("./")) {
                //go down one level
                stack.push(log);
            }
        }

        return stack.size();
    }
  public static void main(String[] args) {
    Problem solution = new Problem();

    // Test the function with different test cases
    assert solution.minOperations(
      new String[] { "d1/", "d2/", "../", "d21/", "./", "../" }
    ) ==
    1;
    assert solution.minOperations(
      new String[] { "d1/", "d2/", "./", "d3/", "../", "d31/", "../" }
    ) ==
    2;
    assert solution.minOperations(
      new String[] { "d1/", "../", "../", "../", "d2/" }
    ) ==
    1;
    System.out.println("All tests passed");
  }
}