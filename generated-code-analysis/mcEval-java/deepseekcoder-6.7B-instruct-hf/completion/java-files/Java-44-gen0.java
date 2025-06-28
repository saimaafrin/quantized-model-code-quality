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
    if (mat == null || mat.length == 0) {
      return new int[0];
    }

    int m = mat.length;
    int n = mat[0].length;

    int[] result = new int[m * n];
    int k = 0;
    ArrayList<Integer> temp = new ArrayList<>();

    for (int i = 0; i < m + n - 1; i++) {
      if (i % 2 == 0) {
        // For even i, we start from top or bottom.
        int start_col = Math.max(0, i - m + 1);
        int count = Math.min(i + 1, n);
        for (int j = start_col; j < count; j++) {
          temp.add(mat[Math.min(i, m - 1)][j]);
        }
      } else {
        // For odd i, we start from left or right.
        int start_row = Math.max(0, i - n + 1);
        int count = Math.min(i + 1, m);
        for (int j = start_row; j < count; j++) {
          temp.add(mat[j][Math.min(i, n - 1)]);
        }
      }
    }

    for (int i = 0; i < temp.size(); i++) {
      result[i] = temp.get(i);
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