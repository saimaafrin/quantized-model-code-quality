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
        // Use a HashMap to represent the adjacency list for the graph
        HashMap<Integer, List<Integer>> graph = new HashMap<>();

        // Add the edges in the graph
        for (int[] path : paths) {
            int src = path[0];
            int dest = path[1];

            if (!graph.containsKey(src)) {
                graph.put(src, new ArrayList<>());
            }

            graph.get(src).add(dest);
        }

        // Use a boolean array to mark visited n-tersections
        boolean[] visited = new boolean[n + 1];

        // Start a DFS from the starting n-tersection
        if (dfs(graph, start[0], visited)) {
            // If the ending n-tersection is visited during DFS, return "can be travelled"
            return "can be travelled";
        } else {
            // If the ending n-tersection is not visited during DFS, return "cannot be travelled"
            return "cannot be travelled";
        }
    }
    public static void main(String[] args) {
        // Test the function with different test cases
        assert canTravelMaze(2, new int[]{0, 0}, new int[]{2, 2}, new int[][]{{0, 0, 0, 1}, {0, 1, 1, 1}, {1, 1, 1, 2}, {1, 2, 2, 2}}).equals("can be travelled");
        assert canTravelMaze(2, new int[]{0, 0}, new int[]{2, 2}, new int[][]{{0, 0, 0, 1}, {0, 1, 1, 1}, {1, 1, 2, 1}, {2, 1, 2, 2}}).equals("can be travelled");
        assert canTravelMaze(2, new int[]{0, 0}, new int[]{2, 2}, new int[][]{{0, 0, 0, 1}, {0, 1, 1, 1}, {1, 1, 2, 1}}).equals("cannot be travelled");
        System.out.println("All tests passed");
    }
}