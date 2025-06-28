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
    int maxArea = 0;

    Stack<Integer> stack = new Stack<>();
    stack.push(0);
    for (int i = 0; i < heights.length; i++) {
      while (heights[i] < heights[stack.peek()]) {
        int top = stack.pop();
        int area = heights[top] * (i - stack.peek() - 1);
        maxArea = Math.max(area, maxArea);
      }

      stack.push(i);
    }

    while (!stack.empty()) {
      int top = stack.pop();
      int area = heights[top] * (heights.length - stack.peek() - 1);
      maxArea = Math.max(area, maxArea);
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