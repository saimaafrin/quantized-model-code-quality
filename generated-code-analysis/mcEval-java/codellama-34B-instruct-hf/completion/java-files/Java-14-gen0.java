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
        int lo = 0;
        int hi = nums.length - 1;
        while (lo <= hi) {
            int mid = (lo + hi) >>> 1;
            if (nums[mid] == target) {
                return mid;
            }
            if (nums[mid] >= nums[lo]) { // left half is sorted
                if (target >= nums[lo] && target < nums[mid]) {
                    hi = mid - 1;
                } else {
                    lo = mid + 1;
                }
            } else { // right half is sorted
                if (target > nums[mid] && target <= nums[hi]) {
                    lo = mid + 1;
                } else {
                    hi = mid - 1;
                }
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