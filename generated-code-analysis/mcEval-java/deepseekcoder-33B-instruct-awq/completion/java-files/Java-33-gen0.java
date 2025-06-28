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
        // Initialize the result string with 'a's.
        char[] result = new char[n];
        Arrays.fill(result, 'a');
        k -= n;  // We subtract the value of the 'a's from k.
        while (k > 0) {
            // The value of the current character is the minimum of k and 25 (the value of 'z').
            int min = Math.min(k, 25);
            result[--n] += min;
            k -= min;
        }
        return new String(result);
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