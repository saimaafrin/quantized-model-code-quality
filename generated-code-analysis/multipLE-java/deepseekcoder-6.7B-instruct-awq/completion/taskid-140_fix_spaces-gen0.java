import java.util.*;
import java.lang.reflect.*;
import org.javatuples.*;
import java.security.*;
import java.math.*;
import java.io.*;
import java.util.stream.*;
class Problem {
    // Given a string text, replace all spaces in it with underscores, 
    // and if a string has more than 2 consecutive spaces, 
    // then replace all consecutive spaces with - 
    // >>> fixSpaces((" Example"))
    // ("Example")
    // >>> fixSpaces((" Example 1"))
    // ("Example_1")
    // >>> fixSpaces((" Example 2"))
    // ("_Example_2")
    // >>> fixSpaces((" Example 3"))
    // ("_Example-3")
    public static String fixSpaces(String text) {

        // your code goes here
        StringBuilder sb = new StringBuilder();
        boolean lastWasSpace = false;
        boolean lastWasDoubleSpace = false;
        
        for (char c : text.toCharArray()) {
            if (c == ' ') {
                if (lastWasSpace) {
                    lastWasDoubleSpace = true;
                } else {
                    lastWasSpace = true;
                    sb.append('_');
                }
            } else {
                if (lastWasDoubleSpace) {
                    sb.append('-');
                    lastWasDoubleSpace = false;
                }
                sb.append(c);
                lastWasSpace = false;
            }
        }
        
        return sb.toString();
    }
    public static void main(String[] args) {
    assert(fixSpaces(("Example")).equals(("Example")));
    assert(fixSpaces(("Mudasir Hanif ")).equals(("Mudasir_Hanif_")));
    assert(fixSpaces(("Yellow Yellow  Dirty  Fellow")).equals(("Yellow_Yellow__Dirty__Fellow")));
    assert(fixSpaces(("Exa   mple")).equals(("Exa-mple")));
    assert(fixSpaces(("   Exa 1 2 2 mple")).equals(("-Exa_1_2_2_mple")));
    }

}
