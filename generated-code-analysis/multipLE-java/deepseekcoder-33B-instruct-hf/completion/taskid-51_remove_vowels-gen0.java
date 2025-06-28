import java.util.*;
import java.lang.reflect.*;
import org.javatuples.*;
import java.security.*;
import java.math.*;
import java.io.*;
import java.util.stream.*;
class Problem {
    // remove_vowels is a function that takes string and returns string without vowels.
    // >>> removeVowels((""))
    // ("")
    // >>> removeVowels(("abcdef"))
    // ("bcdf")
    // >>> removeVowels(("aaaaa"))
    // ("")
    // >>> removeVowels(("aaBAA"))
    // ("B")
    // >>> removeVowels(("zbcd"))
    // ("zbcd")
    public static String removeVowels(String text) {

        List<Character> vowels = Arrays.asList('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U');
        String result = "";
        for (int i = 0; i < text.length(); i++) {
            char ch = text.charAt(i);
            if (!vowels.contains(ch)) {
                result += ch;
            }
        }
        return result;
    }
    public static void main(String[] args) {
    assert(removeVowels(("")).equals(("")));
    assert(removeVowels(("abcdef\nghijklm")).equals(("bcdf\nghjklm")));
    assert(removeVowels(("fedcba")).equals(("fdcb")));
    assert(removeVowels(("eeeee")).equals(("")));
    assert(removeVowels(("acBAA")).equals(("cB")));
    assert(removeVowels(("EcBOO")).equals(("cB")));
    assert(removeVowels(("ybcd")).equals(("ybcd")));
    }

}
