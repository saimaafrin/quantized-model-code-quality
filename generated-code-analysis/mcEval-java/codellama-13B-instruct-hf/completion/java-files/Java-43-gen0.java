import java.util.*;
class Problem {

  /**
   * Given n non-negative integers representing the heights of bars in a bar chart.
   * Each bar has a width of 1 unit. Calculate the largest rectangle area that can be formed in the bar chart.
   *
   * @param heights An array of integers representing the heights of bars.
   * @return The maximum area of the rectangle that can be formed.
   *
   * Example:
   * largestRectangleArea(new int[]{2,1,5,6,2,3})
   * Output: 10
   *
   * Example:
   * largestRectangleArea(new int[]{2,4})
   * Output: 4
   */
  public static int largestRectangleArea(int[] heights)  {
    int n = heights.length;
    int[] left = new int[n];
    int[] right = new int[n];
    int[] maxArea = new int[n];

    // calculate left
    // from left to right
    int maxLeft = 0;
    for (int i = 0; i < n; i++) {
      if (heights[i] > maxLeft) {
        maxLeft = heights[i];
      }
      left[i] = maxLeft;
    }

    // calculate right
    // from right to left
    int maxRight = 0;
    for (int i = n - 1; i >= 0; i--) {
      if (heights[i] > maxRight) {
        maxRight = heights[i];
      }
      right[i] = maxRight;
    }

    // calculate max area
    for (int i = 0; i < n; i++) {
      maxArea[i] = Math.min(left[i], right[i]) * heights[i];
    }

    // find max area
    int max = maxArea[0];
    for (int i = 1; i < n; i++) {
      if (maxArea[i] > max) {
        max = maxArea[i];
      }
    }

    return max;
  }
  public static void main(String[] args) {
    assert largestRectangleArea(new int[] { 1, 2, 3, 4, 5, 3, 3, 2 }) == 15;
    assert largestRectangleArea(new int[] { 6, 2, 5, 4, 5, 1, 6 }) == 12;
    assert largestRectangleArea(new int[] { 2, 1, 2, 3, 1 }) == 5;

    System.out.println("All tests passed");
  }
}