import java.util.*;
import java.lang.reflect.*;
import org.javatuples.*;
import java.security.*;
import java.math.*;
import java.io.*;
import java.util.stream.*;
class Problem {
    // Write a function that takes a message, and encodes in such a 
    // way that it swaps case of all letters, replaces all vowels in 
    // the message with the letter that appears 2 places ahead of that 
    // vowel in the english alphabet. 
    // Assume only letters. 
    // Examples:
    // >>> encode(("test"))
    // ("TGST")
    // >>> encode(("This is a message"))
    // ("tHKS KS C MGSSCGG")
    public static String encode(String message) {

        String result = "";
        char[] charArray = message.toCharArray();
        int offset = 2;
        for (int i = 0; i < charArray.length; i++) {
            char currentChar = charArray[i];
            if (currentChar >= 'a' && currentChar <= 'z') {
                charArray[i] = (char)((currentChar - 'a' + offset) % 26 + 'A');
            } else if (currentChar >= 'A' && currentChar <= 'Z') {
                charArray[i] = (char)((currentChar - 'A' + offset) % 26 + 'a');
            }
        }
        for (int i = 0; i < charArray.length; i++) {
            result += charArray[i];
        }
        return result;
    }
    public static void main(String[] args) {
    assert(encode(("TEST")).equals(("tgst")));
    assert(encode(("Mudasir")).equals(("mWDCSKR")));
    assert(encode(("YES")).equals(("ygs")));
    assert(encode(("This is a message")).equals(("tHKS KS C MGSSCGG")));
    assert(encode(("I DoNt KnOw WhAt tO WrItE")).equals(("k dQnT kNqW wHcT Tq wRkTg")));
    }

}
