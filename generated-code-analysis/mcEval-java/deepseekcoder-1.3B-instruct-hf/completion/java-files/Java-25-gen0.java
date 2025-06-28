class Problem {
  /**
  * Given an integer n, return the minimum number of operations required to make all elements in the array arr equal.
  * The array arr has a length of n, and arr[i] = (2 * i) + 1 for 0 <= i < n.
  * In one operation, you can select two indices x and y (0 <= x, y < n) and subtract 1 from arr[x] and add 1 to arr[y] (i.e., arr[x] -= 1 and arr[y] += 1).
  * The goal is to make all elements in arr equal. The test cases will ensure that after performing some operations, all elements in arr can be made equal.
  *
  * Example 1:
  * Input: n = 3
  * Output: 2
  * Explanation: arr = [1, 3, 5]
  * First operation: x = 2, y = 0 -> arr = [2, 3, 4]
  * Second operation: x = 2, y = 0 -> arr = [3, 3, 3]
  *
  * Example 2:
  * Input: n = 6
  * Output: 9
  */
  public int minOperations(int n)  {
    int total = 0;
    for (int i = 0; i < n; i++) {
      int target = 2 * i + 1;
      int operations = 0;
      while (total < target) {
        total += 1;
        operations += 1;
      }
    }
    return total;
  }
  public static void main(String[] args) {
      Problem solution = new Problem();

      // Test the function with different test cases
      assert solution.minOperations(4) == 4;
      assert solution.minOperations(5) == 6;
      assert solution.minOperations(7) == 12;
      System.out.println("All tests passed");
  }
}