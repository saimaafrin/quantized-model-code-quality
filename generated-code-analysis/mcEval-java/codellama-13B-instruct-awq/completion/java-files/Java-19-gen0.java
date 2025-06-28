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
        // Calculate the sum of all elements in the array
        int sum = 0;
        for (int num : nums) {
            sum += num;
        }

        // Calculate the average of the array
        int average = sum / nums.length;

        // Calculate the sum of the first half of the array
        int firstHalfSum = 0;
        for (int i = 0; i < nums.length / 2; i++) {
            firstHalfSum += nums[i];
        }

        // Check if the sum of the first half of the array is equal to the sum of the second half
        if (firstHalfSum == sum - firstHalfSum) {
            return true;
        }

        // Check if the sum of the first half of the array is equal to the average of the array
        return firstHalfSum == average * (nums.length / 2);
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