class Problem {
    /**
     * Given a positive integer Y indicating the start year, and a positive integer N,
     * this function finds the Nth leap year after the start year Y.
     *
     * @param Y The start year.
     * @param N The position of the leap year to find.
     * @return The Nth leap year after the start year Y.
     *
     * Example:
     * findNthLeapYear(2000, 4) => 2008
     * findNthLeapYear(1996, 10) => 2032
     */
    public static int findNthLeapYear(int Y, int N)  {
        // If start year is not a leap year, we just need to find the Nth
        // leap year after the first leap year after the start year.
        if (Y % 4 != 0) {
            int numLeapYears = 0;
            int firstLeapYearAfterY = Y + 4 - (Y % 4);
            while (numLeapYears < N) {
                firstLeapYearAfterY += 4;
                numLeapYears++;
            }
            return firstLeapYearAfterY;
        } else {
            // If start year is a leap year, we can find the Nth leap year
            // directly by adding multiples of 4 to the start year.
            return Y + (N - 1) * 4;
        }
    }
    public static void main(String[] args) {
        // Test the function with the examples from the comment
        assert findNthLeapYear(2000, 4) == 2012;
        assert findNthLeapYear(1996, 10) == 2032;
        assert findNthLeapYear(2000, 1) == 2000;
        System.out.println("All tests passed");
    }
}