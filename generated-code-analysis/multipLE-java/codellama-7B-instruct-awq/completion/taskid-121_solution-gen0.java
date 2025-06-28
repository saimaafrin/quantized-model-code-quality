import java.util.*;
import java.lang.reflect.*;
import org.javatuples.*;
import java.security.*;
import java.math.*;
import java.io.*;
import java.util.stream.*;
class Problem {
    // Given a non-empty array list of integers, return the sum of all of the odd elements that are in even positions.
    // Examples
    // >>> solution((new ArrayList<Long>(Arrays.asList((long)5l, (long)8l, (long)7l, (long)1l))))
    // (12l)
    // >>> solution((new ArrayList<Long>(Arrays.asList((long)3l, (long)3l, (long)3l, (long)3l, (long)3l))))
    // (9l)
    // >>> solution((new ArrayList<Long>(Arrays.asList((long)30l, (long)13l, (long)24l, (long)321l))))
    // (0l)
    public static long solution(ArrayList<Long> lst) {

        // your code here
        return 0;
    }
    public static void main(String[] args) {
    assert(solution((new ArrayList<Long>(Arrays.asList((long)5l, (long)8l, (long)7l, (long)1l)))) == (12l));
    assert(solution((new ArrayList<Long>(Arrays.asList((long)3l, (long)3l, (long)3l, (long)3l, (long)3l)))) == (9l));
    assert(solution((new ArrayList<Long>(Arrays.asList((long)30l, (long)13l, (long)24l, (long)321l)))) == (0l));
    assert(solution((new ArrayList<Long>(Arrays.asList((long)5l, (long)9l)))) == (5l));
    assert(solution((new ArrayList<Long>(Arrays.asList((long)2l, (long)4l, (long)8l)))) == (0l));
    assert(solution((new ArrayList<Long>(Arrays.asList((long)30l, (long)13l, (long)23l, (long)32l)))) == (23l));
    assert(solution((new ArrayList<Long>(Arrays.asList((long)3l, (long)13l, (long)2l, (long)9l)))) == (3l));
    }

}
