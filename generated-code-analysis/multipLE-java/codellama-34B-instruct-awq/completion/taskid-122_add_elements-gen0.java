import java.util.*;
import java.lang.reflect.*;
import org.javatuples.*;
import java.security.*;
import java.math.*;
import java.io.*;
import java.util.stream.*;
class Problem {
    // Given a non-empty array array list of integers arr and an integer k, return
    // the sum of the elements with at most two digits from the first k elements of arr.
    // Example:
    // >>> addElements((new ArrayList<Long>(Arrays.asList((long)111l, (long)21l, (long)3l, (long)4000l, (long)5l, (long)6l, (long)7l, (long)8l, (long)9l))), (4l))
    // (24l)
    // Constraints:
    // 1. 1 <= len(arr) <= 100
    // 2. 1 <= k <= len(arr)
    public static long addElements(ArrayList<Long> arr, long k) {

        if (k == 1) {
            return arr.get((int)(k - 1));
        }
        // Find the first k elements with at most two digits
        ArrayList<Long> twoDigits = new ArrayList<>();
        long twoDigitsIndex = k - 1;
        if (arr.get((int)(k - 1)) > 99) {
            twoDigitsIndex = 0;
        } else {
            for (long i = 0; i < k; i++) {
                if (arr.get((int)(i)) > 99) {
                    twoDigitsIndex = i;
                    break;
                }
            }
        }
        if (twoDigitsIndex == 0) {
            return arr.get((int)(k - 1));
        }
        for (long i = 0; i <= twoDigitsIndex; i++) {
            twoDigits.add(arr.get((int)(i)));
        }
        // Sum the elements with at most two digits
        long sum = 0;
        for (long element : twoDigits) {
            sum += element;
        }
        return sum;
    }
    public static void main(String[] args) {
    assert(addElements((new ArrayList<Long>(Arrays.asList((long)1l, (long)-2l, (long)-3l, (long)41l, (long)57l, (long)76l, (long)87l, (long)88l, (long)99l))), (3l)) == (-4l));
    assert(addElements((new ArrayList<Long>(Arrays.asList((long)111l, (long)121l, (long)3l, (long)4000l, (long)5l, (long)6l))), (2l)) == (0l));
    assert(addElements((new ArrayList<Long>(Arrays.asList((long)11l, (long)21l, (long)3l, (long)90l, (long)5l, (long)6l, (long)7l, (long)8l, (long)9l))), (4l)) == (125l));
    assert(addElements((new ArrayList<Long>(Arrays.asList((long)111l, (long)21l, (long)3l, (long)4000l, (long)5l, (long)6l, (long)7l, (long)8l, (long)9l))), (4l)) == (24l));
    assert(addElements((new ArrayList<Long>(Arrays.asList((long)1l))), (1l)) == (1l));
    }

}
