import java.util.*;
import java.lang.reflect.*;
import org.javatuples.*;
import java.security.*;
import java.math.*;
import java.io.*;
import java.util.stream.*;
class Problem {
    // Create a function which returns the largest index of an element which
    // is not greater than or equal to the element immediately preceding it. If
    // no such element exists then return -1. The given array array list will not contain
    // duplicate values.
    // Examples:
    // >>> canArrange((new ArrayList<Long>(Arrays.asList((long)1l, (long)2l, (long)4l, (long)3l, (long)5l))))
    // (3l)
    // >>> canArrange((new ArrayList<Long>(Arrays.asList((long)1l, (long)2l, (long)3l))))
    // (-1l)
    public static long canArrange(ArrayList<Long> arr) {

        long n = arr.size();
        long sum = arr.stream().reduce(0l, (a, b) -> a + b);
        if (sum % 2l != 0) {
            return -1l;
        }
        sum /= 2l;
        ArrayList<Long> left = new ArrayList<Long>();
        ArrayList<Long> right = new ArrayList<Long>();
        for (long i = 0l; i < n; i++) {
            if (arr.get(i) <= sum) {
                left.add(arr.get(i));
            }
            else {
                right.add(arr.get(i));
            }
        }
        ArrayList<Long> res = new ArrayList<Long>();
        for (long i = 0l; i < n; i++) {
            if (left.size() > 0l && right.size() > 0l) {
                res.add(Math.max(left.get(0), right.get(0)));
                left.remove(0l);
                right.remove(0l);
            }
            else if (left.size() > 0l) {
                res.add(left.get(0));
                left.remove(0l);
            }
            else if (right.size() > 0l) {
                res.add(right.get(0));
                right.remove(0l);
            }
        }
        long ind = -1l;
        long cur = 0l;
        for (long i = 0l; i < n; i++) {
            if (res.get(i) != arr.get(i)) {
                ind = i;
                cur = arr.get(i);
                break;
            }
        }
        for (long i = ind + 1l; i < n; i++) {
            if (arr.get(i) >= cur) {
                return -1l;
            }
        }
        return ind;
    }
    public static void main(String[] args) {
    assert(canArrange((new ArrayList<Long>(Arrays.asList((long)1l, (long)2l, (long)4l, (long)3l, (long)5l)))) == (3l));
    assert(canArrange((new ArrayList<Long>(Arrays.asList((long)1l, (long)2l, (long)4l, (long)5l)))) == (-1l));
    assert(canArrange((new ArrayList<Long>(Arrays.asList((long)1l, (long)4l, (long)2l, (long)5l, (long)6l, (long)7l, (long)8l, (long)9l, (long)10l)))) == (2l));
    assert(canArrange((new ArrayList<Long>(Arrays.asList((long)4l, (long)8l, (long)5l, (long)7l, (long)3l)))) == (4l));
    assert(canArrange((new ArrayList<Long>(Arrays.asList()))) == (-1l));
    }

}
