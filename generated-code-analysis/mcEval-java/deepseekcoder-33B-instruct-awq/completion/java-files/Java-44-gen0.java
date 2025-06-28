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
    // TODO:
    ArrayList<Integer> result = new ArrayList<>();
    if (mat == null || mat.length == 0) {
      return new int[0];
    }

    int row = mat.length;
    int column = mat[0].length;
    int i = 0;
    int j = 0;
    boolean up = true;

    for (int index = 0; index < row * column;) {
      if (up) {
        for (; i >= 0 && j < column; i--, j++) {
          result.add(mat[i][j]);
          index++;
        }
        if (i < 0 && j <= column - 1) {
          i = 0;
        }
        if (j == column) {
          i += 2;
          j--;
        }
      } else {
        for (; j >= 0 && i < row; i++, j--) {
          result.add(mat[i][j]);
          index++;
        }
        if (j < 0 && i <= row - 1) {
          j = 0;
        }
        if (i == row) {
          j += 2;
          i--;
        }
      }
      up = !up;
    }

    return result.stream().mapToInt(Integer::intValue).toArray();
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