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
        // Add your code here
        int[] dp = new int[N+1];
        dp[0]=0;
        dp[1]=2;
        for(int i=2; i<=N; i++) {
            dp[i]=2*dp[i-1]+1;
        }
        return dp[N];
    }
    public static void main(String[] args) {
        // Test the function with different test cases
        assert maxRegions(3) == 13;
        assert maxRegions(4) == 21;
        assert maxRegions(5) == 31;
        System.out.println("All tests passed");
    }
}