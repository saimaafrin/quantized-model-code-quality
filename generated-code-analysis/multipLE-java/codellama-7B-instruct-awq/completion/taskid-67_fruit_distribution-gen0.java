import java.util.*;
import java.lang.reflect.*;
import org.javatuples.*;
import java.security.*;
import java.math.*;
import java.io.*;
import java.util.stream.*;
class Problem {
    // In this task, you will be given a string that represents a number of apples and oranges 
    // that are distributed in a basket of fruit this basket contains 
    // apples, oranges, and mango fruits. Given the string that represents the total number of 
    // the oranges and apples and an integer that represent the total number of the fruits 
    // in the basket return the number of the mango fruits in the basket.
    // for examble:
    // >>> fruitDistribution(("5 apples and 6 oranges"), (19l))
    // (8l)
    // >>> fruitDistribution(("0 apples and 1 oranges"), (3l))
    // (2l)
    // >>> fruitDistribution(("2 apples and 3 oranges"), (100l))
    // (95l)
    // >>> fruitDistribution(("100 apples and 1 oranges"), (120l))
    // (19l)
    public static long fruitDistribution(String s, long n) {

        return n - Long.valueOf(s.split(" ")[0]);
    }
    public static void main(String[] args) {
    assert(fruitDistribution(("5 apples and 6 oranges"), (19l)) == (8l));
    assert(fruitDistribution(("5 apples and 6 oranges"), (21l)) == (10l));
    assert(fruitDistribution(("0 apples and 1 oranges"), (3l)) == (2l));
    assert(fruitDistribution(("1 apples and 0 oranges"), (3l)) == (2l));
    assert(fruitDistribution(("2 apples and 3 oranges"), (100l)) == (95l));
    assert(fruitDistribution(("2 apples and 3 oranges"), (5l)) == (0l));
    assert(fruitDistribution(("1 apples and 100 oranges"), (120l)) == (19l));
    }

}
