import java.util.*;
import java.lang.reflect.*;
import org.javatuples.*;
import java.security.*;
import java.math.*;
import java.io.*;
import java.util.stream.*;
class Problem {
    // Write a function that returns true if the object q will fly, and false otherwise.
    // The object q will fly if it's balanced (it is a palindromic array list) and the sum of its elements is less than or equal the maximum possible weight w.
    // Example:
    // >>> willItFly((new ArrayList<Long>(Arrays.asList((long)1l, (long)2l))), (5l))
    // (false)
    // # 1+2 is less than the maximum possible weight, but it's unbalanced.
    // >>> willItFly((new ArrayList<Long>(Arrays.asList((long)3l, (long)2l, (long)3l))), (1l))
    // (false)
    // # it's balanced, but 3+2+3 is more than the maximum possible weight.
    // >>> willItFly((new ArrayList<Long>(Arrays.asList((long)3l, (long)2l, (long)3l))), (9l))
    // (true)
    // # 3+2+3 is less than the maximum possible weight, and it's balanced.
    // >>> willItFly((new ArrayList<Long>(Arrays.asList((long)3l))), (5l))
    // (true)
    // # 3 is less than the maximum possible weight, and it's balanced.
    public static boolean willItFly(ArrayList<Long> q, long w) {

        boolean result = false;
        if (q != null) {
            long sum = 0;
            for (Long e: q) {
                sum += e;
            }
            result = (sum <= w && q.indexOf(q.get(0)) == q.lastIndexOf(q.get(0)));
        }
        return result;
    }
    public static void main(String[] args) {
    assert(willItFly((new ArrayList<Long>(Arrays.asList((long)3l, (long)2l, (long)3l))), (9l)) == (true));
    assert(willItFly((new ArrayList<Long>(Arrays.asList((long)1l, (long)2l))), (5l)) == (false));
    assert(willItFly((new ArrayList<Long>(Arrays.asList((long)3l))), (5l)) == (true));
    assert(willItFly((new ArrayList<Long>(Arrays.asList((long)3l, (long)2l, (long)3l))), (1l)) == (false));
    assert(willItFly((new ArrayList<Long>(Arrays.asList((long)1l, (long)2l, (long)3l))), (6l)) == (false));
    assert(willItFly((new ArrayList<Long>(Arrays.asList((long)5l))), (5l)) == (true));
    }

}
