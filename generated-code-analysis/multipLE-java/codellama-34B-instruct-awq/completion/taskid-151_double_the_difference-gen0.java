import java.util.*;
import java.lang.reflect.*;
import org.javatuples.*;
import java.security.*;
import java.math.*;
import java.io.*;
import java.util.stream.*;
class Problem {
    // Given an array array list of numbers, return the sum of squares of the numbers
    // in the array list that are odd. Ignore numbers that are negative or not integers.
    // >>> doubleTheDifference((new ArrayList<Float>(Arrays.asList((long)1l, (long)3l, (long)2l, (long)0l))))
    // (10l)
    // >>> doubleTheDifference((new ArrayList<Float>(Arrays.asList((long)-1l, (long)-2l, (long)0l))))
    // (0l)
    // >>> doubleTheDifference((new ArrayList<Float>(Arrays.asList((long)9l, (long)-2l))))
    // (81l)
    // >>> doubleTheDifference((new ArrayList<Float>(Arrays.asList((long)0l))))
    // (0l)
    // If the input array list is empty, return 0.
    public static long doubleTheDifference(ArrayList<Float> lst) {

        // Convert array list to a stream
        var str = lst.stream();
        // Filter out negative values and non-integers
        var ints = str.filter(e -> e >= 0 && (e % 1) == 0);
        // Get sum of odd numbers
        long sum = ints.filter(e -> e % 2 != 0).map(e -> e * e).reduce(0l, (e1, e2) -> e1 + e2);
        // Return result
        return sum;
    }
    public static void main(String[] args) {
    assert(doubleTheDifference((new ArrayList<Float>(Arrays.asList()))) == (0l));
    assert(doubleTheDifference((new ArrayList<Float>(Arrays.asList((float)5.0f, (float)4.0f)))) == (25l));
    assert(doubleTheDifference((new ArrayList<Float>(Arrays.asList((float)0.1f, (float)0.2f, (float)0.3f)))) == (0l));
    assert(doubleTheDifference((new ArrayList<Float>(Arrays.asList((float)-10.0f, (float)-20.0f, (float)-30.0f)))) == (0l));
    assert(doubleTheDifference((new ArrayList<Float>(Arrays.asList((float)-1.0f, (float)-2.0f, (float)8.0f)))) == (0l));
    assert(doubleTheDifference((new ArrayList<Float>(Arrays.asList((float)0.2f, (float)3.0f, (float)5.0f)))) == (34l));
    assert(doubleTheDifference((new ArrayList<Float>(Arrays.asList((float)-9.0f, (float)-7.0f, (float)-5.0f, (float)-3.0f, (float)-1.0f, (float)1.0f, (float)3.0f, (float)5.0f, (float)7.0f, (float)9.0f)))) == (165l));
    }

}
