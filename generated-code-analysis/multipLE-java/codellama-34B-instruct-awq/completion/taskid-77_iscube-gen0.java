import java.util.*;
import java.lang.reflect.*;
import org.javatuples.*;
import java.security.*;
import java.math.*;
import java.io.*;
import java.util.stream.*;
class Problem {
    // Write a function that takes an integer a and returns true 
    // if this ingeger is a cube of some integer number.
    // Note: you may assume the input is always valid.
    // Examples:
    // >>> iscube((1l))
    // (true)
    // >>> iscube((2l))
    // (false)
    // >>> iscube((-1l))
    // (true)
    // >>> iscube((64l))
    // (true)
    // >>> iscube((0l))
    // (true)
    // >>> iscube((180l))
    // (false)
    public static boolean iscube(long a) {

        double x = Math.pow(Math.abs(a), 1.0/3.0);
        long y = (long) x;
        return (y * y * y == Math.abs(a));
    }
    public static void main(String[] args) {
    assert(iscube((1l)) == (true));
    assert(iscube((2l)) == (false));
    assert(iscube((-1l)) == (true));
    assert(iscube((64l)) == (true));
    assert(iscube((180l)) == (false));
    assert(iscube((1000l)) == (true));
    assert(iscube((0l)) == (true));
    assert(iscube((1729l)) == (false));
    }

}
