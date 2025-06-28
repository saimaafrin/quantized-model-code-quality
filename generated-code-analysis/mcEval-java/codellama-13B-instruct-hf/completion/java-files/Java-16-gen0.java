import java.lang.*;
import java.util.*;

class Problem {
    /**
     * Check if it is possible to divide the array into n/2 pairs such that the sum of each pair is divisible by k.
     *
     * @param arr the input integer array
     * @param k the divisor
     * @return true if it is possible, false otherwise
     *
     * Example:
     * Input: arr = [1,2,3,4,5,10,6,7,8,9], k = 5
     * Output: true
     * Explanation: The pairs are (1,9), (2,8), (3,7), (4,6), (5,10), and the sum of each pair is divisible by 5.
     *
     * Input: arr = [1,2,3,4,5,6], k = 7
     * Output: true
     * Explanation: The pairs are (1,6), (2,5), (3,4), and the sum of each pair is divisible by 7.
     *
     * Input: arr = [1,2,3,4,5,6], k = 10
     * Output: false
     * Explanation: It is not possible to divide the array into n/2 pairs such that the sum of each pair is divisible by 10.
     */
  public boolean canArrange(int[] arr, int k)  {
    // Write your solution here
    int arrSize = arr.length;
    if (k == 1) {
      return true;
    }
    if (arrSize == 1) {
      return false;
    }
    Arrays.sort(arr);
    if (arr[0] == 0) {
      if (k % 2 == 0) {
        return true;
      } else {
        return false;
      }
    }
    int max = -1, min = arr[arrSize - 1];
    for (int i = 0; i < arrSize; i++) {
      if (arr[i] > max) {
        max = arr[i];
      }
      if (arr[i] < min) {
        min = arr[i];
      }
    }
    int count = 0;
    for (int i = 0; i < arrSize; i++) {
      if (arr[i] == 0) {
        count++;
      }
    }
    if ((arrSize - count) % 2 == 1) {
      return false;
    }
    if (max - min < k) {
      return false;
    }
    boolean[] isUsed = new boolean[arrSize];
    for (int i = 0; i < arrSize; i++) {
      if (isUsed[i]) {
        continue;
      }
      int num = arr[i];
      int index = i;
      if (num % k == 0) {
        isUsed[index] = true;
        while (num % k == 0) {
          num /= k;
        }
        for (int j = 0; j < arrSize; j++) {
          if (arr[j] == num) {
            isUsed[j] = true;
            break;
          }
        }
      }
    }
    for (int i = 0; i < arrSize; i++) {
      if (!isUsed[i]) {
        return false;
      }
    }
    return true;
  }
  public static void main(String[] args) {
    Problem solution = new Problem();

    // Test the function with different test cases
    assert solution.canArrange(new int[]{1,2,3,4,5,10,6,7,8,9}, 5) == true;
    assert solution.canArrange(new int[]{1,2,3,4,5,6}, 7) == true;
    assert solution.canArrange(new int[]{1,2,3,4,5,6}, 10) == false;
    System.out.println("All tests passed");
  }
}