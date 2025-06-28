import java.util.*;
import java.lang.reflect.*;
import org.javatuples.*;
import java.security.*;
import java.math.*;
import java.io.*;
import java.util.stream.*;
class Problem {
    // This function takes an array array list l and returns an array array list l' such that
    // l' is identical to l in the odd indicies, while its values at the even indicies are equal
    // to the values of the even indicies of l, but sorted.
    // >>> sortEven((new ArrayList<Long>(Arrays.asList((long)1l, (long)2l, (long)3l))))
    // (new ArrayList<Long>(Arrays.asList((long)1l, (long)2l, (long)3l)))
    // >>> sortEven((new ArrayList<Long>(Arrays.asList((long)5l, (long)6l, (long)3l, (long)4l))))
    // (new ArrayList<Long>(Arrays.asList((long)3l, (long)6l, (long)5l, (long)4l)))
    public static ArrayList<Long> sortEven(ArrayList<Long> l) {

        // We make a copy of the input list to avoid modifying it.
        ArrayList<Long> copy = new ArrayList<Long>(l);
        // We create a list of tuples (i, e), where e is the i-th element of the copy.
        ArrayList<Pair<Long, Long>> tuples = new ArrayList<Pair<Long, Long>>();
        for (int i = 0; i < copy.size(); i++) {
            tuples.add(new Pair<Long, Long>((long)i, copy.get(i)));
        }
        // We filter out the tuples that represent even indicies.
        tuples = new ArrayList<Pair<Long, Long>>(tuples.stream().filter(p -> p.getValue0() % 2 == 0).collect(Collectors.toList()));
        // We sort the tuples based on their value.
        tuples.sort((p1, p2) -> p1.getValue1().compareTo(p2.getValue1()));
        // We replace the even indicies of the original list with the sorted values.
        for (int i = 0; i < tuples.size(); i++) {
            copy.set((int)(long)tuples.get(i).getValue0(), tuples.get(i).getValue1());
        }
        // We return the modified list.
        return copy;
    }
    public static void main(String[] args) {
    assert(sortEven((new ArrayList<Long>(Arrays.asList((long)1l, (long)2l, (long)3l)))).equals((new ArrayList<Long>(Arrays.asList((long)1l, (long)2l, (long)3l)))));
    assert(sortEven((new ArrayList<Long>(Arrays.asList((long)5l, (long)3l, (long)-5l, (long)2l, (long)-3l, (long)3l, (long)9l, (long)0l, (long)123l, (long)1l, (long)-10l)))).equals((new ArrayList<Long>(Arrays.asList((long)-10l, (long)3l, (long)-5l, (long)2l, (long)-3l, (long)3l, (long)5l, (long)0l, (long)9l, (long)1l, (long)123l)))));
    assert(sortEven((new ArrayList<Long>(Arrays.asList((long)5l, (long)8l, (long)-12l, (long)4l, (long)23l, (long)2l, (long)3l, (long)11l, (long)12l, (long)-10l)))).equals((new ArrayList<Long>(Arrays.asList((long)-12l, (long)8l, (long)3l, (long)4l, (long)5l, (long)2l, (long)12l, (long)11l, (long)23l, (long)-10l)))));
    }

}
