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
    // We know we need to find three unique points, but we don't need to know
    // where they are in the array.
    int first = 0;
    int second = 1;
    int third = 2;

    // Use the slope between the first two points as a starting point.
    // (slope = (y2 - y1) / (x2 - x1))
    float slope = (float)(points[second][1] - points[first][1]) / (float)(points[second][0] - points[first][0]);

    // Compare the slope between the first two points and the second two points.
    // If they are equal, we know that the third point is in the same place as
    // the first or second point.
    // If they are not equal, we know that the third point is in a different
    // place.
    boolean isBoomerang = (slope == ((float)(points[third][1] - points[second][1]) / (float)(points[third][0] - points[second][0]))) ? false : true;

    // If we get to this point, we know that the slope between the first two
    // points and the second two points are not equal.
    // Compare the slope between the first two points and the third two points.
    // If they are equal, we know that the second point is in the same place as
    // the first or third point.
    // If they are not equal, we know that the second point is in a different
    // place.
    isBoomerang = (isBoomerang == (slope == ((float)(points[third][1] - points[first][1]) / (float)(points[third][0] - points[first][0])))) ? false : true;

    return isBoomerang;
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