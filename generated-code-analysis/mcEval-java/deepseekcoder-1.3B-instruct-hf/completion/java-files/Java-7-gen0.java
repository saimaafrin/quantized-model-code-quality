import java.util.*;

class Problem {
    /**
     * Given the number of triangles N, determine the maximum number of regions the plane can be divided into.
     *
     * Example:
     * >>> maxRegions(1)
     * 2
     * >>> maxRegions(2)
     * 8
     *
     * @param N the number of triangles
     * @return the maximum number of regions
     */
    public static int maxRegions(int N)  {
        // Write your code here
        // To keep the complexity manageable, we can use dynamic programming
        // dp[i][j] represents the maximum number of regions we can divide the plane into with i triangles left and j edges connected
        // dp[i][j] = max(dp[i-1][j], dp[i-1][j-1] + 1) for i > 0 and j >= 0
        // dp[i][0] = sum(dp[i-1]) for i > 0
        // Initialize dp[0][j] = 1 for j >= 0
        // return dp[N][N-1] for N > 0

        int[][] dp = new int[N+1][N+1];
        for (int j = 0; j <= N; j++) {
            dp[0][j] = 1;
        }
        for (int i = 1; i <= N; i++) {
            dp[i][0] = i;
            for (int j = 1; j <= N; j++) {
                dp[i][j] = Math.max(dp[i-1][j], dp[i-1][j-1] + 1);
            }
        }
        return dp[N][N-1];
    }
    public static void main(String[] args) {
        // Test the function with different test cases
        assert maxRegions(3) == 13;
        assert maxRegions(4) == 21;
        assert maxRegions(5) == 31;
        System.out.println("All tests passed");
    }
}