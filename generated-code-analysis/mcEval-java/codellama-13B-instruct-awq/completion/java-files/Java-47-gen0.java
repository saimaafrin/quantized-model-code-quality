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
    // Compute the cross product of the two vectors
    int cp1 = points[0][0] * points[1][1] + points[1][0] * points[0][1];
    int cp2 = points[1][0] * points[2][1] + points[2][0] * points[1][1];
    return cp1 * cp2 < 0;
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