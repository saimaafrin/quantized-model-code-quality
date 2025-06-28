import java.util.*;
import java.lang.reflect.*;
import org.javatuples.*;
import java.security.*;
import java.math.*;
import java.io.*;
import java.util.stream.*;
class Problem {
    // Filter an input array list of strings only for ones that start with a given prefix.
    // >>> filterByPrefix((new ArrayList<String>(Arrays.asList())), ("a"))
    // (new ArrayList<String>(Arrays.asList()))
    // >>> filterByPrefix((new ArrayList<String>(Arrays.asList((String)"abc", (String)"bcd", (String)"cde", (String)"array"))), ("a"))
    // (new ArrayList<String>(Arrays.asList((String)"abc", (String)"array")))
    public static ArrayList<String> filterByPrefix(ArrayList<String> strings, String prefix) {

        return new ArrayList<String>(strings.stream().filter(s -> s.startsWith(prefix)).collect(Collectors.toList()));
    }
    public static void main(String[] args) {
    assert(filterByPrefix((new ArrayList<String>(Arrays.asList())), ("john")).equals((new ArrayList<String>(Arrays.asList()))));
    assert(filterByPrefix((new ArrayList<String>(Arrays.asList((String)"xxx", (String)"asd", (String)"xxy", (String)"john doe", (String)"xxxAAA", (String)"xxx"))), ("xxx")).equals((new ArrayList<String>(Arrays.asList((String)"xxx", (String)"xxxAAA", (String)"xxx")))));
    }

}
