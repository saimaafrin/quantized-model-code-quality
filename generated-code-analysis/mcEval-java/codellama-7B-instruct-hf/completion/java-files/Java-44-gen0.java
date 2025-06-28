import java.util.ArrayList;

class Problem {

  /**
   * Return all elements in the matrix in diagonal order.
   *
   * @param mat The input matrix.
   * @return An array containing all elements in diagonal order.
   *
   * Example:
   * diagonalOrder(new int[][]{{1,2,3},{4,5,6},{7,8,9}})
   * Output: [1,2,4,7,5,3,6,8,9]
   */
  public static int[] diagonalOrder(int[][] mat)  {
    int n = mat.length;
    int m = mat[0].length;
    int[] result = new int[n * m];
    int i = 0, j = 0;
    boolean row = true;
    int[][] matrix = new int[m][n];
    for (int k = 0; k < n * m; k++) {
      if (row) {
        result[k] = mat[i][j];
        j++;
        if (j == m) {
          i++;
          j = 0;
          row = false;
        }
      } else {
        result[k] = mat[j][i];
        i++;
        if (i == n) {
          j++;
          i = 0;
          row = true;
        }
      }
    }
    return result;
  }
  public static void main(String[] args) {
    assert java.util.Arrays.equals(
      diagonalOrder(new int[][] { { 1, 2 }, { 3, 4 } }),
      new int[] { 1, 2, 3, 4 }
    );
    assert java.util.Arrays.equals(
      diagonalOrder(
        new int[][] { { 1, 2, 3, 4 }, { 5, 6, 7, 8 }, { 9, 10, 11, 12 } }
      ),
      new int[] { 1, 2, 5, 9, 6, 3, 4, 7, 10, 11, 8, 12 }
    );
    assert java.util.Arrays.equals(
      diagonalOrder(new int[][] { { 1 }, { 2 }, { 3 } }),
      new int[] { 1, 2, 3 }
    );

    System.out.println("All tests passed");
  }
}