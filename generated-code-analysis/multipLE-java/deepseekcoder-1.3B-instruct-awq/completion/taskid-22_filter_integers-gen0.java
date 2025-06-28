import java.util.*;
import java.lang.reflect.*;
import org.javatuples.*;
import java.security.*;
import java.math.*;
import java.io.*;
import java.util.stream.*;
class Problem {
    // Filter given array list of any javathon values only for integers
    // >>> filterIntegers((new ArrayList<Object>(Arrays.asList((String)"a", (String)3.14f, (String)5l))))
    // (new ArrayList<Long>(Arrays.asList((long)5l)))
    // >>> filterIntegers((new ArrayList<Object>(Arrays.asList(1l, 2l, 3l, "abc", new HashMap<Long,Long>(Map.of()), new ArrayList<Long>(Arrays.asList())))))
    // (new ArrayList<Long>(Arrays.asList((long)1l, (long)2l, (long)3l)))
    public static ArrayList<Long> filterIntegers(ArrayList<Object> values) {

        ArrayList<Long> result = new ArrayList<>();
        for (Object value : values) {
            if (value instanceof Long) {
                result.add((Long) value);
            }
        }
        return result;
    }
    public static void main(String[] args) {
    assert(filterIntegers((new ArrayList<Object>(Arrays.asList()))).equals((new ArrayList<Long>(Arrays.asList()))));
    assert(filterIntegers((new ArrayList<Object>(Arrays.asList(4l, new HashMap<Long,Long>(Map.of()), new ArrayList<Long>(Arrays.asList()), 23.2f, 9l, "adasd")))).equals((new ArrayList<Long>(Arrays.asList((long)4l, (long)9l)))));
    assert(filterIntegers((new ArrayList<Object>(Arrays.asList(3l, "c", 3l, 3l, "a", "b")))).equals((new ArrayList<Long>(Arrays.asList((long)3l, (long)3l, (long)3l)))));
    }

}
