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
        char[] result = new char[n];
        for (int i = 0; i < n; i++) {
            result[i] = 'a';
        }
        k -= n;
        int i = n - 1;
        while (k > 0) {
            int temp = Math.min(25, k);
            result[i] = (char) (result[i] + temp);
            k -= temp;
            i--;
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