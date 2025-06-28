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
        int leapYears = 0;
        int currentYear = Y;
        while (leapYears < N) {
            currentYear++;
            if (isLeapYear(currentYear)) {
                leapYears++;
            }
        }
        return currentYear;
    }
    public static void main(String[] args) {
        // Test the function with the examples from the comment
        assert findNthLeapYear(2000, 4) == 2012;
        assert findNthLeapYear(1996, 10) == 2032;
        assert findNthLeapYear(2000, 1) == 2000;
        System.out.println("All tests passed");
    }
}