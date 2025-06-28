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

        // If n is 0, return 0
        if (n == 0) return 0;
        // If n is 1, return 2 (1 and 10)
        if (n == 1) return 2;
        // If n is 2, return 3 (11, 101, 110)
        if (n == 2) return 3;
        // If n is greater than 2, return 2^(n-1)
        return (long)Math.pow(2, n - 1);
    }
    public static void main(String[] args) {
    assert(startsOneEnds((1l)) == (1l));
    assert(startsOneEnds((2l)) == (18l));
    assert(startsOneEnds((3l)) == (180l));
    assert(startsOneEnds((4l)) == (1800l));
    assert(startsOneEnds((5l)) == (18000l));
    }

}
