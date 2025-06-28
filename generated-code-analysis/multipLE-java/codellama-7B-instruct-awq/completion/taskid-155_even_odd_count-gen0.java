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

        Pair<Long, Long> ret = Pair.with(0l, 0l);
        while (num != 0) {
            long lastDigit = num % 10;
            if (lastDigit % 2 == 0) {
                ret.setA(ret.getValue0() + 1);
            } else {
                ret.setB(ret.getValue1() + 1);
            }
            num /= 10;
        }
        return ret;
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
