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
        StringBuilder sb = new StringBuilder();
        k = 27 - k;
        while (n > 0) {
            if (n == 1) {
                if (k > 2) {
                    sb.append('a');
                    k -= 1;
                } else {
                    sb.append('z');
                    n -= 1;
               
                }
            } else {
                if (k % 2 == 1) {
                    sb.append('a');
                    k -= 1;
                } else {
                    sb.append('z');
                    k /= 2;
                }
                n -= 1;
            }
        }
        return sb.reverse().toString();
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