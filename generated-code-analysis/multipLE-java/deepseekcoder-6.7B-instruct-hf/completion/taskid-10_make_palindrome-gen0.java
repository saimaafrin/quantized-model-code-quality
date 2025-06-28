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

        int n = string.length();
        int[] prefixFunction = new int[n+1];
        for (int i = 1; i < n; i++) {
            int j = prefixFunction[i-1];
            while (j > 0 && string.charAt(i) != string.charAt(j)) {
                j = prefixFunction[j-1];
            }
            if (string.charAt(i) == string.charAt(j)) {
                j++;
            }
            prefixFunction[i] = j;
        }
        String palindrome = string + new StringBuilder(string.substring(prefixFunction[n-1])).reverse().toString();
        return palindrome;
    }
    public static void main(String[] args) {
    assert(makePalindrome(("")).equals(("")));
    assert(makePalindrome(("x")).equals(("x")));
    assert(makePalindrome(("xyz")).equals(("xyzyx")));
    assert(makePalindrome(("xyx")).equals(("xyx")));
    assert(makePalindrome(("jerry")).equals(("jerryrrej")));
    }

}
