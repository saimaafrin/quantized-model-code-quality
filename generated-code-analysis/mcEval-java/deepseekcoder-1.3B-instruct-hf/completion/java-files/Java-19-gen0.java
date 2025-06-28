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
        int n = nums.length;
        double sum = 0;
        for(int num: nums) {
            sum += num;
        }

        boolean[] dp = new boolean[10001];
        dp[0] = true;
        for(int i = 1; i <= n; i++){
            for(int j = 10000; j >= nums[i - 1]; j--){
                dp[j] = dp[j] || dp[j - nums[i - 1]];
            }
        }

        for(int i = 0; i <= sum / n; i++){
            if(dp[i]){
                if(sum / n == 2 * i)
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