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
    if (heights.length == 0) {
      return 0;
    }

    int maxArea = 0;
    Stack<Integer> stack = new Stack<>();

    // Add an extra zero to the left and right of the heights
    int[] extendedHeights = new int[heights.length + 2];
    for (int i = 0; i < heights.length; i++) {
      extendedHeights[i + 1] = heights[i];
    }

    for (int i = 0; i < extendedHeights.length; i++) {
      while (!stack.isEmpty() && extendedHeights[i] < extendedHeights[stack.peek()]) {
        int height = extendedHeights[stack.pop()];
        int width = i - stack.peek() - 1;
        maxArea = Math.max(maxArea, height * width);
      }

      stack.push(i);
    }

    return maxArea;
  }
  public static void main(String[] args) {
    assert largestRectangleArea(new int[] { 1, 2, 3, 4, 5, 3, 3, 2 }) == 15;
    assert largestRectangleArea(new int[] { 6, 2, 5, 4, 5, 1, 6 }) == 12;
    assert largestRectangleArea(new int[] { 2, 1, 2, 3, 1 }) == 5;

    System.out.println("All tests passed");
  }
}