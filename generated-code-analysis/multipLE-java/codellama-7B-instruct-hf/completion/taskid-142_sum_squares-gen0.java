import java.util.*;
import java.lang.reflect.*;
import org.javatuples.*;
import java.security.*;
import java.math.*;
import java.io.*;
import java.util.stream.*;
class Problem {
    // "
    // This function will take an array array list of integers. For all entries in the array list, the function shall square the integer entry if its index is a 
    // multiple of 3 and will cube the integer entry if its index is a multiple of 4 and not a multiple of 3. The function will not 
    // change the entries in the array list whose indexes are not a multiple of 3 or 4. The function shall then return the sum of all entries. 
    // Examples:
    // >>> lst
    // (long)new ArrayList<Long>(Arrays.asList((long)1l, (long)2l, (long)3l))
    // >>> lst
    // (long)new ArrayList<Long>(Arrays.asList())
    // >>> lst
    // (long)new ArrayList<Long>(Arrays.asList((long)-1l, (long)-5l, (long)2l, (long)-1l, (long)-5l))
    public static long sumSquares(ArrayList<Long> lst) {

        long sum = 0;
        long x = 0;
        for (int i = 0; i < lst.size(); i++){
            x = lst.get(i);
            if (i % 3 == 0){
                x = x * x;
            }
            if (i % 4 == 0 && i % 3 != 0){
                x = x * x * x;
            }
            sum = sum + x;
        }
        return sum;
    }
    public static void main(String[] args) {
    assert(sumSquares((new ArrayList<Long>(Arrays.asList((long)1l, (long)2l, (long)3l)))) == (6l));
    assert(sumSquares((new ArrayList<Long>(Arrays.asList((long)1l, (long)4l, (long)9l)))) == (14l));
    assert(sumSquares((new ArrayList<Long>(Arrays.asList()))) == (0l));
    assert(sumSquares((new ArrayList<Long>(Arrays.asList((long)1l, (long)1l, (long)1l, (long)1l, (long)1l, (long)1l, (long)1l, (long)1l, (long)1l)))) == (9l));
    assert(sumSquares((new ArrayList<Long>(Arrays.asList((long)-1l, (long)-1l, (long)-1l, (long)-1l, (long)-1l, (long)-1l, (long)-1l, (long)-1l, (long)-1l)))) == (-3l));
    assert(sumSquares((new ArrayList<Long>(Arrays.asList((long)0l)))) == (0l));
    assert(sumSquares((new ArrayList<Long>(Arrays.asList((long)-1l, (long)-5l, (long)2l, (long)-1l, (long)-5l)))) == (-126l));
    assert(sumSquares((new ArrayList<Long>(Arrays.asList((long)-56l, (long)-99l, (long)1l, (long)0l, (long)-2l)))) == (3030l));
    assert(sumSquares((new ArrayList<Long>(Arrays.asList((long)-1l, (long)0l, (long)0l, (long)0l, (long)0l, (long)0l, (long)0l, (long)0l, (long)-1l)))) == (0l));
    assert(sumSquares((new ArrayList<Long>(Arrays.asList((long)-16l, (long)-9l, (long)-2l, (long)36l, (long)36l, (long)26l, (long)-20l, (long)25l, (long)-40l, (long)20l, (long)-4l, (long)12l, (long)-26l, (long)35l, (long)37l)))) == (-14196l));
    assert(sumSquares((new ArrayList<Long>(Arrays.asList((long)-1l, (long)-3l, (long)17l, (long)-1l, (long)-15l, (long)13l, (long)-1l, (long)14l, (long)-14l, (long)-12l, (long)-5l, (long)14l, (long)-14l, (long)6l, (long)13l, (long)11l, (long)16l, (long)16l, (long)4l, (long)10l)))) == (-1448l));
    }

}
