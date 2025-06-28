import java.util.*;
import java.lang.reflect.*;
import org.javatuples.*;
import java.security.*;
import java.math.*;
import java.io.*;
import java.util.stream.*;
class Problem {
    // Given a string s and a natural number n, you have been tasked to implement 
    // a function that returns an array array list of all words from string s that contain exactly 
    // n consonants, in order these words appear in the string s.
    // If the string s is empty then the function should return an empty array list.
    // Note: you may assume the input string contains only letters and spaces.
    // Examples:
    // >>> selectWords(("Mary had a little lamb"), (4l))
    // (new ArrayList<String>(Arrays.asList((String)"little")))
    // >>> selectWords(("Mary had a little lamb"), (3l))
    // (new ArrayList<String>(Arrays.asList((String)"Mary", (String)"lamb")))
    // >>> selectWords(("simple white space"), (2l))
    // (new ArrayList<String>(Arrays.asList()))
    // >>> selectWords(("Hello world"), (4l))
    // (new ArrayList<String>(Arrays.asList((String)"world")))
    // >>> selectWords(("Uncle sam"), (3l))
    // (new ArrayList<String>(Arrays.asList((String)"Uncle")))
    public static ArrayList<String> selectWords(String s, long n) {

        if (n < 0) {
            return new ArrayList<String>(Arrays.asList());
        }
        String[] arr = s.split(" ");
        ArrayList<String> list = new ArrayList<String>();
        String regex = "[aeiou]";
        for (int i = 0; i < arr.length; i++) {
            long vowelCount = arr[i].chars()
                    .mapToObj(c -> (char) c)
                    .filter(c -> c.toString().matches(regex))
                    .count();
            if (vowelCount == n) {
                list.add(arr[i]);
            }
        }
        return list;
    }
    public static void main(String[] args) {
    assert(selectWords(("Mary had a little lamb"), (4l)).equals((new ArrayList<String>(Arrays.asList((String)"little")))));
    assert(selectWords(("Mary had a little lamb"), (3l)).equals((new ArrayList<String>(Arrays.asList((String)"Mary", (String)"lamb")))));
    assert(selectWords(("simple white space"), (2l)).equals((new ArrayList<String>(Arrays.asList()))));
    assert(selectWords(("Hello world"), (4l)).equals((new ArrayList<String>(Arrays.asList((String)"world")))));
    assert(selectWords(("Uncle sam"), (3l)).equals((new ArrayList<String>(Arrays.asList((String)"Uncle")))));
    assert(selectWords((""), (4l)).equals((new ArrayList<String>(Arrays.asList()))));
    assert(selectWords(("a b c d e f"), (1l)).equals((new ArrayList<String>(Arrays.asList((String)"b", (String)"c", (String)"d", (String)"f")))));
    }

}
