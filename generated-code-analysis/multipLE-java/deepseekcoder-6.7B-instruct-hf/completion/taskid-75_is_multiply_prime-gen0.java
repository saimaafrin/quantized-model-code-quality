import java.util.*;
import java.lang.reflect.*;
import org.javatuples.*;
import java.security.*;
import java.math.*;
import java.io.*;
import java.util.stream.*;
class Problem {
    // Write a function that returns true if the given number is the multiplication of 3 prime numbers
    // and false otherwise.
    // Knowing that (a) is less then 100. 
    // Example:
    // >>> isMultiplyPrime((30l))
    // (true)
    // 30 = 2 * 3 * 5
    public static boolean isMultiplyPrime(long a) {

        if (a <= 1) {
            return false;
        }
        long prime1 = 2, prime2 = 3, prime3 = 5;
        long prime4 = 7, prime5 = 11, prime6 = 13;
        long prime7 = 17, prime8 = 19, prime9 = 23;
        long prime10 = 29, prime11 = 31, prime12 = 37;
        long prime13 = 41, prime14 = 43, prime15 = 47;
        long prime16 = 53, prime17 = 59, prime18 = 61;
        long prime19 = 67, prime20 = 71, prime21 = 73;
        long prime22 = 79, prime23 = 83, prime24 = 89;
        long prime25 = 97;
        if (a % prime1 == 0 && a % prime2 == 0 && a % prime3 == 0) {
            return true;
        }
        if (a % prime4 == 0 && a % prime5 == 0 && a % prime6 == 0) {
            return true;
        }
        if (a % prime7 == 0 && a % prime8 == 0 && a % prime9 == 0) {
            return true;
        }
        if (a % prime10 == 0 && a % prime11 == 0 && a % prime12 == 0) {
            return true;
        }
        if (a % prime13 == 0 && a % prime14 == 0 && a % prime15 == 0) {
            return true;
        }
        if (a % prime16 == 0 && a % prime17 == 0 && a % prime18 == 0) {
            return true;
        }
        if (a % prime19 == 0 && a % prime20 == 0 && a % prime21 == 0) {
            return true;
        }
        if (a % prime22 == 0 && a % prime23 == 0 && a % prime24 == 0) {
            return true;
        }
        if (a % prime25 == 0) {
            return true;
        }
        return false;
    }
    public static void main(String[] args) {
    assert(isMultiplyPrime((5l)) == (false));
    assert(isMultiplyPrime((30l)) == (true));
    assert(isMultiplyPrime((8l)) == (true));
    assert(isMultiplyPrime((10l)) == (false));
    assert(isMultiplyPrime((125l)) == (true));
    assert(isMultiplyPrime((105l)) == (true));
    assert(isMultiplyPrime((126l)) == (false));
    assert(isMultiplyPrime((729l)) == (false));
    assert(isMultiplyPrime((891l)) == (false));
    assert(isMultiplyPrime((1001l)) == (true));
    }

}
