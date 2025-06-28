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
    if (mat.length == 0) {
      return 0;
    }

    int max = 0;
    int row = mat.length, col = mat[0].length;
    int[][][] dp = new int[row][col][8];

    // Initialize first row
    for (int i = 0; i < col; i++) {
      if (mat[0][i] == 1) {
        dp[0][i][0] = 1;
        max = Math.max(max, dp[0][i][0]);
      }
    }

    // Initialize first column
    for (int i = 0; i < row; i++) {
      if (mat[i][0] == 1) {
        dp[i][0][2] = 1;
        max = Math.max(max, dp[i][0][2]);
      }
    }

    for (int r = 1; r < row; r++) {
      for (int c = 0; c < col; c++) {
        if (mat[r][c] == 1) {
          dp[r][c][0] = dp[r - 1][c][0] + 1;
          dp[r][c][2] = dp[r - 1][c][2] + 1;
          dp[r][c][4] = dp[r - 1][c][4] + 1;
          dp[r][c][6] = dp[r - 1][c][6] + 1;

          // Update max
          max = Math.max(max, dp[r][c][0]);
          max = Math.max(max, dp[r][c][2]);
          max = Math.max(max, dp[r][c][4]);
          max = Math.max(max, dp[r][c][6]);

          // Diagonal
          if (c > 0) {
            dp[r][c][1] = dp[r - 1][c - 1][1] + 1;
            dp[r][c][3] = dp[r - 1][c - 1][3] + 1;
            dp[r][c][5] = dp[r - 1][c - 1][5] + 1;
            dp[r][c][7] = dp[r - 1][c - 1][7] + 1;

            // Update max
            max = Math.max(max, dp[r][c][1]);
            max = Math.max(max, dp[r][c][3]);
            max = Math.max(max, dp[r][c][5]);
            max = Math.max(max, dp[r][c][7]);
          }
        }
      }
    }

    return max;
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