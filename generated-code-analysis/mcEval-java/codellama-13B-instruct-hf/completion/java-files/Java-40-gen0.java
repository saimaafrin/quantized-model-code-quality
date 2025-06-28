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
    int rows = mat.length, cols = mat[0].length;
    int[][] dirs = new int[][]{{0,1},{1,0},{1,1},{1,-1}};
    int max = 0;
    for(int i=0; i<rows; i++)
      for(int j=0; j<cols; j++)
        for(int[] dir : dirs) {
          int cnt = 0;
          int x = i, y = j;
          while(x >= 0 && x < rows && y >= 0 && y < cols && mat[x][y] == 1) {
            cnt++;
            x += dir[0];
            y += dir[1];
          }
          if(cnt > max)
            max = cnt;
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