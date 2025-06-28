class Problem {

  /**
   * Given a binary matrix mat of size m x n, return the length of the longest continuous line of 1s in the matrix.
   * The line could be horizontal, vertical, diagonal, or anti-diagonal.
   *
   * @param mat The binary matrix.
   * @return The length of the longest continuous line of 1s.
   *
   * Example:
   * longestLine(new int[][]{{0,1,1,0},{0,1,1,0},{0,0,0,1}})
   * Output: 3
   */
  public static int longestLine(int[][] mat)  {
    if (mat == null || mat.length == 0) return 0;
    int rows = mat.length;
    int cols = mat[0].length;
    int[][] dp = new int[rows][cols];

    // DP table initialization
    for (int i = 0; i < rows; i++) {
      dp[i][0] = mat[i][0];
    }
    for (int j = 0; j < cols; j++) {
      dp[0][j] = mat[0][j];
    }

    // Fill the DP table
    for (int i = 1; i < rows; i++) {
      for (int j = 1; j < cols; j++) {
        if (mat[i][j] == 1) {
          dp[i][j] = Math.min(Math.min(dp[i - 1][j], dp[i][j - 1]), dp[i - 1][j - 1]) + 1;
        }
      }
    }

    // Find the maximum value in the DP table
    int maxLen = 0;
    for (int i = 0; i < rows; i++) {
      for (int j = 0; j < cols; j++) {
        maxLen = Math.max(maxLen, dp[i][j]);
      }
    }

    return maxLen;
  }
  public static void main(String[] args) {
    assert longestLine(
      new int[][] {
        { 1, 1, 0, 0 },
        { 0, 1, 1, 0 },
        { 0, 0, 0, 1 },
        { 1, 0, 0, 0 },
      }
    ) ==
    3;
    assert longestLine(
      new int[][] {
        { 1, 0, 0, 1 },
        { 0, 1, 1, 0 },
        { 1, 1, 0, 0 },
        { 1, 0, 1, 1 },
      }
    ) ==
    4;
    assert longestLine(new int[][] { { 0, 0, 0 }, { 0, 1, 0 }, { 0, 0, 0 } }) ==
    1;

    System.out.println("All tests passed");
  }
}