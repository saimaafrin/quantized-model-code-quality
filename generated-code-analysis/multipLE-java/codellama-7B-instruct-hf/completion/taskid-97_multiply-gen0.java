import java.util.*;
import java.lang.reflect.*;
import org.javatuples.*;
import java.security.*;
import java.math.*;
import java.io.*;
import java.util.stream.*;
class Problem {
    // Complete the function that takes two integers and returns 
    // the product of their unit digits.
    // Assume the input is always valid.
    // Examples:
    // >>> multiply((148l), (412l))
    // (16l)
    // >>> multiply((19l), (28l))
    // (72l)
    // >>> multiply((2020l), (1851l))
    // (0l)
    // >>> multiply((14l), (-15l))
    // (20l)
    public static long multiply(long a, long b) {

        if(a == 0 || b == 0)
            return 0;
        return ((int)(a%10)*(int)(b%10));
    }
    public static void main(String[] args) {
    assert(multiply((148l), (412l)) == (16l));
    assert(multiply((19l), (28l)) == (72l));
    assert(multiply((2020l), (1851l)) == (0l));
    assert(multiply((14l), (-15l)) == (20l));
    assert(multiply((76l), (67l)) == (42l));
    assert(multiply((17l), (27l)) == (49l));
    assert(multiply((0l), (1l)) == (0l));
    assert(multiply((0l), (0l)) == (0l));
    }

}
