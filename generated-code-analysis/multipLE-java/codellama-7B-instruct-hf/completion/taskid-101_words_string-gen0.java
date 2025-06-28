import java.util.*;
import java.lang.reflect.*;
import org.javatuples.*;
import java.security.*;
import java.math.*;
import java.io.*;
import java.util.stream.*;
class Problem {
    // You will be given a string of words separated by commas or spaces. Your task is
    // to split the string into words and return an array array list of the words.
    // For example:
    // >>> wordsString(("Hi, my name is John"))
    // (new ArrayList<String>(Arrays.asList((String)"Hi", (String)"my", (String)"name", (String)"is", (String)"John")))
    // >>> wordsString(("One, two, three, four, five, six"))
    // (new ArrayList<String>(Arrays.asList((String)"One", (String)"two", (String)"three", (String)"four", (String)"five", (String)"six")))
    public static ArrayList<String> wordsString(String s) {

        String[] words = s.split("[ ,]");
        return new ArrayList<String>(Arrays.asList(words));
    }
    public static void main(String[] args) {
    assert(wordsString(("Hi, my name is John")).equals((new ArrayList<String>(Arrays.asList((String)"Hi", (String)"my", (String)"name", (String)"is", (String)"John")))));
    assert(wordsString(("One, two, three, four, five, six")).equals((new ArrayList<String>(Arrays.asList((String)"One", (String)"two", (String)"three", (String)"four", (String)"five", (String)"six")))));
    assert(wordsString(("Hi, my name")).equals((new ArrayList<String>(Arrays.asList((String)"Hi", (String)"my", (String)"name")))));
    assert(wordsString(("One,, two, three, four, five, six,")).equals((new ArrayList<String>(Arrays.asList((String)"One", (String)"two", (String)"three", (String)"four", (String)"five", (String)"six")))));
    assert(wordsString(("")).equals((new ArrayList<String>(Arrays.asList()))));
    assert(wordsString(("ahmed     , gamal")).equals((new ArrayList<String>(Arrays.asList((String)"ahmed", (String)"gamal")))));
    }

}
