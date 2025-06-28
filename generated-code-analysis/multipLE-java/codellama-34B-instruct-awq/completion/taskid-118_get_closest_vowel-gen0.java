import java.util.*;
import java.lang.reflect.*;
import org.javatuples.*;
import java.security.*;
import java.math.*;
import java.io.*;
import java.util.stream.*;
class Problem {
    // You are given a word. Your task is to find the closest vowel that stands between 
    // two consonants from the right side of the word (case sensitive).
    // Vowels in the beginning and ending doesn't count. Return empty string if you didn't
    // find any vowel met the above condition. 
    // You may assume that the given string contains English letter only.
    // Example:
    // >>> getClosestVowel(("yogurt"))
    // ("u")
    // >>> getClosestVowel(("FULL"))
    // ("U")
    // >>> getClosestVowel(("quick"))
    // ("")
    // >>> getClosestVowel(("ab"))
    // ("")
    public static String getClosestVowel(String word) {

        // Write your code here
        String[] vowels = "aeiou".split("");
        String[] consonants = "bcdfghjklmnpqrstvwxyz".split("");
        String result = "";
        for (int i = 0; i < word.length(); i++) {
            if (vowels[0].equals(word.charAt(i) + "") || vowels[1].equals(word.charAt(i) + "") || vowels[2].equals(word.charAt(i) + "")
                    || vowels[3].equals(word.charAt(i) + "") || vowels[4].equals(word.charAt(i) + "") || vowels[5].equals(word.charAt(i) + "")) {
                for (int j = 0; j < consonants.length; j++) {
                    if (word.charAt(i - 1) == consonants[j].charAt(0) && word.charAt(i + 1) == consonants[j].charAt(0)) {
                        result = word.charAt(i) + "";
                    }
                }
            }
        }
        return result;
    }
    public static void main(String[] args) {
    assert(getClosestVowel(("yogurt")).equals(("u")));
    assert(getClosestVowel(("full")).equals(("u")));
    assert(getClosestVowel(("easy")).equals(("")));
    assert(getClosestVowel(("eAsy")).equals(("")));
    assert(getClosestVowel(("ali")).equals(("")));
    assert(getClosestVowel(("bad")).equals(("a")));
    assert(getClosestVowel(("most")).equals(("o")));
    assert(getClosestVowel(("ab")).equals(("")));
    assert(getClosestVowel(("ba")).equals(("")));
    assert(getClosestVowel(("quick")).equals(("")));
    assert(getClosestVowel(("anime")).equals(("i")));
    assert(getClosestVowel(("Asia")).equals(("")));
    assert(getClosestVowel(("Above")).equals(("o")));
    }

}
