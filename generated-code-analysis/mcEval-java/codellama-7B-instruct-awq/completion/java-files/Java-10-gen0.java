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
        // base case
        if (start[0] == end[0] && start[1] == end[1]) {
            return "can be travelled";
        }

        // map to mark the visited n-tersections
        boolean[][] visited = new boolean[n][n];
        for (int[] row : visited) {
            Arrays.fill(row, false);
        }

        // queue to keep track of the n-tersections to visit
        Queue<int[]> queue = new LinkedList<>();
        queue.add(start);
        visited[start[0]][start[1]] = true;

        while (!queue.isEmpty()) {
            int[] cur = queue.poll();

            // if the current n-tersection is the ending n-tersection, return "can be travelled"
            if (cur[0] == end[0] && cur[1] == end[1]) {
                return "can be travelled";
            }

            // mark the neighbors of the current n-tersection as visited
            for (int[] path : paths) {
                int x = cur[0] + path[0];
                int y = cur[1] + path[1];
                if (x >= 0 && x < n && y >= 0 && y < n && !visited[x][y]) {
                    queue.add(new int[] { x, y });
                    visited[x][y] = true;
                }
            }
        }

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