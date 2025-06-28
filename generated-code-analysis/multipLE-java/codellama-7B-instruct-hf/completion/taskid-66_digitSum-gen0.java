import java.util.*;
import java.lang.reflect.*;
import org.javatuples.*;
import java.security.*;
import java.math.*;
import java.io.*;
import java.util.stream.*;
class Problem {
    // Task
    // Write a function that takes a string as input and returns the sum of the upper characters only'
    // ASCII codes.
    // Examples:
    // >>> digitSum((""))
    // (0l)
    // >>> digitSum(("abAB"))
    // (131l)
    // >>> digitSum(("abcCd"))
    // (67l)
    // >>> digitSum(("helloE"))
    // (69l)
    // >>> digitSum(("woArBld"))
    // (131l)
    // >>> digitSum(("aAaaaXa"))
    // (153l)
    public static long digitSum(String s) {

        long result = 0;
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            int value = Character.isUpperCase(c) ? c : Character.toUpperCase(c);
            result += value;
        }
        return result;
    }
    public static void main(String[] args) {
    assert(digitSum(("")) == (0l));
    assert(digitSum(("abAB")) == (131l));
    assert(digitSum(("abcCd")) == (67l));
    assert(digitSum(("helloE")) == (69l));
    assert(digitSum(("woArBld")) == (131l));
    assert(digitSum(("aAaaaXa")) == (153l));
    assert(digitSum((" How are yOu?")) == (151l));
    assert(digitSum(("You arE Very Smart")) == (327l));
    }

}
