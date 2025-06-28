import java.util.*;
import java.lang.reflect.*;
import org.javatuples.*;
import java.security.*;
import java.math.*;
import java.io.*;
import java.util.stream.*;
class Problem {
    // Input are two strings a and b consisting only of 1s and 0s.
    // Perform binary XOR on these inputs and return result also as a string.
    // >>> stringXor(("010"), ("110"))
    // ("100")
    public static String stringXor(String a, String b) {

        if (a.length() != b.length()) throw new RuntimeException("Length of input strings must match!");
        StringBuilder result = new StringBuilder();
        for (int i = 0; i < a.length(); i++) {
            int bitA = Character.getNumericValue(a.charAt(i));
            int bitB = Character.getNumericValue(b.charAt(i));
            result.append(bitA ^ bitB);
        }
        return result.toString();
    }
    public static void main(String[] args) {
    assert(stringXor(("111000"), ("101010")).equals(("010010")));
    assert(stringXor(("1"), ("1")).equals(("0")));
    assert(stringXor(("0101"), ("0000")).equals(("0101")));
    }

}
