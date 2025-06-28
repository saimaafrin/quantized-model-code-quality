import java.util.*;
import java.lang.reflect.*;
import org.javatuples.*;
import java.security.*;
import java.math.*;
import java.io.*;
import java.util.stream.*;
class Problem {
    // Return n-th Fibonacci number.
    // >>> fib((10l))
    // (55l)
    // >>> fib((1l))
    // (1l)
    // >>> fib((8l))
    // (21l)
    public static long fib(long n) {

        if (n <= 1) {
            return n;
        }
        return fib(n-1) + fib(n-2);
    }
    public static void main(String[] args) {
    assert(fib((10l)) == (55l));
    assert(fib((1l)) == (1l));
    assert(fib((8l)) == (21l));
    assert(fib((11l)) == (89l));
    assert(fib((12l)) == (144l));
    }

}
