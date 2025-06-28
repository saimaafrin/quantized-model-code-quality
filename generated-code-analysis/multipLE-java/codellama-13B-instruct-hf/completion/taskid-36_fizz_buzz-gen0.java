import java.util.*;
import java.lang.reflect.*;
import org.javatuples.*;
import java.security.*;
import java.math.*;
import java.io.*;
import java.util.stream.*;
class Problem {
    // Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    // >>> fizzBuzz((50l))
    // (0l)
    // >>> fizzBuzz((78l))
    // (2l)
    // >>> fizzBuzz((79l))
    // (3l)
    public static long fizzBuzz(long n) {

        List<Long> factors = new ArrayList<>();
        for (long i = 1l; i <= n; i++) {
            if ((i % 11l == 0l || i % 13l == 0l) && i % 7l != 0l)
                factors.add(i);
        }
        long count = 0l;
        for (long factor : factors) {
            String str = String.valueOf(factor);
            for (int i = 0; i < str.length(); i++) {
                if (str.charAt(i) == '7') {
                    count++;
                }
            }
        }
        return count;
    }
    public static void main(String[] args) {
    assert(fizzBuzz((50l)) == (0l));
    assert(fizzBuzz((78l)) == (2l));
    assert(fizzBuzz((79l)) == (3l));
    assert(fizzBuzz((100l)) == (3l));
    assert(fizzBuzz((200l)) == (6l));
    assert(fizzBuzz((4000l)) == (192l));
    assert(fizzBuzz((10000l)) == (639l));
    assert(fizzBuzz((100000l)) == (8026l));
    }

}
