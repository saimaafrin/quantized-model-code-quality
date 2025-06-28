class Problem {

  /**
   * Determine if the given points form a boomerang on the X-Y plane.
   *
   * @param points An array of points where points[i] = [xi, yi].
   * @return True if the points form a boomerang, false otherwise.
   *
   * Example:
   * isBoomerang(new int[][]{{1,1},{2,3},{3,2}})
   * Output: true
   */
  public static boolean isBoomerang(int[][] points)  {
    int[] a = points[0], b = points[1], c = points[2];
    return (a[0] - b[0]) * (a[1] - c[1]) != (a[0] - c[0]) * (a[1] - b[1]);
  }
  public static void main(String[] args) {
    assert isBoomerang(new int[][] { { 0, 0 }, { 2, 2 }, { 1, 1 } }) ==
    false : "Test case 1 failed";
    assert isBoomerang(new int[][] { { 1, 1 }, { 2, 4 }, { 3, 1 } }) ==
    true : "Test case 2 failed";
    assert isBoomerang(new int[][] { { 0, 1 }, { 1, 0 }, { 0, -1 } }) ==
    true : "Test case 3 failed";

    System.out.println("All tests passed");
  }
}