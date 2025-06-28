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
        int sum = Arrays.stream(nums).sum();
        int n = nums.length;

        boolean[][] dp = new boolean[n+1][sum*2+1];
        dp[0][0] = true;

        for (int i = 0; i < n; i++) {
            for (int j = sum; j >= nums[i]; j--) {
                for (int k = sum; k >= 0; k--) {
                    dp[i+1][j] |= dp[i][j-nums[i]] && (k == 0 || j >= nums[i] && dp[i+1][k-nums[i]]);
                }
            }
        }

        for (int i = 1; i < n; i++) {
            if (sum*i % n == 0 && dp[i][sum*i/n]) {
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