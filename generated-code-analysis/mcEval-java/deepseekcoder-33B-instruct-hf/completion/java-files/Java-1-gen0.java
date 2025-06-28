import java.util.Arrays;
import java.util.List;

class Problem {
     /**
         * Calculate the average account balance based on the closing balances from the past twelve months.
         *
         * @param closingBalances A list of closing balances from the past twelve months.
         * @return The average account balance.
         *
         * Example:
         * calculateAverageBalance(Arrays.asList(100.0, 489.12, 12454.12, 1234.10, 823.05, 109.20, 5.27, 1542.25, 839.18, 83.99, 1295.01, 1.75))
         * Output: 1581.42
         */
    public static double calculateAverageBalance(List<Double> closingBalances) {
        // Add your code here
        Double average=0.0;
        for(Double balance: closingBalances)
        {
            average+=balance;
        }
        return average/closingBalances.size();
    }
    public static void main(String[] args) {
        // Test the function with the examples from the comment
        assert Math.abs(calculateAverageBalance(Arrays.asList(100.0, 489.12, 12454.12, 1234.10, 823.05, 109.20, 5.27, 1542.25, 839.18, 83.99, 1295.01, 1.75)) - 1581.42) < 0.01;
        assert Math.abs(calculateAverageBalance(Arrays.asList(100.0, 200.0, 300.0, 400.0, 500.0, 600.0, 700.0, 800.0, 900.0, 1000.0, 1100.0, 1200.0)) - 650.0) < 0.01;
        assert Math.abs(calculateAverageBalance(Arrays.asList(1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0)) - 6.5) < 0.01;
        System.out.println("All tests passed");
    }
}