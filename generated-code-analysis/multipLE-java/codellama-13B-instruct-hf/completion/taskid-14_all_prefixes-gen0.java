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

        // We'll need a dynamic list to keep track of our prefixes.
        // The list will initially contain only the empty string.
        ArrayList<String> prefixes = new ArrayList<String>();
        prefixes.add("");
        // We'll use this for-loop to iterate over all characters in the string.
        for (int i = 0; i < string.length(); i++) {
            // Get the prefix at the current index.
            String prefix = prefixes.get(prefixes.size() - 1);
            // Add the character at the current index to the prefix.
            prefix += string.charAt(i);
            // Add the prefix to our list.
            prefixes.add(prefix);
        }
        return prefixes;
    }
    public static void main(String[] args) {
    assert(allPrefixes(("")).equals((new ArrayList<String>(Arrays.asList()))));
    assert(allPrefixes(("asdfgh")).equals((new ArrayList<String>(Arrays.asList((String)"a", (String)"as", (String)"asd", (String)"asdf", (String)"asdfg", (String)"asdfgh")))));
    assert(allPrefixes(("WWW")).equals((new ArrayList<String>(Arrays.asList((String)"W", (String)"WW", (String)"WWW")))));
    }

}
