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

        // Solution 1
        // String vowels = "aeiou";
        // String consonants = "bcdfghjklmnpqrstvwxyz";
        // int max = -1;
        // String result = "";

        // for(int i=0; i<word.length()-1; i++) {
        //     if(consonants.indexOf(word.charAt(i)) > -1 && consonants.indexOf(word.charAt(i+1)) > -1) {
        //         if(word.charAt(i+1) == 'a' || word.charAt(i+1) == 'e' || word.charAt(i+1) == 'i' || word.charAt(i+1) == 'o' || word.charAt(i+1) == 'u') {
        //             result = String.valueOf(word.charAt(i+1));
        //             break;
        //         }
        //         else {
        //             if(vowels.indexOf(word.charAt(i+1)) > -1) {
        //                 if(max == -1) {
        //                     max = vowels.indexOf(word.charAt(i+1));
        //                     result = String.valueOf(word.charAt(i+1));
        //                 }
        //                 else {
        //                     if(max > vowels.indexOf(word.charAt(i+1))) {
        //                         max = vowels.indexOf(word.charAt(i+1));
        //                         result = String.valueOf(word.charAt(i+1));
        //                     }
        //                 }
        //             }
        //         }
        //     }
        // }

        // Solution 2
        for(int i = word.length()-2; i >= 0; i--) {
            if(word.charAt(i) == 'a' || word.charAt(i) == 'e' || word.charAt(i) == 'i' || word.charAt(i) == 'o' || word.charAt(i) == 'u') {
                if(word.charAt(i+1) == 'a' || word.charAt(i+1) == 'e' || word.charAt(i+1) == 'i' || word.charAt(i+1) == 'o' || word.charAt(i+1) == 'u') {
                    return "";
                }
                else {
                    return String.valueOf(word.charAt(i));
                }
            }
            else if(word.charAt(i) == 'A' || word.charAt(i) == 'E' || word.charAt(i) == 'I' || word.charAt(i) == 'O' || word.charAt(i) == 'U') {
                if(word.charAt(i+1) == 'A' || word.charAt(i+1) == 'E' || word.charAt(i+1) == 'I' || word.charAt(i+1) == 'O' || word.charAt(i+1) == 'U') {
                    return "";
                }
                else {
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
