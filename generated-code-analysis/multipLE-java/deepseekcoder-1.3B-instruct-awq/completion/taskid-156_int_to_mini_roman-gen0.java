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

        // First, create a list of tuples with roman numerals and their corresponding values.
        List<Tuple2<String, Integer>> romanNumerals = Arrays.asList(
            Tuple2.of("m", 1000), Tuple2.of("cm", 900), Tuple2.of("d", 500), Tuple2.of("cd", 400),
            Tuple2.of("c", 100), Tuple2.of("xc", 90), Tuple2.of("l", 50), Tuple2.of("xl", 40),
            Tuple2.of("x", 10), Tuple2.of("ix", 9), Tuple2.of("v", 5), Tuple2.of("iv", 4),
            Tuple2.of("i", 1)
        );

        // Then, create a string to hold the final roman numeral.
        StringBuilder romanNumeral = new StringBuilder();

        // For each tuple in the list, subtract the value from the number until the number becomes less than the value.
        // Add the corresponding roman numeral to the result.
        for (Tuple2<String, Integer> tuple : romanNumerals) {
            while (number >= tuple._2) {
                number -= tuple._2;
                romanNumeral.append(tuple._1);
            }
        }

        // Return the final roman numeral.
        return romanNumeral.toString().toLowerCase();
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
