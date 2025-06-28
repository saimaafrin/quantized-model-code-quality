import java.util.*;
import java.lang.reflect.*;
import org.javatuples.*;
import java.security.*;
import java.math.*;
import java.io.*;
import java.util.stream.*;
class Problem {
    // You have been tasked to write a function that receives 
    // a hexadecimal number as a string and counts the number of hexadecimal 
    // digits that are primes (prime number, or a prime, is a natural number 
    // greater than 1 that is not a product of two smaller natural numbers).
    // Hexadecimal digits are 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E, F.
    // Prime numbers are 2, 3, 5, 7, 11, 13, 17,...
    // So you have to determine a number of the following digits: 2, 3, 5, 7, 
    // B (=decimal 11), D (=decimal 13).
    // Note: you may assume the input is always correct or empty string, 
    // and symbols A,B,C,D,E,F are always uppercase.
    // Examples:
    // >>> hexKey(("AB"))
    // (1l)
    // >>> hexKey(("1077E"))
    // (2l)
    // >>> hexKey(("ABED1A33"))
    // (4l)
    // >>> hexKey(("123456789ABCDEF0"))
    // (6l)
    // >>> hexKey(("2020"))
    // (2l)
    public static long hexKey(String num) {

        String[] hex = {"A","B","C","D","E","F"};
        String[] hexPrimes = {"11","13"};
        String[] hexDigits = {"0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"};
        ArrayList<Integer> primes = new ArrayList<Integer>();
        ArrayList<Integer> digits = new ArrayList<Integer>();
        // find all prime numbers
        for (int i = 2; i < 1000; i++){
            int isPrime = 1;
            for (int j = 2; j < i; j++){
                if(i % j == 0){
                    isPrime = 0;
                }
            }
            if(isPrime == 1){
                primes.add(i);
            }
        }
        // find all digits from input string
        for (int i = 0; i < hexDigits.length; i++){
            for (int j = 0; j < num.length(); j++){
                if(hexDigits[i].equals(num.substring(j,j+1))){
                    digits.add(i);
                }
            }
        }
        long result = 0;
        // count the number of prime digits
        for (int i = 0; i < digits.size(); i++){
            for (int j = 0; j < primes.size(); j++){
                if(digits.get(i) == primes.get(j)){
                    result++;
                }
            }
            for (int j = 0; j < hexPrimes.length; j++){
                if(digits.get(i) == hexPrimes[j]){
                    result++;
                }
            }
        }
        return result;
    }
    public static void main(String[] args) {
    assert(hexKey(("AB")) == (1l));
    assert(hexKey(("1077E")) == (2l));
    assert(hexKey(("ABED1A33")) == (4l));
    assert(hexKey(("2020")) == (2l));
    assert(hexKey(("123456789ABCDEF0")) == (6l));
    assert(hexKey(("112233445566778899AABBCCDDEEFF00")) == (12l));
    }

}
