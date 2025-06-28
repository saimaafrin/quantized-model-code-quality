import java.util.*;
import java.lang.reflect.*;
import org.javatuples.*;
import java.security.*;
import java.math.*;
import java.io.*;
import java.util.stream.*;
class Problem {
    // Filter an input array list of strings only for ones that contain given substring
    // >>> filterBySubstring((new ArrayList<String>(Arrays.asList())), ("a"))
    // (new ArrayList<String>(Arrays.asList()))
    // >>> filterBySubstring((new ArrayList<String>(Arrays.asList((String)"abc", (String)"bacd", (String)"cde", (String)"array"))), ("a"))
    // (new ArrayList<String>(Arrays.asList((String)"abc", (String)"bacd", (String)"array")))
    public static ArrayList<String> filterBySubstring(ArrayList<String> strings, String substring) {

        return new ArrayList<String>(strings.stream().filter(s -> s.contains(substring)).collect(Collectors.toList()));
    }
    public static void main(String[] args) {
    assert(filterBySubstring((new ArrayList<String>(Arrays.asList())), ("john")).equals((new ArrayList<String>(Arrays.asList()))));
    assert(filterBySubstring((new ArrayList<String>(Arrays.asList((String)"xxx", (String)"asd", (String)"xxy", (String)"john doe", (String)"xxxAAA", (String)"xxx"))), ("xxx")).equals((new ArrayList<String>(Arrays.asList((String)"xxx", (String)"xxxAAA", (String)"xxx")))));
    assert(filterBySubstring((new ArrayList<String>(Arrays.asList((String)"xxx", (String)"asd", (String)"aaaxxy", (String)"john doe", (String)"xxxAAA", (String)"xxx"))), ("xx")).equals((new ArrayList<String>(Arrays.asList((String)"xxx", (String)"aaaxxy", (String)"xxxAAA", (String)"xxx")))));
    assert(filterBySubstring((new ArrayList<String>(Arrays.asList((String)"grunt", (String)"trumpet", (String)"prune", (String)"gruesome"))), ("run")).equals((new ArrayList<String>(Arrays.asList((String)"grunt", (String)"prune")))));
    }

}
