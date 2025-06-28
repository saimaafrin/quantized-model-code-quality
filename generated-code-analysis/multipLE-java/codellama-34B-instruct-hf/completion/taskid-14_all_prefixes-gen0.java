import java.util.*;
import java.lang.reflect.*;
import org.javatuples.*;
import java.security.*;
import java.math.*;
import java.io.*;
import java.util.stream.*;
class Problem {
    // Return array list of all prefixes from shortest to longest of the input string
    // >>> allPrefixes(("abc"))
    // (new ArrayList<String>(Arrays.asList((String)"a", (String)"ab", (String)"abc")))
    public static ArrayList<String> allPrefixes(String string) {

        ArrayList<String> prefixes = new ArrayList<>();
        for (int i = 0; i < string.length(); i++) {
            prefixes.add(string.substring(0, i+1));
        }
        return prefixes;
    }
    public static void main(String[] args) {
    assert(allPrefixes(("")).equals((new ArrayList<String>(Arrays.asList()))));
    assert(allPrefixes(("asdfgh")).equals((new ArrayList<String>(Arrays.asList((String)"a", (String)"as", (String)"asd", (String)"asdf", (String)"asdfg", (String)"asdfgh")))));
    assert(allPrefixes(("WWW")).equals((new ArrayList<String>(Arrays.asList((String)"W", (String)"WW", (String)"WWW")))));
    }

}
