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
        int sum = 0;
        for (int num : nums) {
            sum += num;
        }

        int average = sum / nums.length;
        int rest = sum % nums.length;

        int sum1 = 0;
        for (int i = 0; i < nums.length - rest; i++) {
            sum1 += nums[i];
            if (sum1 == average * rest) {
                return true;
            }
        }

        int sum2 = 0;
        for (int i = nums.length - rest; i < nums.length; i++) {
            sum2 += nums[i];
            if (sum2 == average * (rest + 1)) {
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