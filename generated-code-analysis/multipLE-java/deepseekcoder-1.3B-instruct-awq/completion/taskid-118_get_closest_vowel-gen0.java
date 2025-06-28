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

        String res = "";
        char lastChar = word.charAt(word.length()-1);
        if(word.indexOf('a') != -1 || word.indexOf('A') != -1){
            res = "No vowel between consonant and end";
        } else if(word.indexOf('e') != -1 || word.indexOf('E') != -1){
            res = "No vowel between consonant and end";
        } else if(word.indexOf('i') != -1 || word.indexOf('I') != -1){
            res = "No vowel between consonant and end";
        } else if(word.indexOf('o') != -1 || word.indexOf('O') != -1){
            res = "No vowel between consonant and end";
        } else if(word.indexOf('u') != -1 || word.indexOf('U') != -1){
            res = "No vowel between consonant and end";
        } 
        if(res.equals("No vowel between consonant and end")){
            res = "";
            for(int i = word.length()-1; i >= 2; i--){
                if((word.charAt(i) == 'a' || word.charAt(i) == 'A') && (word.charAt(i-1) == 'e' || word.charAt(i-1) == 'E') && (word.charAt(i-2) == 'i' || word.charAt(i-2) == 'I') && (word.charAt(i-3) == 'o' || word.charAt(i-3) == 'O') && (word.charAt(i-4) == 'u' || word.charAt(i-4) == 'U')){
                    res = String.valueOf(word.charAt(i));
                    break;
                }
            }
        } 
        return res;
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
