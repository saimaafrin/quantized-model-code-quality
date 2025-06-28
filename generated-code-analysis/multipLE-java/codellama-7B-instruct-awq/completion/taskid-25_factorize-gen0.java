import java.util.*;
import java.lang.reflect.*;
import org.javatuples.*;
import java.security.*;
import java.math.*;
import java.io.*;
import java.util.stream.*;
class Problem {
    // Return array list of prime factors of given integer in the order from smallest to largest.
    // Each of the factors should be array listed number of times corresponding to how many times it appeares in factorization.
    // Input number should be equal to the product of all factors
    // >>> factorize((8l))
    // (new ArrayList<Long>(Arrays.asList((long)2l, (long)2l, (long)2l)))
    // >>> factorize((25l))
    // (new ArrayList<Long>(Arrays.asList((long)5l, (long)5l)))
    // >>> factorize((70l))
    // (new ArrayList<Long>(Arrays.asList((long)2l, (long)5l, (long)7l)))
    public static ArrayList<Long> factorize(long n) {

        ArrayList<Long> factors = new ArrayList<Long>();
        if (n == 0) {
            return factors;
        } else {
            factors.add(BigInteger.valueOf(n).isProbablePrime(10) ? 1L : 2L);
            long i = 2L;
            while (i <= Math.sqrt(n)) {
                while (n % i == 0) {
                    factors.add(i);
                    n /= i;
                }
                i += 1L;
            }
            if (n > 1) {
                factors.add(n);
            }
            return factors;
        }
    }
    public static void main(String[] args) {
    assert(factorize((2l)).equals((new ArrayList<Long>(Arrays.asList((long)2l)))));
    assert(factorize((4l)).equals((new ArrayList<Long>(Arrays.asList((long)2l, (long)2l)))));
    assert(factorize((8l)).equals((new ArrayList<Long>(Arrays.asList((long)2l, (long)2l, (long)2l)))));
    assert(factorize((57l)).equals((new ArrayList<Long>(Arrays.asList((long)3l, (long)19l)))));
    assert(factorize((3249l)).equals((new ArrayList<Long>(Arrays.asList((long)3l, (long)3l, (long)19l, (long)19l)))));
    assert(factorize((185193l)).equals((new ArrayList<Long>(Arrays.asList((long)3l, (long)3l, (long)3l, (long)19l, (long)19l, (long)19l)))));
    assert(factorize((20577l)).equals((new ArrayList<Long>(Arrays.asList((long)3l, (long)19l, (long)19l, (long)19l)))));
    assert(factorize((18l)).equals((new ArrayList<Long>(Arrays.asList((long)2l, (long)3l, (long)3l)))));
    }

}
