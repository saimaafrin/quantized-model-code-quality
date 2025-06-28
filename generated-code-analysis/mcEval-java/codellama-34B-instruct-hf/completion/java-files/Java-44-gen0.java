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

    int m = mat.length;
    if (m == 0) {
      return new int[0];
    }

    int n = mat[0].length;
    if (n == 0) {
      return new int[0];
    }

    int[] result = new int[m * n];
    ArrayList<Integer> resultList = new ArrayList<>();

    // for each diagonal
    for (int diagonal = 0; diagonal < m + n - 1; diagonal++) {

      // find the (x, y) coordinates of the first element in this diagonal
      int x = diagonal < n ? 0 : diagonal - n + 1;
      int y = diagonal < n ? diagonal : n - 1;

      // iterate through the elements of this diagonal
      while (x < m && y >= 0) {
        resultList.add(mat[x][y]);
        x++;
        y--;
      }
    }

    return resultList.stream().mapToInt(i -> i).toArray();
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