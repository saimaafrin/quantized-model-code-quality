import java.util.*;
import java.lang.reflect.*;
import org.javatuples.*;
import java.security.*;
import java.math.*;
import java.io.*;
import java.util.stream.*;
class Problem {
    // Given a hash map, return true if all keys are strings in lower 
    // case or all keys are strings in upper case, else return false.
    // The function should return false is the given hash map is empty.
    // Examples:
    // >>> checkDictCase((new HashMap<String,String>(Map.of("a", "apple", "b", "banana"))))
    // (true)
    // >>> checkDictCase((new HashMap<String,String>(Map.of("a", "apple", "A", "banana", "B", "banana"))))
    // (false)
    // >>> checkDictCase((new HashMap<String,String>(Map.of("a", "apple", 8l, "banana", "a", "apple"))))
    // (false)
    // >>> checkDictCase((new HashMap<String,String>(Map.of("Name", "John", "Age", "36", "City", "Houston"))))
    // (false)
    // >>> checkDictCase((new HashMap<String,String>(Map.of("STATE", "NC", "ZIP", "12345"))))
    // (true)
    public static boolean checkDictCase(HashMap<String,String> dict) {

        // Checking the dictionary is empty.
        if (dict.size() == 0) return false;

        // Getting the keys of the dictionary.
        Set<String> keys = dict.keySet();

        // Storing the first uppercase string in the dictionary.
        String firstUppercaseString = null;

        // Checking if all the keys in the dictionary are strings in uppercase.
        for (String key : keys) {
            if (firstUppercaseString == null) firstUppercaseString = key;
            else if (firstUppercaseString.equals(key) == false) return false;
        }

        // If the keys are all in uppercase, return true.
        if (firstUppercaseString.equals(firstUppercaseString.toUpperCase())) return true;

        // Storing the first lowercase string in the dictionary.
        String firstLowercaseString = null;

        // Checking if all the keys in the dictionary are strings in lowercase.
        for (String key : keys) {
            if (firstLowercaseString == null) firstLowercaseString = key;
            else if (firstLowercaseString.equals(key) == false) return false;
        }

        // If the keys are all in lowercase, return true.
        if (firstLowercaseString.equals(firstLowercaseString.toLowerCase())) return true;

        // Otherwise, return false.
        return false;
    }
    public static void main(String[] args) {
    assert(checkDictCase((new HashMap<String,String>(Map.of("p", "pineapple", "b", "banana")))) == (true));
    assert(checkDictCase((new HashMap<String,String>(Map.of("p", "pineapple", "A", "banana", "B", "banana")))) == (false));
    assert(checkDictCase((new HashMap<String,String>(Map.of("p", "pineapple", "5", "banana", "a", "apple")))) == (false));
    assert(checkDictCase((new HashMap<String,String>(Map.of("Name", "John", "Age", "36", "City", "Houston")))) == (false));
    assert(checkDictCase((new HashMap<String,String>(Map.of("STATE", "NC", "ZIP", "12345")))) == (true));
    assert(checkDictCase((new HashMap<String,String>(Map.of("fruit", "Orange", "taste", "Sweet")))) == (true));
    assert(checkDictCase((new HashMap<String,String>())) == (false));
    }

}
