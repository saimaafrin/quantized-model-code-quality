import java.util.*;

class Problem {
    /**
     * Check if it is possible to split the given integer array into two non-empty arrays
     * with the same average.
     *
     * >>> splitArraySameAverage(new int[]{1,2,3,4,5,6,7,8})
     * true
     *
     * >>> splitArraySameAverage(new int[]{3,1})
     * false
     */
    public boolean splitArraySameAverage(int[] nums)  {
        int len = nums.length;
        int sum = 0;
        for (int num : nums) {
            sum += num;
        }
        // Make sure the average is an integer
        boolean isPossible = false;
        for (int i = 1; i <= len / 2; i++) {
            if ((sum * i) % len == 0) {
                isPossible = true;
                break;
            }
        }
        if (!isPossible) {
            return false;
        }
        // DP
        boolean[] dp = new boolean[sum + 1];
        dp[0] = true;
        int[] count = new int[sum + 1];
        count[0] = 1;
        for (int num : nums) {
            for (int i = sum; i >= num; i--) {
                dp[i] = dp[i] || dp[i - num] && count[i - num] < len;
                count[i] = count[i] + (dp[i - num] ? count[i - num] : 0);
            }
        }
        for (int i = 1; i <= len / 2; i++) {
            if ((sum * i) % len == 0 && dp[(sum * i) / len] && count[(sum * i) / len] > 0) {
                return true;
            }
        }
        return false;
    }
public static void main(String[] args) {
        Problem solution = new Problem();

        // Test the function with different test cases
        assert solution.splitArraySameAverage(new int[]{1, 2, 3, 4, 5, 6, 7, 8}) == true;
        assert solution.splitArraySameAverage(new int[]{1, 2, 3, 4, 5, 6, 7, 9}) == false;
        assert solution.splitArraySameAverage(new int[]{1, 2, 3, 4, 5, 6, 7, 10}) == true;
        assert solution.splitArraySameAverage(new int[]{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}) == true;
        System.out.println("All tests passed");
    }
}