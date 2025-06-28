class Problem {
    /**
     * Given an integer array cost where cost[i] is the cost of ith step on a staircase,
     * return the minimum cost to reach the top of the floor.
     * You can either start from the step with index 0 or the step with index 1.
     *
     * Example:
     * >>> minCostClimbingStairs([10, 15, 20])
     * 15
     * Explanation: You will start at index 1.
     * - Pay 15 and climb two steps to reach the top.
     * The total cost is 15.
     *
     * >>> minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1])
     * 6
     * Explanation: You will start at index 0.
     * - Pay 1 and climb two steps to reach index 2.
     * - Pay 1 and climb two steps to reach index 4.
     * - Pay 1 and climb two steps to reach index 6.
     * - Pay 1 and climb one step to reach index 7.
     * - Pay 1 and climb two steps to reach index 9.
     * - Pay 1 and climb one step to reach the top.
     * The total cost is 6.
     */
  public int minCostClimbingStairs(int[] cost)  {
      int min = Integer.MAX_VALUE;
      for (int i = 0; i < cost.length; i++) {
        if (i + 1 == cost.length) {
          min = Math.min(min, cost[i]);
          break;
        }
        if (i + 2 == cost.length) {
          min = Math.min(min, cost[i] + cost[i + 1]);
          break;
        }
        min = Math.min(min, cost[i] + Math.min(minCostClimbingStairs(Arrays.copyOfRange(cost, i + 2, cost.length)), minCostClimbingStairs(Arrays.copyOfRange(cost, i + 1, cost.length))));
      }
      return min;
    }
  public static void main(String[] args) {
    Problem solution = new Problem();

    // Test the function with different test cases
    assert solution.minCostClimbingStairs(new int[] { 10, 15, 20 }) == 15;
    assert solution.minCostClimbingStairs(
      new int[] { 1, 100, 1, 1, 1, 100, 1, 1, 100, 1 }
    ) ==
    6;
    assert solution.minCostClimbingStairs(new int[] { 0, 0, 0, 1 }) == 0;
    System.out.println("All tests passed");
  }
}
