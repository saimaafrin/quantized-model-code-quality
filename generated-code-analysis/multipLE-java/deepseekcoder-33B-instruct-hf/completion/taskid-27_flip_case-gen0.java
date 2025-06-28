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

        StringBuilder newString = new StringBuilder();
        for (char ch: string.toCharArray()){
            if (Character.isUpperCase(ch)){
                newString.append(Character.toLowerCase(ch));
            }
            else if (Character.isLowerCase(ch)){
                newString.append(Character.toUpperCase(ch));
            }
            else {
                newString.append(ch);
            }
        }
        return newString.toString();
    }
    public static void main(String[] args) {
    assert(flipCase(("")).equals(("")));
    assert(flipCase(("Hello!")).equals(("hELLO!")));
    assert(flipCase(("These violent delights have violent ends")).equals(("tHESE VIOLENT DELIGHTS HAVE VIOLENT ENDS")));
    }

}
