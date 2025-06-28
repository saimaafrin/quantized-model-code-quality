import java.util.*;
import java.lang.reflect.*;
import org.javatuples.*;
import java.security.*;
import java.math.*;
import java.io.*;
import java.util.stream.*;
class Problem {
    // prime_fib returns n-th number that is a Fibonacci number and it's also prime.
    // >>> primeFib((1l))
    // (2l)
    // >>> primeFib((2l))
    // (3l)
    // >>> primeFib((3l))
    // (5l)
    // >>> primeFib((4l))
    // (13l)
    // >>> primeFib((5l))
    // (89l)
    public static long primeFib(long n) {

        long[] fib = new long[n];
        long[] isPrime = new long[n];
        long[] primeFib = new long[n];
        fib[0] = 1l;
        fib[1] = 2l;
        isPrime[0] = 1l;
        isPrime[1] = 1l;
        primeFib[0] = 1l;
        primeFib[1] = 2l;
        long i = 2l;
        while (i < n) {
            fib[i] = fib[i - 2l] + fib[i - 1l];
            isPrime[i] = fib[i] % 2l != 0l;
            primeFib[i] = fib[i];
            i += 1l;
        }
        return primeFib[n - 1l];
    }
    public static void main(String[] args) {
    assert(primeFib((1l)) == (2l));
    assert(primeFib((2l)) == (3l));
    assert(primeFib((3l)) == (5l));
    assert(primeFib((4l)) == (13l));
    assert(primeFib((5l)) == (89l));
    assert(primeFib((6l)) == (233l));
    assert(primeFib((7l)) == (1597l));
    assert(primeFib((8l)) == (28657l));
    assert(primeFib((9l)) == (514229l));
    assert(primeFib((10l)) == (433494437l));
    }

}
