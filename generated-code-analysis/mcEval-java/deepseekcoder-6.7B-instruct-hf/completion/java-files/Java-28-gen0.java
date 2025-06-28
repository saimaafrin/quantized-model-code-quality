import java.util.*;

class Problem {
    /**
     * Given an integer k, return the minimum number of Fibonacci numbers whose sum is equal to k.
     * Fibonacci numbers are defined as follows:
     * F1 = 1
     * F2 = 1
     * Fn = Fn-1 + Fn-2, for n > 2.
     * It is guaranteed that there is at least one valid solution for the given k.
     *
     * Example 1:
     * Input: k = 7
     * Output: 2
     * Explanation: Fibonacci numbers are: 1, 1, 2, 3, 5, 8, 13, ...
     * For k = 7, we can get 2 + 5 = 7.
     *
     * Example 2:
     * Input: k = 10
     * Output: 2
     * Explanation: For k = 10, we can get 2 + 8 = 10.
     *
     * Example 3:
     * Input: k = 19
     * Output: 3
     * Explanation: For k = 19, we can get 1 + 5 + 13 = 19.
     */
  public int findMinFibonacciNumbers(int k)  {
    // List of fibonacci numbers
    List<Integer> fib = new ArrayList<>();
    fib.add(1);
    fib.add(1);
    
    // Generate fibonacci numbers until we have one bigger than k
    while (fib.get(fib.size() - 1) < k) {
      fib.add(fib.get(fib.size() - 1) + fib.get(fib.size() - 2));
    }
    
    // Start from the biggest fibonacci number and try to subtract it as long as possible
    int count = 0;
    int i = fib.size() - 1;
    while (k > 0) {
      if (fib.get(i) <= k) {
        k -= fib.get(i);
        count++;
      }
      i--;
    }
    return count;
  }
  public static void main(String[] args) {
    Problem solution = new Problem();

    // Test the function with different test cases
    assert solution.findMinFibonacciNumbers(7) == 2;
    assert solution.findMinFibonacciNumbers(10) == 2;
    assert solution.findMinFibonacciNumbers(13) == 1;
    System.out.println("All tests passed");
  }
}