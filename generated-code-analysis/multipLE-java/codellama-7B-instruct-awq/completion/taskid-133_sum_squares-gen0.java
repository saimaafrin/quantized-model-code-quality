import java.util.*;
import java.lang.reflect.*;
import org.javatuples.*;
import java.security.*;
import java.math.*;
import java.io.*;
import java.util.stream.*;
class Problem {
    // You are given an array array list of numbers.
    // You need to return the sum of squared numbers in the given array list,
    // round each element in the array list to the upper int(Ceiling) first.
    // Examples:
    // >>> lst((new ArrayList<Float>(Arrays.asList((float)1.0f, (float)2.0f, (float)3.0f))))
    // (14l)
    // >>> lst((new ArrayList<Float>(Arrays.asList((float)1.0f, (float)4.0f, (float)9.0f))))
    // (98l)
    // >>> lst((new ArrayList<Float>(Arrays.asList((float)1.0f, (float)3.0f, (float)5.0f, (float)7.0f))))
    // (84l)
    // >>> lst((new ArrayList<Float>(Arrays.asList((float)1.4f, (float)4.2f, (float)0.0f))))
    // (29l)
    // >>> lst((new ArrayList<Float>(Arrays.asList((float)-2.4f, (float)1.0f, (float)1.0f))))
    // (6l)
    public static long sumSquares(ArrayList<Float> lst) {

        long ans = 0;
        for (int i = 0; i < lst.size(); i++) {
            ans += (long) (Math.ceil(lst.get(i))) * (Math.ceil(lst.get(i))) * 1l;
        }
        return ans;
    }
    public static void main(String[] args) {
    assert(sumSquares((new ArrayList<Float>(Arrays.asList((float)1.0f, (float)2.0f, (float)3.0f)))) == (14l));
    assert(sumSquares((new ArrayList<Float>(Arrays.asList((float)1.0f, (float)2.0f, (float)3.0f)))) == (14l));
    assert(sumSquares((new ArrayList<Float>(Arrays.asList((float)1.0f, (float)3.0f, (float)5.0f, (float)7.0f)))) == (84l));
    assert(sumSquares((new ArrayList<Float>(Arrays.asList((float)1.4f, (float)4.2f, (float)0.0f)))) == (29l));
    assert(sumSquares((new ArrayList<Float>(Arrays.asList((float)-2.4f, (float)1.0f, (float)1.0f)))) == (6l));
    assert(sumSquares((new ArrayList<Float>(Arrays.asList((float)100.0f, (float)1.0f, (float)15.0f, (float)2.0f)))) == (10230l));
    assert(sumSquares((new ArrayList<Float>(Arrays.asList((float)10000.0f, (float)10000.0f)))) == (200000000l));
    assert(sumSquares((new ArrayList<Float>(Arrays.asList((float)-1.4f, (float)4.6f, (float)6.3f)))) == (75l));
    assert(sumSquares((new ArrayList<Float>(Arrays.asList((float)-1.4f, (float)17.9f, (float)18.9f, (float)19.9f)))) == (1086l));
    assert(sumSquares((new ArrayList<Float>(Arrays.asList((float)0.0f)))) == (0l));
    assert(sumSquares((new ArrayList<Float>(Arrays.asList((float)-1.0f)))) == (1l));
    assert(sumSquares((new ArrayList<Float>(Arrays.asList((float)-1.0f, (float)1.0f, (float)0.0f)))) == (2l));
    }

}
