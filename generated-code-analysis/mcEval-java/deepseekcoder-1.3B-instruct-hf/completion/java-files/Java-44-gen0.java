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
    if (mat.length == 0) return new int[0];

    int m = mat.length, n = mat[0].length;
    int size = m * n;
    int[] result = new int[size];
    int idx = 0;

    ArrayList<Integer> top = new ArrayList<>(), bottom = new ArrayList<>();
    for (int i = 0; i < m; i++) {
      top.add(mat[i][i]);
      if (i != 0) bottom.add(mat[i][m - i - 1]);
    }

    ArrayList<Integer> temp = new ArrayList<>();
    while (top.size() > 0 || bottom.size() > 0) {
      if (top.size() > 0) {
        result[idx++] = top.remove(0);
      }
      if (bottom.size() > 0) {
        result[idx++] = bottom.remove(0);
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