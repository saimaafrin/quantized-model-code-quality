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
        // Initialize an array to keep track of visited paths
        boolean[] visitedPaths = new boolean[paths.length];
        // Initialize a Queue to keep track of the n-tersections to visit
        Queue<Integer[]> queue = new LinkedList<>();
        // Add the starting n-tersection to the Queue
        queue.add(new Integer[]{start[0], start[1]});

        // Keep track of the number of n-tersections visited
        int numVisited = 1;

        // Loop while there are still n-tersections in the Queue
        while (!queue.isEmpty()) {
            // Dequeue the n-tersection from the Queue
            Integer[] current = queue.poll();
            // Add the n-tersection to the array of visited n-tersections
            visitedPaths[current[1]] = true;
            // Check if the n-tersection is the ending n-tersection
            if (current[0] == end[0] && current[1] == end[1]) {
                // If it is the ending n-tersection, return "can be travelled"
                return "can be travelled";
            }
            // Loop through the adjacent n-tersections of the dequeued n-tersection
            for (int i = 0; i < paths[current[1]].length; i++) {
                // Check if the adjacent n-tersection has not been visited
                if (!visitedPaths[paths[current[1]][i]]) {
                    // Add the adjacent n-tersection to the Queue
                    queue.add(new Integer[]{current[0], paths[current[1]][i]});
                    // Increment the number of n-tersections visited
                    numVisited++;
                    // If the number of n-tersections visited is greater than the size of the n-teresting space, return "cannot be travelled"
                    if (numVisited > n) {
                        return "cannot be travelled";
                    }
                }
            }
        }
        // If the Queue is empty and the ending n-tersection has not been visited, return "cannot be travelled"
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