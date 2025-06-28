import java.util.*;
import java.lang.reflect.*;
import org.javatuples.*;
import java.security.*;
import java.math.*;
import java.io.*;
import java.util.stream.*;
class Problem {
    // Concatenate array list of strings into a single string
    // >>> concatenate((new ArrayList<String>(Arrays.asList())))
    // ("")
    // >>> concatenate((new ArrayList<String>(Arrays.asList((String)"a", (String)"b", (String)"c"))))
    // ("abc")
    public static String concatenate(ArrayList<String> strings) {

        return String.join("", strings);
    }
    public static void main(String[] args) {
    assert(concatenate((new ArrayList<String>(Arrays.asList()))).equals(("")));
    assert(concatenate((new ArrayList<String>(Arrays.asList((String)"x", (String)"y", (String)"z")))).equals(("xyz")));
    assert(concatenate((new ArrayList<String>(Arrays.asList((String)"x", (String)"y", (String)"z", (String)"w", (String)"k")))).equals(("xyzwk")));
    }

}
