import java.util.*;
import java.lang.reflect.*;
import org.javatuples.*;
import java.security.*;
import java.math.*;
import java.io.*;
import java.util.stream.*;
class Problem {
    // Checks if given string is a palindrome
    // >>> isPalindrome((""))
    // (true)
    // >>> isPalindrome(("aba"))
    // (true)
    // >>> isPalindrome(("aaaaa"))
    // (true)
    // >>> isPalindrome(("zbcd"))
    // (false)
    public static boolean isPalindrome(String text) {

        // Convert string to lowercase
        String lowerText = text.toLowerCase();
        // Remove all characters that are not letters or numbers
        String alphanumeric = lowerText.replaceAll("[^a-zA-Z0-9]", "");
        // Create a char array of the remaining characters
        char[] charArray = alphanumeric.toCharArray();
        // Check if the length is odd or even, and set the midpoint accordingly
        int midpoint = 0;
        if (alphanumeric.length() % 2 == 0) {
            // Length is even
            midpoint = alphanumeric.length() / 2;
        }
        else {
            // Length is odd
            midpoint = (alphanumeric.length() + 1) / 2;
        }
        // Iterate through the char array, comparing characters at the beginning and end of the string
        for (int i = 0; i < midpoint; i++) {
            // If characters do not match, return false
            if (charArray[i] != charArray[alphanumeric.length() - 1 - i]) {
                return false;
            }
        }
        // If the loop completes successfully, return true
        return true;
    }
    public static void main(String[] args) {
    assert(isPalindrome(("")) == (true));
    assert(isPalindrome(("aba")) == (true));
    assert(isPalindrome(("aaaaa")) == (true));
    assert(isPalindrome(("zbcd")) == (false));
    assert(isPalindrome(("xywyx")) == (true));
    assert(isPalindrome(("xywyz")) == (false));
    assert(isPalindrome(("xywzx")) == (false));
    }

}
