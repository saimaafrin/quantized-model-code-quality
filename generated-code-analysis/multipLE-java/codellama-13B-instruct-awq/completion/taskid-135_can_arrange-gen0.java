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

        // add a sentinel to end of list
        // if there is a number that is less than it, swap them
        // if no swap can be done, then return the sentinel index
        // otherwise, remove the sentinel and repeat
        // if you have to swap two elements and get stuck in an infinite loop
        // then return -1
        int sentinel_index = arr.size() - 1;
        while (true) {
            int prev = sentinel_index - 1;
            boolean swapped = false;
            while (prev >= 0) {
                if (arr.get(prev) > arr.get(sentinel_index)) {
                    // swap prev and sentinel_index
                    long prev_val = arr.get(prev);
                    long sentinel_val = arr.get(sentinel_index);
                    arr.set(prev, sentinel_val);
                    arr.set(sentinel_index, prev_val);
                    swapped = true;
                    sentinel_index = prev;
                    break;
                }
                prev--;
            }
            if (prev < 0 && !swapped) {
                // no swap made, sentinel was the smallest
                // remove sentinel and repeat
                arr.remove(sentinel_index);
                sentinel_index = arr.size() - 1;
            } else if (prev < 0 && swapped) {
                // no swap made, sentinel was the smallest
                // remove sentinel and repeat
                return sentinel_index;
            }
        }
    }
    public static void main(String[] args) {
    assert(canArrange((new ArrayList<Long>(Arrays.asList((long)1l, (long)2l, (long)4l, (long)3l, (long)5l)))) == (3l));
    assert(canArrange((new ArrayList<Long>(Arrays.asList((long)1l, (long)2l, (long)4l, (long)5l)))) == (-1l));
    assert(canArrange((new ArrayList<Long>(Arrays.asList((long)1l, (long)4l, (long)2l, (long)5l, (long)6l, (long)7l, (long)8l, (long)9l, (long)10l)))) == (2l));
    assert(canArrange((new ArrayList<Long>(Arrays.asList((long)4l, (long)8l, (long)5l, (long)7l, (long)3l)))) == (4l));
    assert(canArrange((new ArrayList<Long>(Arrays.asList()))) == (-1l));
    }

}
