import java.util.*;
import java.lang.reflect.*;
import org.javatuples.*;
import java.security.*;
import java.math.*;
import java.io.*;
import java.util.stream.*;
class Problem {
    // Circular shift the digits of the integer x, shift the digits right by shift
    // and return the result as a string.
    // If shift > number of digits, return digits reversed.
    // >>> circularShift((12l), (1l))
    // ("21")
    // >>> circularShift((12l), (2l))
    // ("12")
    public static String circularShift(long x, long shift) {

        // Your code here!
        // Get number of digits from x
        int nDigits = Long.toString(x).length();
        // If shift > nDigits, return reversed string
        if (shift > nDigits) {
            return new StringBuilder(Long.toString(x)).reverse().toString();
        }
        // Shift the digits right by shift
        String s = Long.toString(x);
        char[] ch = s.toCharArray();
        char[] ch2 = new char[ch.length];
        // For each digit in ch
        for (int i = 0; i < ch.length; i++) {
            // Get next index
            int index = (i + shift) % ch.length;
            // Assign digit to next index in ch2
            ch2[index] = ch[i];
        }
        // Return string from ch2
        return new String(ch2);
    }
    public static void main(String[] args) {
    assert(circularShift((100l), (2l)).equals(("001")));
    assert(circularShift((12l), (2l)).equals(("12")));
    assert(circularShift((97l), (8l)).equals(("79")));
    assert(circularShift((12l), (1l)).equals(("21")));
    assert(circularShift((11l), (101l)).equals(("11")));
    }

}
