import java.util.*;
import java.lang.reflect.*;
import org.javatuples.*;
import java.security.*;
import java.math.*;
import java.io.*;
import java.util.stream.*;
class Problem {
    // Given a positive integer, obtain its roman numeral equivalent as a string,
    // and return it in lowercase.
    // Restrictions: 1 <= num <= 1000
    // Examples:
    // >>> intToMiniRoman((19l))
    // ("xix")
    // >>> intToMiniRoman((152l))
    // ("clii")
    // >>> intToMiniRoman((426l))
    // ("cdxxvi")
    public static String intToMiniRoman(long number) {

        // Create list of integers and corresponding Roman numerals
        Map<Integer, String> numerals = new LinkedHashMap<>();
        numerals.put(1000, "m");
        numerals.put(900, "cm");
        numerals.put(500, "d");
        numerals.put(400, "cd");
        numerals.put(100, "c");
        numerals.put(90, "xc");
        numerals.put(50, "l");
        numerals.put(40, "xl");
        numerals.put(10, "x");
        numerals.put(9, "ix");
        numerals.put(5, "v");
        numerals.put(4, "iv");
        numerals.put(1, "i");

        // Convert input number to string and reverse it
        String numStr = Long.toString(number);
        String reverseNumStr = new StringBuilder(numStr).reverse().toString();

        // Create list to hold converted numerals
        List<String> romanNumerals = new ArrayList<>();

        // Iterate through reversed string of input number
        for(int i = 0; i < reverseNumStr.length(); i++) {
            // Convert individual string digits to int and multiply by 10 for each
            // place value in input number
            int digit = Integer.parseInt(String.valueOf(reverseNumStr.charAt(i))) * (int) Math.pow(10, i);

            // Iterate through numerals map to match and convert
            for(int numeral : numerals.keySet()) {
                if(digit == numeral) {
                    romanNumerals.add(numerals.get(digit));
                }
            }
        }
        // Reverse list to match order of input number
        Collections.reverse(romanNumerals);

        // Join list of converted numerals into one string and return
        StringBuilder finalRomanNumeral = new StringBuilder();
        for(String n : romanNumerals) {
            finalRomanNumeral.append(n);
        }
        return finalRomanNumeral.toString();
    }
    public static void main(String[] args) {
    assert(intToMiniRoman((19l)).equals(("xix")));
    assert(intToMiniRoman((152l)).equals(("clii")));
    assert(intToMiniRoman((251l)).equals(("ccli")));
    assert(intToMiniRoman((426l)).equals(("cdxxvi")));
    assert(intToMiniRoman((500l)).equals(("d")));
    assert(intToMiniRoman((1l)).equals(("i")));
    assert(intToMiniRoman((4l)).equals(("iv")));
    assert(intToMiniRoman((43l)).equals(("xliii")));
    assert(intToMiniRoman((90l)).equals(("xc")));
    assert(intToMiniRoman((94l)).equals(("xciv")));
    assert(intToMiniRoman((532l)).equals(("dxxxii")));
    assert(intToMiniRoman((900l)).equals(("cm")));
    assert(intToMiniRoman((994l)).equals(("cmxciv")));
    assert(intToMiniRoman((1000l)).equals(("m")));
    }

}
