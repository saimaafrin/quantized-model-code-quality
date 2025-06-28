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
        if (nums == null || nums.length == 0) return -1;
        if (nums.length == 1) return nums[0] == target ? 0 : -1;
        
        int left = 0, right = nums.length - 1;
        while (left <= right) {
            int mid = (left + right) >>> 1;
            int l = mid, r = mid + 1;
            if (nums[l] >= nums[left] && nums[r] >= nums[left]) {
                // mid is on the left side
                if (nums[mid] == target) return mid;
                if (nums[left] == nums[right]) {
                    // all the elements are the same
                    if (nums[left] == target) return left;
                    return -1;
                }
                left = mid + 1;
            } else if (nums[l] <= nums[right] && nums[r] <= nums[right]) {
                // mid is on the right side
                if (nums[mid] == target) return mid;
                right = mid - 1;
            } else {
                // mid is on the edge
                if (nums[mid] == target) return mid;
                if (nums[left] == target) return left;
                if (nums[right] == target) return right;
                return -1;
            }
        }
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