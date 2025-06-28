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
        int[] suffixArray = new int[n + 1];
        suffixArray[0] = -1;
        for (int i = 0; i < n; i++) {
            int j = i;
            int k = 0;
            while (j >= 0 && k < n && string.charAt(j) == string.charAt(n - k - 1)) {
                j--;
                k++;
            }
            suffixArray[i + 1] = k;
        }
        int maxPalindromeEnd = 0;
        for (int i = 1; i <= n; i++) {
            while (maxPalindromeEnd > 0 && suffixArray[maxPalindromeEnd + 1] < i) {
                maxPalindromeEnd--;
            }
            if (suffixArray[i] > maxPalindromeEnd) {
                maxPalindromeEnd = i;
            }
        }
        String postfix = string.substring(maxPalindromeEnd);
        String prefix = string.substring(0, maxPalindromeEnd);
        StringBuilder builder = new StringBuilder(postfix);
        builder.append(new StringBuilder(prefix).reverse().toString());
        return builder.toString();
    }
    public static void main(String[] args) {
    assert(makePalindrome(("")).equals(("")));
    assert(makePalindrome(("x")).equals(("x")));
    assert(makePalindrome(("xyz")).equals(("xyzyx")));
    assert(makePalindrome(("xyx")).equals(("xyx")));
    assert(makePalindrome(("jerry")).equals(("jerryrrej")));
    }

}
