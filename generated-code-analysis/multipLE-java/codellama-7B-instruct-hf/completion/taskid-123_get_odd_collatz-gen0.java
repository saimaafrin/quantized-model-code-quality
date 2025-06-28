import java.util.*;
import java.lang.reflect.*;
import org.javatuples.*;
import java.security.*;
import java.math.*;
import java.io.*;
import java.util.stream.*;
class Problem {
    // Given a positive integer n, return a sorted array list that has the odd numbers in collatz sequence.
    // The Collatz conjecture is a conjecture in mathematics that concerns a sequence defined
    // as follows: start with any positive integer n. Then each term is obtained from the 
    // previous term as follows: if the previous term is even, the next term is one half of 
    // the previous term. If the previous term is odd, the next term is 3 times the previous
    // term plus 1. The conjecture is that no matter what value of n, the sequence will always reach 1.
    // Note: 
    // 1. Collatz(1) is [1].
    // 2. returned array list sorted in increasing order.
    // For example:
    // get_odd_collatz(5) returns [1, 5] # The collatz sequence for 5 is [5, 16, 8, 4, 2, 1], so the odd numbers are only 1, and 5.
    // >>> getOddCollatz((5l))
    // (new ArrayList<Long>(Arrays.asList((long)1l, (long)5l)))
    public static ArrayList<Long> getOddCollatz(long n) {

        ArrayList<Long> ans = new ArrayList<Long>();
        while (n != 1) {
            if (n % 2 == 0) {
                n = n / 2;
            } else {
                n = (3 * n) + 1;
            }
            ans.add(n);
        }
        return ans;
    }
    public static void main(String[] args) {
    assert(getOddCollatz((14l)).equals((new ArrayList<Long>(Arrays.asList((long)1l, (long)5l, (long)7l, (long)11l, (long)13l, (long)17l)))));
    assert(getOddCollatz((5l)).equals((new ArrayList<Long>(Arrays.asList((long)1l, (long)5l)))));
    assert(getOddCollatz((12l)).equals((new ArrayList<Long>(Arrays.asList((long)1l, (long)3l, (long)5l)))));
    assert(getOddCollatz((1l)).equals((new ArrayList<Long>(Arrays.asList((long)1l)))));
    }

}
