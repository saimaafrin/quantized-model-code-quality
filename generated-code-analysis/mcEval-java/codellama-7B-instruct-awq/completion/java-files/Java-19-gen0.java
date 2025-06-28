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
        int min = Integer.MAX_VALUE;
        int max = Integer.MIN_VALUE;

        for (int num : nums) {
            sum += num;
            min = Math.min(min, num);
            max = Math.max(max, num);
        }

        if (min == max) {
            return false;
        }

        double avg = sum / nums.length;
        double diff = avg * 0.00001;

        // First array: [min, avg-diff)
        int firstSum = 0;
        for (int num : nums) {
            if (num == min) {
                continue;
            }
            if (num >= (int)(avg - diff)) {
                firstSum += num;
            } else {
                break;
            }
        }

        // Second array: (avg+diff, max]
        int secondSum = 0;
        for (int num : nums) {
            if (num == max) {
                continue;
            }
            if (num <= (int)(avg + diff)) {
                secondSum += num;
            } else {
                break;
            }
        }

        return firstSum == (int)avg && secondSum == (int)avg;
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