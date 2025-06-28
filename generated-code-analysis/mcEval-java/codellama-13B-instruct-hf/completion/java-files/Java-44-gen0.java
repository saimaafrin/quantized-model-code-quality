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
    // Base case:
    if (mat.length == 0) {
      return new int[0];
    }

    // Variables:
    ArrayList<Integer> ans = new ArrayList<Integer>();
    int rowCount = mat.length;
    int colCount = mat[0].length;

    // Iterate through the matrix:
    for (int i = 0; i < rowCount; i++) {
      for (int j = 0; j < colCount; j++) {
        int idx = 0;

        // Add the value at the current position to the list:
        ans.add(idx++, mat[i][j]);

        // Get the next row to add to the list:
        if (i != 0) {
          idx = getNextRow(mat, i, j, idx, ans);
        }

        // Get the next column to add to the list:
        if (j != colCount - 1) {
          idx = getNextCol(mat, i, j, idx, ans);
        }
      }
    }

    // Return the list as an array:
    int[] ansArr = new int[ans.size()];
    for (int i = 0; i < ans.size(); i++) {
      ansArr[i] = ans.get(i);
    }
    return ansArr;
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