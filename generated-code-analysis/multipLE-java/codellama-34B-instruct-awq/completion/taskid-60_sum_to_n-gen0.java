import java.util.*;
import java.lang.reflect.*;
import org.javatuples.*;
import java.security.*;
import java.math.*;
import java.io.*;
import java.util.stream.*;
class Problem {
    // sum_to_n is a function that sums numbers from 1 to n.
    // >>> sumToN((30l))
    // (465l)
    // >>> sumToN((100l))
    // (5050l)
    // >>> sumToN((5l))
    // (15l)
    // >>> sumToN((10l))
    // (55l)
    // >>> sumToN((1l))
    // (1l)
    public static long sumToN(long n) {

        return n * (n + 1) / 2;
    }
    public static void main(String[] args) {
    assert(sumToN((1l)) == (1l));
    assert(sumToN((6l)) == (21l));
    assert(sumToN((11l)) == (66l));
    assert(sumToN((30l)) == (465l));
    assert(sumToN((100l)) == (5050l));
    }

}
