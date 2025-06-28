import java.util.*;
import java.lang.reflect.*;
import org.javatuples.*;
import java.security.*;
import java.math.*;
import java.io.*;
import java.util.stream.*;
class Problem {
    // Given a positive integer n, return the count of the numbers of n-digit
    // positive integers that start or end with 1.
    public static long startsOneEnds(long n) {

        if (n == 0) {
            return 0;
        }
        if (n == 1) {
            return 1;
        }
        long[][] dp = new long[2][(int)n+1];
        dp[0][0] = dp[1][0] = 0;
        dp[0][1] = dp[1][1] = 1;
        for (int j = 2; j <= n; j++) {
            dp[0][j] = dp[0][j-1] * 9 + dp[1][j-1] * 9;
            dp[1][j] = dp[0][j-1] * 9 + dp[1][j-1] * 9;
        }
        return dp[0][(int)n] + dp[1][(int)n];
    }
    public static void main(String[] args) {
    assert(startsOneEnds((1l)) == (1l));
    assert(startsOneEnds((2l)) == (18l));
    assert(startsOneEnds((3l)) == (180l));
    assert(startsOneEnds((4l)) == (1800l));
    assert(startsOneEnds((5l)) == (18000l));
    }

}
