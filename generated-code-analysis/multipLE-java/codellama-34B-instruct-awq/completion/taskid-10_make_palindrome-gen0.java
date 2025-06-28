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

        if (string.length() == 0) {
            return "";
        }
        // Find the longest postfix of supplied string that is a palindrome.
        // A palindrome is any string that is the same when read backwards or forwards.
        int i = string.length() - 1;
        int j = string.length();
        // We use a simple O(n**2) algorithm that checks if the string is a palindrome.
        // This could be optimized to O(n) using Manacher's algorithm.
        while (i >= 0 && string.charAt(i) == string.charAt(j - 1)) {
            i -= 1;
            j += 1;
        }
        int palindrome_length = j - i - 1;
        // Now that we have the longest palindrome, we can construct the shortest palindrome.
        int string_length = string.length();
        if (palindrome_length == string_length) {
            return string;
        } else if (palindrome_length == 0) {
            return string + new StringBuilder(string).reverse().toString();
        } else {
            int prefix_length = string_length - palindrome_length;
            return string.substring(0, prefix_length) + string.substring(prefix_length, string_length) + new StringBuilder(string.substring(0, prefix_length)).reverse().toString();
        }
    }
    public static void main(String[] args) {
    assert(makePalindrome(("")).equals(("")));
    assert(makePalindrome(("x")).equals(("x")));
    assert(makePalindrome(("xyz")).equals(("xyzyx")));
    assert(makePalindrome(("xyx")).equals(("xyx")));
    assert(makePalindrome(("jerry")).equals(("jerryrrej")));
    }

}
