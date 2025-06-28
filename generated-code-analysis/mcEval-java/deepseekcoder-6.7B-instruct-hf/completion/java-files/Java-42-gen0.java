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
    int len = A.length;
    Set<Integer>[] count = new HashSet[len];
    int[][] dp = new int[len][len];
    for (int i = 0; i < len; i++) {
      count[i] = new HashSet<>();
      dp[i][i] = 1;
    }
    for (int i = 0; i < len - 1; i++) {
      if (isPerfectSquare(A[i] + A[i + 1])) {
        dp[i][i + 1] = 3;
        count[1].add(A[i]);
        count[1].add(A[i + 1]);
      } else {
        dp[i][i + 1] = 1;
      }
    }
    for (int l = 2; l < len; l++) {
      for (int i = 0; i + l < len; i++) {
        int j = i + l;
        for (int k = i; k < j; k++) {
          int total = dp[i][k] * dp[k + 1][j];
          if (isPerfectSquare(A[i] + A[j])) {
            total *= 2;
            if (k + 1 < len && isPerfectSquare(A[i] + A[k + 1])) {
              total *= 2;
            }
            if (k - 1 >= 0 && isPerfectSquare(A[k + 1] + A[j])) {
              total *= 2;
            }
          }
          dp[i][j] += total;
          dp[i][j] %= 1000000007;
        }
        for (int num : count[l - 1]) {
          if (isPerfectSquare(num + A[j])) {
            dp[i][j] = (dp[i][j] * 2) % 1000000007;
          }
        }
        count[l].addAll(count[l - 1]);
        if (j + 1 < len && isPerfectSquare(A[j] + A[j + 1])) {
          count[l].add(A[j]);
          count[l].add(A[j + 1]);
        }
      }
    }
    return dp[0][len - 1];
  }
  public static void main(String[] args) {
    assert squarePermutations(new int[] { 1, 8, 27 }) == 0;
    assert squarePermutations(new int[] { 1, 8, 17 }) == 2;
    assert squarePermutations(new int[] { 4, 1, 3, 0, 2 }) == 0;
    System.out.println("All tests passed");
  }
}