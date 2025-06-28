import java.util.*;
import java.lang.reflect.*;
import org.javatuples.*;
import java.security.*;
import java.math.*;
import java.io.*;
import java.util.stream.*;
class Problem {
    // Your task is to write a function that returns true if a number x is a simple
    // power of n and false in other cases.
    // x is a simple power of n if n**int=x
    // For example:
    // >>> isSimplePower((1l), (4l))
    // (true)
    // >>> isSimplePower((2l), (2l))
    // (true)
    // >>> isSimplePower((8l), (2l))
    // (true)
    // >>> isSimplePower((3l), (2l))
    // (false)
    // >>> isSimplePower((3l), (1l))
    // (false)
    // >>> isSimplePower((5l), (3l))
    // (false)
    public static boolean isSimplePower(long x, long n) {

        // Your code here
        int res = (int)(Math.log10(x)/Math.log10(n));
        return n == Math.pow(n,res);
    }
    public static void main(String[] args) {
    assert(isSimplePower((16l), (2l)) == (true));
    assert(isSimplePower((143214l), (16l)) == (false));
    assert(isSimplePower((4l), (2l)) == (true));
    assert(isSimplePower((9l), (3l)) == (true));
    assert(isSimplePower((16l), (4l)) == (true));
    assert(isSimplePower((24l), (2l)) == (false));
    assert(isSimplePower((128l), (4l)) == (false));
    assert(isSimplePower((12l), (6l)) == (false));
    assert(isSimplePower((1l), (1l)) == (true));
    assert(isSimplePower((1l), (12l)) == (true));
    }

}
