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
    if (mat.length == 0 || mat[0].length == 0) {
      return new int[]{};
    }

    int m = mat.length;
    int n = mat[0].length;

    int[] result = new int[m * n];
    int idx = 0;
    ArrayList<Integer> intermediate = new ArrayList<>();

    for (int i = 0; i < m + n - 1; i++) {
      intermediate.clear();

      int row = i < n ? 0 : i - n + 1;
      int col = i < n ? i : n - 1;

      while (row < m && col > -1) {
        intermediate.add(mat[row][col]);
        row++;
        col--;
      }

      if (i % 2 == 0) {
        for (int j = intermediate.size() - 1; j >= 0; j--) {
          result[idx++] = intermediate.get(j);
        }
      } else {
        for (Integer j : intermediate) {
          result[idx++] = j;
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