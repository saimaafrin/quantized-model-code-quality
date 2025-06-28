import java.util.*;
import java.lang.reflect.*;
import org.javatuples.*;
import java.security.*;
import java.math.*;
import java.io.*;
import java.util.stream.*;
class Problem {
    // Return the largest prime factor of n. Assume n > 1 and is not a prime.
    // >>> largestPrimeFactor((13195l))
    // (29l)
    // >>> largestPrimeFactor((2048l))
    // (2l)
    public static long largestPrimeFactor(long n) {

        // This is the largest prime factor of n. We will return it.
        // The largest prime factor of a composite number must be less than the square root of the number.
        long largestFactor = 0;
        // The smallest prime factor must be greater than 1, so we start with 2.
        long factor = 2;
        // The square root of n is the largest factor of n that we need to check.
        long maxFactor = (long) Math.floor(Math.sqrt((double) n));
        while (true) {
            if (n % factor == 0) {
                largestFactor = factor;
                // The current factor is a prime factor. Check if it's the largest so far.
                if (factor > largestFactor) {
                    largestFactor = factor;
                }
            }
            factor++;
            // If we've reached the maximum factor or we've found a factor that is greater than the square root of n, we're done.
            if (factor > maxFactor || largestFactor > maxFactor) {
                break;
            }
        }
        return largestFactor;
    }
    public static void main(String[] args) {
    assert(largestPrimeFactor((15l)) == (5l));
    assert(largestPrimeFactor((27l)) == (3l));
    assert(largestPrimeFactor((63l)) == (7l));
    assert(largestPrimeFactor((330l)) == (11l));
    assert(largestPrimeFactor((13195l)) == (29l));
    }

}
