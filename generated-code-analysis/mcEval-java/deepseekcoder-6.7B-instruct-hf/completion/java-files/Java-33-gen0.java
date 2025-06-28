import java.util.*;

class Problem {
    /**
     * Return the lexicographically smallest string of length n and value k.
     * The value of a string is the sum of the positions of its characters in the alphabet (starting from 1).
     * Example:
     * >>> getSmallestString(3, 27)
     * "aay"
     * >>> getSmallestString(5, 73)
     * "aaszz"
     */
    public String getSmallestString(int n, int k)  {
        // Initialize array to store the result
        char[] res = new char[n];
        // Initialize the array to fill 'a's
        Arrays.fill(res, 'a');
        // Subtract n from k
        k -= n;

        // Start from the rightmost position
        int j = n - 1;
        while (k > 0) {
            // Get the minimum of k and 25
            int tmp = Math.min(25, k);
            // Add tmp to the result array
            res[j] += tmp;
            // Subtract tmp from k
            k -= tmp;
            // Move to the left
            j--;
        }

        // Convert the array to string and return
        return new String(res);
    }

    public static void main(String[] args) {
        Problem solution = new Problem();

        // Test the function with different test cases
        assert solution.getSmallestString(3, 27).equals("aay");
        assert solution.getSmallestString(5, 73).equals("aaszz");
        assert solution.getSmallestString(3, 30).equals("acz");
        System.out.println("All tests passed");
    }
}