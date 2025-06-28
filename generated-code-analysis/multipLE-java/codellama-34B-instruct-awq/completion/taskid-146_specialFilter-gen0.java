import java.util.*;
import java.lang.reflect.*;
import org.javatuples.*;
import java.security.*;
import java.math.*;
import java.io.*;
import java.util.stream.*;
class Problem {
    // Write a function that takes an array array list of numbers as input and returns 
    // the number of elements in the array array list that are greater than 10 and both 
    // first and last digits of a number are odd (1, 3, 5, 7, 9).
    // For example:
    // >>> specialFilter((new ArrayList<Long>(Arrays.asList((long)15l, (long)-73l, (long)14l, (long)-15l))))
    // (1l)
    // >>> specialFilter((new ArrayList<Long>(Arrays.asList((long)33l, (long)-2l, (long)-3l, (long)45l, (long)21l, (long)109l))))
    // (2l)
    public static long specialFilter(ArrayList<Long> nums) {

        return nums.stream()
                   .filter(e -> {
                            if(e >= 10) {
                                BigInteger b = new BigInteger(e + "");
                                String a = b.toString().substring(0, 1);
                                String c = b.toString().substring(b.toString().length() - 1, b.toString().length());
                                BigInteger ab = new BigInteger(a);
                                BigInteger cb = new BigInteger(c);
                                if(ab.mod(new BigInteger("2")) == new BigInteger("1") && cb.mod(new BigInteger("2")) == new BigInteger("1")) {
                                    return true;
                                }
                            }
                            return false;
                        }).count();
    }
    public static void main(String[] args) {
    assert(specialFilter((new ArrayList<Long>(Arrays.asList((long)5l, (long)-2l, (long)1l, (long)-5l)))) == (0l));
    assert(specialFilter((new ArrayList<Long>(Arrays.asList((long)15l, (long)-73l, (long)14l, (long)-15l)))) == (1l));
    assert(specialFilter((new ArrayList<Long>(Arrays.asList((long)33l, (long)-2l, (long)-3l, (long)45l, (long)21l, (long)109l)))) == (2l));
    assert(specialFilter((new ArrayList<Long>(Arrays.asList((long)43l, (long)-12l, (long)93l, (long)125l, (long)121l, (long)109l)))) == (4l));
    assert(specialFilter((new ArrayList<Long>(Arrays.asList((long)71l, (long)-2l, (long)-33l, (long)75l, (long)21l, (long)19l)))) == (3l));
    assert(specialFilter((new ArrayList<Long>(Arrays.asList((long)1l)))) == (0l));
    assert(specialFilter((new ArrayList<Long>(Arrays.asList()))) == (0l));
    }

}
