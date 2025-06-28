import java.util.*;
import java.lang.reflect.*;
import org.javatuples.*;
import java.security.*;
import java.math.*;
import java.io.*;
import java.util.stream.*;
class Problem {
    // Implement a function that takes an non-negative integer and returns an array array list of the first n
    // integers that are prime numbers and less than n.
    // for example:
    // >>> countUpTo((5l))
    // (new ArrayList<Long>(Arrays.asList((long)2l, (long)3l)))
    // >>> countUpTo((11l))
    // (new ArrayList<Long>(Arrays.asList((long)2l, (long)3l, (long)5l, (long)7l)))
    // >>> countUpTo((0l))
    // (new ArrayList<Long>(Arrays.asList()))
    // >>> countUpTo((20l))
    // (new ArrayList<Long>(Arrays.asList((long)2l, (long)3l, (long)5l, (long)7l, (long)11l, (long)13l, (long)17l, (long)19l)))
    // >>> countUpTo((1l))
    // (new ArrayList<Long>(Arrays.asList()))
    // >>> countUpTo((18l))
    // (new ArrayList<Long>(Arrays.asList((long)2l, (long)3l, (long)5l, (long)7l, (long)11l, (long)13l, (long)17l)))
    public static ArrayList<Long> countUpTo(long n) {

        ArrayList<Long> res = new ArrayList<Long>();
        for (long i = 2l; i < n; i++) {
            if (isPrime(i)) res.add(i);
        }
        return res;
    }
    public static void main(String[] args) {
    assert(countUpTo((5l)).equals((new ArrayList<Long>(Arrays.asList((long)2l, (long)3l)))));
    assert(countUpTo((6l)).equals((new ArrayList<Long>(Arrays.asList((long)2l, (long)3l, (long)5l)))));
    assert(countUpTo((7l)).equals((new ArrayList<Long>(Arrays.asList((long)2l, (long)3l, (long)5l)))));
    assert(countUpTo((10l)).equals((new ArrayList<Long>(Arrays.asList((long)2l, (long)3l, (long)5l, (long)7l)))));
    assert(countUpTo((0l)).equals((new ArrayList<Long>(Arrays.asList()))));
    assert(countUpTo((22l)).equals((new ArrayList<Long>(Arrays.asList((long)2l, (long)3l, (long)5l, (long)7l, (long)11l, (long)13l, (long)17l, (long)19l)))));
    assert(countUpTo((1l)).equals((new ArrayList<Long>(Arrays.asList()))));
    assert(countUpTo((18l)).equals((new ArrayList<Long>(Arrays.asList((long)2l, (long)3l, (long)5l, (long)7l, (long)11l, (long)13l, (long)17l)))));
    assert(countUpTo((47l)).equals((new ArrayList<Long>(Arrays.asList((long)2l, (long)3l, (long)5l, (long)7l, (long)11l, (long)13l, (long)17l, (long)19l, (long)23l, (long)29l, (long)31l, (long)37l, (long)41l, (long)43l)))));
    assert(countUpTo((101l)).equals((new ArrayList<Long>(Arrays.asList((long)2l, (long)3l, (long)5l, (long)7l, (long)11l, (long)13l, (long)17l, (long)19l, (long)23l, (long)29l, (long)31l, (long)37l, (long)41l, (long)43l, (long)47l, (long)53l, (long)59l, (long)61l, (long)67l, (long)71l, (long)73l, (long)79l, (long)83l, (long)89l, (long)97l)))));
    }

}
