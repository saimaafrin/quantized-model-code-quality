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

        return isPrime(string.length());
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
