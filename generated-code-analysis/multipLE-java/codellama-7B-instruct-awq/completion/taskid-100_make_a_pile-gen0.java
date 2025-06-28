import java.util.*;
import java.lang.reflect.*;
import org.javatuples.*;
import java.security.*;
import java.math.*;
import java.io.*;
import java.util.stream.*;
class Problem {
    // Given a positive integer n, you have to make a pile of n levels of stones.
    // The first level has n stones.
    // The number of stones in the next level is:
    // - the next odd number if n is odd.
    // - the next even number if n is even.
    // Return the number of stones in each level in an array array list, where element at index
    // i represents the number of stones in the level (i+1).
    // Examples:
    // >>> makeAPile((3l))
    // (new ArrayList<Long>(Arrays.asList((long)3l, (long)5l, (long)7l)))
    public static ArrayList<Long> makeAPile(long n) {

        long i = 1;
        ArrayList<Long> r = new ArrayList<Long>();
        while (i <= n) {
            r.add(i);
            i = (i % 2 == 0) ? i + 2 : i + 1;
        }
        return r;
    }
    public static void main(String[] args) {
    assert(makeAPile((3l)).equals((new ArrayList<Long>(Arrays.asList((long)3l, (long)5l, (long)7l)))));
    assert(makeAPile((4l)).equals((new ArrayList<Long>(Arrays.asList((long)4l, (long)6l, (long)8l, (long)10l)))));
    assert(makeAPile((5l)).equals((new ArrayList<Long>(Arrays.asList((long)5l, (long)7l, (long)9l, (long)11l, (long)13l)))));
    assert(makeAPile((6l)).equals((new ArrayList<Long>(Arrays.asList((long)6l, (long)8l, (long)10l, (long)12l, (long)14l, (long)16l)))));
    assert(makeAPile((8l)).equals((new ArrayList<Long>(Arrays.asList((long)8l, (long)10l, (long)12l, (long)14l, (long)16l, (long)18l, (long)20l, (long)22l)))));
    }

}
