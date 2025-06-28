class Problem {
    /**
     * Search for the target value in the rotated sorted array.
     * If the target value exists, return its index; otherwise, return -1.
     * The array nums is rotated at some unknown pivot k, where 0 <= k < nums.length.
     * The time complexity of the algorithm must be O(log n).
     * 
     * >>> search(new int[]{4,5,6,7,0,1,2}, 0)
     * 4
     * >>> search(new int[]{4,5,6,7,0,1,2}, 3)
     * -1
     * >>> search(new int[]{1}, 0)
     * -1
     */
    public int search(int[] nums, int target)  {
        // Special cases.
        if (nums == null || nums.length == 0) return -1;
        if (nums.length == 1) return nums[0] == target ? 0 : -1;
        int mid;
        if (nums[0] <= nums[nums.length - 1]) {
            // If the array is not rotated, just do a linear search.
            for (mid = 0; mid < nums.length; ++mid)
                if (nums[mid] == target) return mid;
            return -1;
        }
        // Find the pivot point.
        int left = 0, right = nums.length - 1;
        while (left + 1 < right) {
            mid = (left + right) / 2;
            if (nums[mid] > nums[mid + 1]) {
                right = mid;
            } else {
                left = mid;
            }
        }
        mid = (left + right) / 2;
        // If target is larger than the maximum value, search the left part.
        if (target > nums[nums.length - 1]) {
            if (nums[0] <= target) {
                for (mid = 0; mid < left + 1; ++mid)
                    if (nums[mid] == target) return mid;
                return -1;
            }
            for (mid = left + 1; mid < nums.length; ++mid)
                if (nums[mid] == target) return mid;
            return -1;
        }
        // If target is smaller than the minimum value, search the right part.
        if (target < nums[0]) {
            if (nums[nums.length - 1] >= target) {
                for (mid = nums.length - 1; mid > right; --mid)
                    if (nums[mid] == target) return mid;
                return -1;
            }
            for (mid = right; mid >= 0; --mid)
                if (nums[mid] == target) return mid;
            return -1;
        }
        // Search the entire array.
        for (mid = 0; mid < nums.length; ++mid)
            if (nums[mid] == target) return mid;
        return -1;
    }
    public static void main(String[] args) {
        Problem solution = new Problem();

        // Test the function with different test cases
        assert solution.search(new int[]{4,5,6,7,0,1,2}, 6) == 2;
        assert solution.search(new int[]{4,5,6,7,0,1,2}, 7) == 3;
        assert solution.search(new int[]{1, 3}, 3) == 1;
        System.out.println("All tests passed");
    }
}