import java.util.*;
import java.lang.reflect.*;
import org.javatuples.*;
import java.security.*;
import java.math.*;
import java.io.*;
import java.util.stream.*;
class Problem {
    // Add two numbers x and y
    // >>> add((2l), (3l))
    // (5l)
    // >>> add((5l), (7l))
    // (12l)
    public static long add(long x, long y) {

        return x + y;
    }
    public static void main(String[] args) {
    assert(add((0l), (1l)) == (1l));
    assert(add((1l), (0l)) == (1l));
    assert(add((2l), (3l)) == (5l));
    assert(add((5l), (7l)) == (12l));
    assert(add((7l), (5l)) == (12l));
    }

}
