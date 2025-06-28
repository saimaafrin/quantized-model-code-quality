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
        return (int)Math.pow(2, N) - 1;
    }
    public static void main(String[] args) {
        // Test the function with different test cases
        assert maxRegions(3) == 13;
        assert maxRegions(4) == 21;
        assert maxRegions(5) == 31;
        System.out.println("All tests passed");
    }
}