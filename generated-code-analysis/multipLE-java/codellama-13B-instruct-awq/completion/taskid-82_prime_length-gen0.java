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
        if(length == 0) return false;
        else if(length == 1) return true;
        else if(length == 2) return true;
        else if(length == 3) return true;
        else if(length == 5) return true;
        else if(length == 7) return true;
        else if(length == 11) return true;
        else if(length == 13) return true;
        else if(length == 17) return true;
        else if(length == 19) return true;
        else if(length == 23) return true;
        else if(length == 29) return true;
        else if(length == 31) return true;
        else if(length == 37) return true;
        else if(length == 41) return true;
        else if(length == 43) return true;
        else if(length == 47) return true;
        else if(length == 53) return true;
        else if(length == 59) return true;
        else if(length == 61) return true;
        else if(length == 67) return true;
        else if(length == 71) return true;
        else if(length == 73) return true;
        else if(length == 79) return true;
        else if(length == 83) return true;
        else if(length == 89) return true;
        else if(length == 97) return true;
        else return false;
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
