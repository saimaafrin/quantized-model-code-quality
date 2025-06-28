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

        String alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ";
        String encoded_msg="";
        for(int i=0; i<message.length(); i++) {
            if(alphabet.contains(String.valueOf(message.charAt(i)))) {
                int index=alphabet.indexOf(String.valueOf(message.charAt(i)));
                int new_index=index+2;
                if(new_index>25) {
                    new_index=new_index-26;
                }
                char new_letter=alphabet.charAt(new_index);
                encoded_msg+=new_letter;
            }
            else {
                encoded_msg+=message.charAt(i);
            }
        }
        return encoded_msg;
    }
    public static void main(String[] args) {
    assert(encode(("TEST")).equals(("tgst")));
    assert(encode(("Mudasir")).equals(("mWDCSKR")));
    assert(encode(("YES")).equals(("ygs")));
    assert(encode(("This is a message")).equals(("tHKS KS C MGSSCGG")));
    assert(encode(("I DoNt KnOw WhAt tO WrItE")).equals(("k dQnT kNqW wHcT Tq wRkTg")));
    }

}
