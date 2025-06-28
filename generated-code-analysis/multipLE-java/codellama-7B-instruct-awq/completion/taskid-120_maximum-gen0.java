import java.util.*;
import java.lang.reflect.*;
import org.javatuples.*;
import java.security.*;
import java.math.*;
import java.io.*;
import java.util.stream.*;
class Problem {
    // Given an array array list arr of integers and a positive integer k, return a sorted array list 
    // of length k with the maximum k numbers in arr.
    // Example 1:
    // >>> maximum((new ArrayList<Long>(Arrays.asList((long)-3l, (long)-4l, (long)5l))), (3l))
    // (new ArrayList<Long>(Arrays.asList((long)-4l, (long)-3l, (long)5l)))
    // Example 2:
    // >>> maximum((new ArrayList<Long>(Arrays.asList((long)4l, (long)-4l, (long)4l))), (2l))
    // (new ArrayList<Long>(Arrays.asList((long)4l, (long)4l)))
    // Example 3:
    // >>> maximum((new ArrayList<Long>(Arrays.asList((long)-3l, (long)2l, (long)1l, (long)2l, (long)-1l, (long)-2l, (long)1l))), (1l))
    // (new ArrayList<Long>(Arrays.asList((long)2l)))
    // Note:
    // 1. The length of the array array list will be in the range of [1, 1000].
    // 2. The elements in the array array list will be in the range of [-1000, 1000].
    // 3. 0 <= k <= len(arr)
    public static ArrayList<Long> maximum(ArrayList<Long> arr, long k) {

        // I will be using a bucket sort algorithm, 
        // since it is a very efficient method of sorting.
        // To make the algorithm even more efficient, I will be using a technique called a "bucket sort".
        // The way this works is that I will be dividing the array into a number of buckets, 
        // and then filling each bucket with the numbers in the array that fit within the bounds of the bucket.
        // Then, I will be going through each bucket and counting the number of numbers in each bucket.
        // Then, I will be sorting the buckets and putting them into the final array.
        // This is an efficient method of sorting because it uses a very small amount of memory.
        long max = 0;
        long min = 0;
        for (long l : arr) {
            max = (l > max) ? l : max;
            min = (l < min) ? l : min;
        }
        // The number of buckets that I will be using will be the number of buckets that the array can be divided into.
        // This is given by the number of buckets required to divide the range of the array.
        // For example, if the array is from -10 to 10, then the number of buckets that are needed is 10.
        // To calculate this, I will be dividing the range of the array by the size of the bucket.
        // For example, if the range of the array is from -10 to 10 and the size of the bucket is 2, 
        // then the number of buckets that are needed is 10 / 2 = 5.
        long buckets = (max - min) / k;
        // The size of each bucket will be the size of the bucket.
        // To calculate this, I will be dividing the range of the array by the number of buckets.
        // For example, if the range of the array is from -10 to 10 and the number of buckets is 5, 
        // then the size of each bucket will be 10 / 5 = 2.
        long bucketSize = (max - min) / buckets;
        // Now, I will be creating the buckets.
        // To do this, I will be creating a two-dimensional array list of the same size as the array.
        // This will be the number of buckets that I will be using, 
        // with each bucket being a list of the numbers that fit within its boundaries.
        ArrayList<ArrayList<Long>> buckets = new ArrayList<ArrayList<Long>>();
        for (long
    }
    public static void main(String[] args) {
    assert(maximum((new ArrayList<Long>(Arrays.asList((long)-3l, (long)-4l, (long)5l))), (3l)).equals((new ArrayList<Long>(Arrays.asList((long)-4l, (long)-3l, (long)5l)))));
    assert(maximum((new ArrayList<Long>(Arrays.asList((long)4l, (long)-4l, (long)4l))), (2l)).equals((new ArrayList<Long>(Arrays.asList((long)4l, (long)4l)))));
    assert(maximum((new ArrayList<Long>(Arrays.asList((long)-3l, (long)2l, (long)1l, (long)2l, (long)-1l, (long)-2l, (long)1l))), (1l)).equals((new ArrayList<Long>(Arrays.asList((long)2l)))));
    assert(maximum((new ArrayList<Long>(Arrays.asList((long)123l, (long)-123l, (long)20l, (long)0l, (long)1l, (long)2l, (long)-3l))), (3l)).equals((new ArrayList<Long>(Arrays.asList((long)2l, (long)20l, (long)123l)))));
    assert(maximum((new ArrayList<Long>(Arrays.asList((long)-123l, (long)20l, (long)0l, (long)1l, (long)2l, (long)-3l))), (4l)).equals((new ArrayList<Long>(Arrays.asList((long)0l, (long)1l, (long)2l, (long)20l)))));
    assert(maximum((new ArrayList<Long>(Arrays.asList((long)5l, (long)15l, (long)0l, (long)3l, (long)-13l, (long)-8l, (long)0l))), (7l)).equals((new ArrayList<Long>(Arrays.asList((long)-13l, (long)-8l, (long)0l, (long)0l, (long)3l, (long)5l, (long)15l)))));
    assert(maximum((new ArrayList<Long>(Arrays.asList((long)-1l, (long)0l, (long)2l, (long)5l, (long)3l, (long)-10l))), (2l)).equals((new ArrayList<Long>(Arrays.asList((long)3l, (long)5l)))));
    assert(maximum((new ArrayList<Long>(Arrays.asList((long)1l, (long)0l, (long)5l, (long)-7l))), (1l)).equals((new ArrayList<Long>(Arrays.asList((long)5l)))));
    assert(maximum((new ArrayList<Long>(Arrays.asList((long)4l, (long)-4l))), (2l)).equals((new ArrayList<Long>(Arrays.asList((long)-4l, (long)4l)))));
    assert(maximum((new ArrayList<Long>(Arrays.asList((long)-10l, (long)10l))), (2l)).equals((new ArrayList<Long>(Arrays.asList((long)-10l, (long)10l)))));
    assert(maximum((new ArrayList<Long>(Arrays.asList((long)1l, (long)2l, (long)3l, (long)-23l, (long)243l, (long)-400l, (long)0l))), (0l)).equals((new ArrayList<Long>(Arrays.asList()))));
    }

}
