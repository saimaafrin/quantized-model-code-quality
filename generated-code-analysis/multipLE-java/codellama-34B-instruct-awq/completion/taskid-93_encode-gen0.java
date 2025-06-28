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

        String ans = "";
        for (int i = 0; i < message.length(); i++) {
            char ch = message.charAt(i);
            if (ch >= 'a' && ch <= 'z') {
                if (ch == 'a')
                    ch = 'c';
                else if (ch == 'e')
                    ch = 'g';
                else if (ch == 'i')
                    ch = 'k';
                else if (ch == 'o')
                    ch = 'm';
                else if (ch == 'u')
                    ch = 'o';
                else
                    ch += 2;
            } else if (ch >= 'A' && ch <= 'Z') {
                if (ch == 'A')
                    ch = 'C';
                else if (ch == 'E')
                    ch = 'G';
                else if (ch == 'I')
                    ch = 'K';
                else if (ch == 'O')
                    ch = 'M';
                else if (ch == 'U')
                    ch = 'O';
                else
                    ch += 2;
            }
            ans += ch;
        }
        return ans;
    }
    public static void main(String[] args) {
    assert(encode(("TEST")).equals(("tgst")));
    assert(encode(("Mudasir")).equals(("mWDCSKR")));
    assert(encode(("YES")).equals(("ygs")));
    assert(encode(("This is a message")).equals(("tHKS KS C MGSSCGG")));
    assert(encode(("I DoNt KnOw WhAt tO WrItE")).equals(("k dQnT kNqW wHcT Tq wRkTg")));
    }

}
