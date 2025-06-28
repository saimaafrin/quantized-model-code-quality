import java.util.HashSet;
import java.util.Set;

class Problem {

  /**
   * Given a non-negative integer array A, if the sum of each pair of adjacent elements in the array is a perfect square, then the array is considered a square array.
   * Return the number of square permutations of A. Two permutations A1 and A2 are considered different if there exists an index i such that A1[i] != A2[i].
   *
   * @param A The input non-negative integer array.
   * @return The number of square permutations of A.
   *
   * Example:
   * squarePermutations(new int[]{1, 17, 8})
   * Output: 2
   *
   * Example:
   * squarePermutations(new int[]{2, 2, 2})
   * Output: 1
   */
  public static int squarePermutations(int[] A)  {
    // Convert the input array to a list
    List<Integer> nums = new ArrayList<>();
    for (int num : A) {
      nums.add(num);
    }

    // Create an array to store the counts of each number
    int[] counts = new int[1001];
    for (int num : A) {
      counts[num]++;
    }

    // Create a DP array to store the number of valid square permutations ending with each number
    int[] dp = new int[1001];
    for (int num : A) {
      dp[num]++;
    }

    // Iterate over all pairs of numbers in the array
    for (int i = 0; i < A.length; i++) {
      for (int j = 0; j < A.length; j++) {
        // If the sum of the two numbers is a perfect square, add the count of the second number to the count of the first number
        if (isPerfectSquare(A[i] + A[j])) {
          dp[A[i]] += dp[A[j]];
        }
      }
    }

    // Sum up the counts of all numbers
    int result = 0;
    for (int count : dp) {
      result += count;
    }

    // Return the sum
    return result;
  }
  public static void main(String[] args) {
    assert squarePermutations(new int[] { 1, 8, 27 }) == 0;
    assert squarePermutations(new int[] { 1, 8, 17 }) == 2;
    assert squarePermutations(new int[] { 4, 1, 3, 0, 2 }) == 0;
    System.out.println("All tests passed");
  }
}