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

        StringBuilder sb = new StringBuilder();
        int num = (int) number;

        while(num > 0) {
            if(num >= 100) {
                sb.append("c");
                num -= 100;
            }
            else if(num >= 90) {
                sb.append("xc");
                num -= 90;
            }
            else if(num >= 50) {
                sb.append("l");
                num -= 50;
            }
            else if(num >= 40) {
                sb.append("xl");
                num -= 40;
            }
            else if(num >= 10) {
                sb.append("x".repeat((int) num / 10));
                num %= 10;
            }
            else if(num == 9) {
                sb.append("ix");
                num -= 9;
            }
            else if(num >= 5) {
                sb.append("v");
                num -= 5;
            }
            else if(num == 4) {
                sb.append("iv");
                num -= 4;
            }
            else if(num >= 1) {
                sb.append("i".repeat(num));
                num = 0;
            }
        }

        return sb.toString();
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
