import java.util.*;
import java.lang.reflect.*;
import org.javatuples.*;
import java.security.*;
import java.math.*;
import java.io.*;
import java.util.stream.*;
class Problem {
    // Given an integer. return a pair that has the number of even and odd digits respectively.
    // Example:
    // >>> evenOddCount((-12l))
    // (Pair.with(1l, 1l))
    // >>> evenOddCount((123l))
    // (Pair.with(1l, 2l))
    public static Pair<Long, Long> evenOddCount(long num) {

        return Pair.with(0l, 0l);
    }
    public static void main(String[] args) {
    assert(evenOddCount((7l)).equals((Pair.with(0l, 1l))));
    assert(evenOddCount((-78l)).equals((Pair.with(1l, 1l))));
    assert(evenOddCount((3452l)).equals((Pair.with(2l, 2l))));
    assert(evenOddCount((346211l)).equals((Pair.with(3l, 3l))));
    assert(evenOddCount((-345821l)).equals((Pair.with(3l, 3l))));
    assert(evenOddCount((-2l)).equals((Pair.with(1l, 0l))));
    assert(evenOddCount((-45347l)).equals((Pair.with(2l, 3l))));
    assert(evenOddCount((0l)).equals((Pair.with(1l, 0l))));
    }

}
