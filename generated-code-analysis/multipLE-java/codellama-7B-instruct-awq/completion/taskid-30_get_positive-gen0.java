import java.util.*;
import java.lang.reflect.*;
import org.javatuples.*;
import java.security.*;
import java.math.*;
import java.io.*;
import java.util.stream.*;
class Problem {
    // Return only positive numbers in the array list.
    // >>> getPositive((new ArrayList<Long>(Arrays.asList((long)-1l, (long)2l, (long)-4l, (long)5l, (long)6l))))
    // (new ArrayList<Long>(Arrays.asList((long)2l, (long)5l, (long)6l)))
    // >>> getPositive((new ArrayList<Long>(Arrays.asList((long)5l, (long)3l, (long)-5l, (long)2l, (long)-3l, (long)3l, (long)9l, (long)0l, (long)123l, (long)1l, (long)-10l))))
    // (new ArrayList<Long>(Arrays.asList((long)5l, (long)3l, (long)2l, (long)3l, (long)9l, (long)123l, (long)1l)))
    public static ArrayList<Long> getPositive(ArrayList<Long> l) {

        ArrayList<Long> result = new ArrayList<Long>();
        for (Long i : l) {
            if (i > 0) {
                result.add(i);
            }
        }
        return result;
    }
    public static void main(String[] args) {
    assert(getPositive((new ArrayList<Long>(Arrays.asList((long)-1l, (long)-2l, (long)4l, (long)5l, (long)6l)))).equals((new ArrayList<Long>(Arrays.asList((long)4l, (long)5l, (long)6l)))));
    assert(getPositive((new ArrayList<Long>(Arrays.asList((long)5l, (long)3l, (long)-5l, (long)2l, (long)3l, (long)3l, (long)9l, (long)0l, (long)123l, (long)1l, (long)-10l)))).equals((new ArrayList<Long>(Arrays.asList((long)5l, (long)3l, (long)2l, (long)3l, (long)3l, (long)9l, (long)123l, (long)1l)))));
    assert(getPositive((new ArrayList<Long>(Arrays.asList((long)-1l, (long)-2l)))).equals((new ArrayList<Long>(Arrays.asList()))));
    assert(getPositive((new ArrayList<Long>(Arrays.asList()))).equals((new ArrayList<Long>(Arrays.asList()))));
    }

}
