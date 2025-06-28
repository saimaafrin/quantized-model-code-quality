import java.util.*;
import java.lang.reflect.*;
import org.javatuples.*;
import java.security.*;
import java.math.*;
import java.io.*;
import java.util.stream.*;
class Problem {
    // Return array list with elements incremented by 1.
    // >>> incrList((new ArrayList<Long>(Arrays.asList((long)1l, (long)2l, (long)3l))))
    // (new ArrayList<Long>(Arrays.asList((long)2l, (long)3l, (long)4l)))
    // >>> incrList((new ArrayList<Long>(Arrays.asList((long)5l, (long)3l, (long)5l, (long)2l, (long)3l, (long)3l, (long)9l, (long)0l, (long)123l))))
    // (new ArrayList<Long>(Arrays.asList((long)6l, (long)4l, (long)6l, (long)3l, (long)4l, (long)4l, (long)10l, (long)1l, (long)124l)))
    public static ArrayList<Long> incrList(ArrayList<Long> l) {

        for (int i = 0; i < l.size(); i++) {
            l.set(i, l.get(i) + 1);
        }
        return l;
    }
    public static void main(String[] args) {
    assert(incrList((new ArrayList<Long>(Arrays.asList()))).equals((new ArrayList<Long>(Arrays.asList()))));
    assert(incrList((new ArrayList<Long>(Arrays.asList((long)3l, (long)2l, (long)1l)))).equals((new ArrayList<Long>(Arrays.asList((long)4l, (long)3l, (long)2l)))));
    assert(incrList((new ArrayList<Long>(Arrays.asList((long)5l, (long)2l, (long)5l, (long)2l, (long)3l, (long)3l, (long)9l, (long)0l, (long)123l)))).equals((new ArrayList<Long>(Arrays.asList((long)6l, (long)3l, (long)6l, (long)3l, (long)4l, (long)4l, (long)10l, (long)1l, (long)124l)))));
    }

}
