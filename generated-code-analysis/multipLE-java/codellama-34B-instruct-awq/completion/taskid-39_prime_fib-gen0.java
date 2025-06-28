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

        // a is the (n-1)th prime Fibonacci number,
        // b is the nth prime Fibonacci number,
        // c is the (n+1)th prime Fibonacci number
        long a = 1;
        long b = 2;
        long c = 3;

        // invariant:
        //   a is the (n-1)th prime Fibonacci number,
        //   b is the nth prime Fibonacci number,
        //   c is the (n+1)th prime Fibonacci number
        while (n > 1) {
            a = b;
            b = c;
            c = a + b;
            n -= 1;
        }
        return b;
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
