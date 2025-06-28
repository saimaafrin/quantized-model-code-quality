import java.util.*;
import java.lang.reflect.*;
import org.javatuples.*;
import java.security.*;
import java.math.*;
import java.io.*;
import java.util.stream.*;
class Problem {
    // Given an array array list of integers nums, find the minimum sum of any non-empty sub-array array list
    // of nums.
    // Example
    // >>> minSubArraySum((new ArrayList<Long>(Arrays.asList((long)2l, (long)3l, (long)4l, (long)1l, (long)2l, (long)4l))))
    // (1l)
    // >>> minSubArraySum((new ArrayList<Long>(Arrays.asList((long)-1l, (long)-2l, (long)-3l))))
    // (-6l)
    public static long minSubArraySum(ArrayList<Long> nums) {

        long min = Long.MAX_VALUE;
        long total = 0;
        for (long num : nums) {
            total += num;
            min = Math.min(min, total);
            total = total - num;
        }
        return min;
    }
    public static void main(String[] args) {
    assert(minSubArraySum((new ArrayList<Long>(Arrays.asList((long)2l, (long)3l, (long)4l, (long)1l, (long)2l, (long)4l)))) == (1l));
    assert(minSubArraySum((new ArrayList<Long>(Arrays.asList((long)-1l, (long)-2l, (long)-3l)))) == (-6l));
    assert(minSubArraySum((new ArrayList<Long>(Arrays.asList((long)-1l, (long)-2l, (long)-3l, (long)2l, (long)-10l)))) == (-14l));
    assert(minSubArraySum((new ArrayList<Long>(Arrays.asList((long)-9999999999999999l)))) == (-9999999999999999l));
    assert(minSubArraySum((new ArrayList<Long>(Arrays.asList((long)0l, (long)10l, (long)20l, (long)1000000l)))) == (0l));
    assert(minSubArraySum((new ArrayList<Long>(Arrays.asList((long)-1l, (long)-2l, (long)-3l, (long)10l, (long)-5l)))) == (-6l));
    assert(minSubArraySum((new ArrayList<Long>(Arrays.asList((long)100l, (long)-1l, (long)-2l, (long)-3l, (long)10l, (long)-5l)))) == (-6l));
    assert(minSubArraySum((new ArrayList<Long>(Arrays.asList((long)10l, (long)11l, (long)13l, (long)8l, (long)3l, (long)4l)))) == (3l));
    assert(minSubArraySum((new ArrayList<Long>(Arrays.asList((long)100l, (long)-33l, (long)32l, (long)-1l, (long)0l, (long)-2l)))) == (-33l));
    assert(minSubArraySum((new ArrayList<Long>(Arrays.asList((long)-10l)))) == (-10l));
    assert(minSubArraySum((new ArrayList<Long>(Arrays.asList((long)7l)))) == (7l));
    assert(minSubArraySum((new ArrayList<Long>(Arrays.asList((long)1l, (long)-1l)))) == (-1l));
    }

}
