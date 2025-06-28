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

    // Use stack to store the index of each bar
    Stack<Integer> stack = new Stack<>();
    int maxArea = 0;
    int i = 0;
    while (i < heights.length) {
      // If stack is empty or the current bar is higher than the bar of the top of the stack, push the index to stack
      if (stack.empty() || heights[i] >= heights[stack.peek()]) {
        stack.push(i);
        i++;
      } else {
        // If the current bar is lower than the bar of the top of the stack, calculate the area of the rectangle formed by the bar at the top of the stack
        int p = stack.pop();
        int h = heights[p];
        int w = stack.empty() ? i : i - stack.peek() - 1;
        maxArea = Math.max(maxArea, h * w);
      }
    }

    // If stack is not empty, calculate the area of the rectangle formed by the remaining bars
    while (!stack.empty()) {
      int p = stack.pop();
      int h = heights[p];
      int w = stack.empty() ? i : i - stack.peek() - 1;
      maxArea = Math.max(maxArea, h * w);
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