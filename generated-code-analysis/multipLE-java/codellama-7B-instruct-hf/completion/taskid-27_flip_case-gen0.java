import java.util.*;
import java.lang.reflect.*;
import org.javatuples.*;
import java.security.*;
import java.math.*;
import java.io.*;
import java.util.stream.*;
class Problem {
    // For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    // >>> flipCase(("Hello"))
    // ("hELLO")
    public static String flipCase(String string) {

        char[] flip = string.toCharArray();
        for(int i = 0; i < flip.length; i++) {
            if (flip[i] >= 'a' && flip[i] <= 'z') {
                flip[i] = (char) (flip[i] - 32);
            } else if (flip[i] >= 'A' && flip[i] <= 'Z') {
                flip[i] = (char) (flip[i] + 32);
            }
        }
        return String.valueOf(flip);
    }
    public static void main(String[] args) {
    assert(flipCase(("")).equals(("")));
    assert(flipCase(("Hello!")).equals(("hELLO!")));
    assert(flipCase(("These violent delights have violent ends")).equals(("tHESE VIOLENT DELIGHTS HAVE VIOLENT ENDS")));
    }

}
