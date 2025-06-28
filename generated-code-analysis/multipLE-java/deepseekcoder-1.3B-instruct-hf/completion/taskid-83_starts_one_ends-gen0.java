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

        if (n <= 0) {
            return 0;
        } else if (n == 1) {
            return 2;
        } else {
            long res = 0;
            long start = 1;
            long end = 10;
            while (start % 10 != 1 && end % 10 != 1) {
                long middle = start + (end - start) / 2;
                res += middle / 10 * start + (middle % 10 == 1 ? middle % 10 : 0);
                start = middle / 10 + 1;
                end = middle * 10;
            }
            return res;
        }
    }
    public static void main(String[] args) {
    assert(startsOneEnds((1l)) == (1l));
    assert(startsOneEnds((2l)) == (18l));
    assert(startsOneEnds((3l)) == (180l));
    assert(startsOneEnds((4l)) == (1800l));
    assert(startsOneEnds((5l)) == (18000l));
    }

}
