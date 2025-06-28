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
        // Create an array to store the result
        char[] res = new char[n];
        // Initialize the array with 'a'
        Arrays.fill(res, 'a');
        // Subtract the value of 'a' from k
        k -= n;

        // While k > 0
        int i = n - 1;
        while(k > 0) {
            // Get the min value between k and 25
            int val = Math.min(25, k);
            // Update the res[i] with the char corresponding to val + 1
            res[i] = (char)('a' + val);
            // Subtract the value from k
            k -= val;
            // Decrement i
            i--;
        }
        // Return the string
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