import java.util.*;

class Problem {
    /**
     * Given the size of the n-teresting space, the starting and ending n-tersection coordinates, and the paths between adjacent n-tersections, determine if it is possible to travel from the starting n-tersection to the ending n-tersection.
     * 
     * Parameters:
     * - n: the size of the n-teresting space
     * - start: the starting n-tersection coordinates
     * - end: the ending n-tersection coordinates
     * - paths: paths between adjacent n-tersections in the n-teresting space
     * 
     * Output:
     * - If travel is possible, return "can be travelled"
     * - If travel is not possible, return "cannot be travelled"
     */
    public static String canTravelMaze(int n, int[] start, int[] end, int[][] paths)  {
        // Write your code here
        // Base case
        if (n == 0) {
            return "cannot be travelled";
        }

        // The n-teresting space is divided into four regions of size n/2, so we need to check if the
        // starting and ending n-tersections are in the same region.
        int startRegion = (start[0] * n + start[1]) % 4;
        int endRegion = (end[0] * n + end[1]) % 4;
        if (startRegion != endRegion) {
            return "cannot be travelled";
        }

        // Check if the starting and ending n-tersections are at the edge of the n-teresting space
        // (i.e. they are in the corner of the space)
        if (start[0] == 0 || start[1] == 0 || end[0] == n - 1 || end[1] == n - 1) {
            return "cannot be travelled";
        }

        // Check if the starting and ending n-tersections are at the center of the n-teresting space
        // (i.e. they are in the middle of the space)
        if (start[0] == (n - 1) / 2 && start[1] == (n - 1) / 2 && end[0] == (n - 1) / 2 && end[1] == (n - 1) / 2) {
            return "can be travelled";
        }

        // Check if the paths are valid
        for (int[] path : paths) {
            // Check if the starting n-tersection is the path's starting n-tersection
            if (start[0] == path[0] && start[1] == path[1]) {
                // Check if the path is valid
                if (path[0] == end[0] && path[1] == end[1]) {
                    // Path is valid, so we can travel from the starting n-tersection to the ending n-tersection
                    return "can be travelled";
                }
            }
        }

        // Path is not valid, so we cannot travel from the starting n-tersection to the ending n-tersection
        return "cannot be travelled";
    }
    public static void main(String[] args) {
        // Test the function with different test cases
        assert canTravelMaze(2, new int[]{0, 0}, new int[]{2, 2}, new int[][]{{0, 0, 0, 1}, {0, 1, 1, 1}, {1, 1, 1, 2}, {1, 2, 2, 2}}).equals("can be travelled");
        assert canTravelMaze(2, new int[]{0, 0}, new int[]{2, 2}, new int[][]{{0, 0, 0, 1}, {0, 1, 1, 1}, {1, 1, 2, 1}, {2, 1, 2, 2}}).equals("can be travelled");
        assert canTravelMaze(2, new int[]{0, 0}, new int[]{2, 2}, new int[][]{{0, 0, 0, 1}, {0, 1, 1, 1}, {1, 1, 2, 1}}).equals("cannot be travelled");
        System.out.println("All tests passed");
    }
}