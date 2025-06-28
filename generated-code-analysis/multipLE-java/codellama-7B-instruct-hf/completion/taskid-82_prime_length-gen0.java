import java.util.*;
import java.lang.reflect.*;
import org.javatuples.*;
import java.security.*;
import java.math.*;
import java.io.*;
import java.util.stream.*;
class Problem {
    // Write a function that takes a string and returns true if the string
    // length is a prime number or false otherwise
    // Examples
    // >>> primeLength(("Hello"))
    // (true)
    // >>> primeLength(("abcdcba"))
    // (true)
    // >>> primeLength(("kittens"))
    // (true)
    // >>> primeLength(("orange"))
    // (false)
    public static boolean primeLength(String string) {

        int length = string.length();
        return length == 0 || (length > 1 && length % 2 != 0 && length % 3 != 0 && length % 5 != 0 && length % 7 != 0 && length % 11 != 0 && length % 13 != 0 && length % 17 != 0 && length % 19 != 0 && length % 23 != 0 && length % 29 != 0 && length % 31 != 0 && length % 37 != 0 && length % 41 != 0 && length % 43 != 0 && length % 47 != 0 && length % 53 != 0 && length % 59 != 0 && length % 61 != 0 && length % 67 != 0 && length % 71 != 0 && length % 73 != 0 && length % 79 != 0 && length % 83 != 0 && length % 89 != 0 && length % 97 != 0 && length % 101 != 0);
    }
    public static void main(String[] args) {
    assert(primeLength(("Hello")) == (true));
    assert(primeLength(("abcdcba")) == (true));
    assert(primeLength(("kittens")) == (true));
    assert(primeLength(("orange")) == (false));
    assert(primeLength(("wow")) == (true));
    assert(primeLength(("world")) == (true));
    assert(primeLength(("MadaM")) == (true));
    assert(primeLength(("Wow")) == (true));
    assert(primeLength(("")) == (false));
    assert(primeLength(("HI")) == (true));
    assert(primeLength(("go")) == (true));
    assert(primeLength(("gogo")) == (false));
    assert(primeLength(("aaaaaaaaaaaaaaa")) == (false));
    assert(primeLength(("Madam")) == (true));
    assert(primeLength(("M")) == (false));
    assert(primeLength(("0")) == (false));
    }

}
