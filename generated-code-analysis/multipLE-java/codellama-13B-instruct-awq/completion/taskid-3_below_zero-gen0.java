import java.util.*;
import java.lang.reflect.*;
import org.javatuples.*;
import java.security.*;
import java.math.*;
import java.io.*;
import java.util.stream.*;
class Problem {
    // You're given an array array list of deposit and withdrawal operations on a bank account that starts with
    // zero balance. Your task is to detect if at any point the balance of account fallls below zero, and
    // at that point function should return true. Otherwise it should return false.
    // >>> belowZero((new ArrayList<Long>(Arrays.asList((long)1l, (long)2l, (long)3l))))
    // (false)
    // >>> belowZero((new ArrayList<Long>(Arrays.asList((long)1l, (long)2l, (long)-4l, (long)5l))))
    // (true)
    public static boolean belowZero(ArrayList<Long> operations) {

        int i;
        long currentBalance = 0;
        boolean isBelowZero = false;
        for (i = 0; i < operations.size(); i++) {
            currentBalance += operations.get(i);
            if (currentBalance < 0) {
                isBelowZero = true;
                break;
            }
        }
        return isBelowZero;
    }
    public static void main(String[] args) {
    assert(belowZero((new ArrayList<Long>(Arrays.asList()))) == (false));
    assert(belowZero((new ArrayList<Long>(Arrays.asList((long)1l, (long)2l, (long)-3l, (long)1l, (long)2l, (long)-3l)))) == (false));
    assert(belowZero((new ArrayList<Long>(Arrays.asList((long)1l, (long)2l, (long)-4l, (long)5l, (long)6l)))) == (true));
    assert(belowZero((new ArrayList<Long>(Arrays.asList((long)1l, (long)-1l, (long)2l, (long)-2l, (long)5l, (long)-5l, (long)4l, (long)-4l)))) == (false));
    assert(belowZero((new ArrayList<Long>(Arrays.asList((long)1l, (long)-1l, (long)2l, (long)-2l, (long)5l, (long)-5l, (long)4l, (long)-5l)))) == (true));
    assert(belowZero((new ArrayList<Long>(Arrays.asList((long)1l, (long)-2l, (long)2l, (long)-2l, (long)5l, (long)-5l, (long)4l, (long)-4l)))) == (true));
    }

}
