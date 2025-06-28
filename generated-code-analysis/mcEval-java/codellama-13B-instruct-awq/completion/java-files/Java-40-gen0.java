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
    int max = Integer.MIN_VALUE;
    int m = mat.length, n = mat[0].length;
    for (int i = 0; i < m; i++) {
      for (int j = 0; j < n; j++) {
        int count = 0;
        // horizonal
        for (int k = j; k < n; k++) {
          count = mat[i][k] == 1 ? count + 1 : 0;
          max = Math.max(count, max);
        }
        count = 0;
        // vertical
        for (int k = i; k < m; k++) {
          count = mat[k][j] == 1 ? count + 1 : 0;
          max = Math.max(count, max);
        }
        count = 0;
        // diagonal
        for (int k = i, l = j; k < m && l < n; k++, l++) {
          count = mat[k][l] == 1 ? count + 1 : 0;
          max = Math.max(count, max);
        }
        count = 0;
        // anti diagonal
        for (int k = i, l = j; k >= 0 && l >= 0; k--, l--) {
          count = mat[k][l] == 1 ? count + 1 : 0;
          max = Math.max(count, max);
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