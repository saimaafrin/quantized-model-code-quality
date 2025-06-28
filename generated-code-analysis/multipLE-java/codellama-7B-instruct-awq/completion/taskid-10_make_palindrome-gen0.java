import java.util.*;
import java.lang.reflect.*;
import org.javatuples.*;
import java.security.*;
import java.math.*;
import java.io.*;
import java.util.stream.*;
class Problem {
    // Find the shortest palindrome that begins with a supplied string.
    // Algorithm idea is simple:
    // - Find the longest postfix of supplied string that is a palindrome.
    // - Append to the end of the string reverse of a string prefix that comes before the palindromic suffix.
    // >>> makePalindrome((""))
    // ("")
    // >>> makePalindrome(("cat"))
    // ("catac")
    // >>> makePalindrome(("cata"))
    // ("catac")
    public static String makePalindrome(String string) {

        String palindrome = string;
        String postfix = "";
        for (int i = 0; i < string.length() / 2; i++) {
            char c1 = string.charAt(i);
            char c2 = string.charAt(string.length() - 1 - i);
            if (c1 == c2) {
                postfix += c1;
            } else {
                break;
            }
        }
        String prefix = "";
        for (int i = 0; i < string.length() / 2; i++) {
            char c1 = string.charAt(i);
            char c2 = string.charAt(string.length() - 1 - i);
            if (c1 == c2) {
                prefix += c1;
            } else {
                break;
            }
        }
        prefix = new StringBuffer(prefix).reverse().toString();
        return palindrome + prefix;
    }
    public static void main(String[] args) {
    assert(makePalindrome(("")).equals(("")));
    assert(makePalindrome(("x")).equals(("x")));
    assert(makePalindrome(("xyz")).equals(("xyzyx")));
    assert(makePalindrome(("xyx")).equals(("xyx")));
    assert(makePalindrome(("jerry")).equals(("jerryrrej")));
    }

}
