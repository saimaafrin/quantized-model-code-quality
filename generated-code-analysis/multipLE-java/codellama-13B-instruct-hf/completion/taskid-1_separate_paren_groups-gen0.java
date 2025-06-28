import java.util.*;
import java.lang.reflect.*;
import org.javatuples.*;
import java.security.*;
import java.math.*;
import java.io.*;
import java.util.stream.*;
class Problem {
    // Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    // separate those group into separate strings and return the array list of those.
    // Separate groups are balanced (each open brace is properly closed) and not nested within each other
    // Ignore any spaces in the input string.
    // >>> separateParenGroups(("( ) (( )) (( )( ))"))
    // (new ArrayList<String>(Arrays.asList((String)"()", (String)"(())", (String)"(()())")))
    public static ArrayList<String> separateParenGroups(String paren_string) {

        char[] chars = paren_string.toCharArray();
        char[] paren = {'(',')','{','}'};
        ArrayList<String> output = new ArrayList<>();
        ArrayList<String> buffer = new ArrayList<>();
        int stack = 0;
        String temp = "";
        boolean flag = false;
        for (int i = 0; i < chars.length; i++) {
            if (chars[i] == ' ' || (stack == 0 && chars[i] == ' ' && flag == true)) {
                if (!temp.isEmpty()) {
                    buffer.add(temp);
                    temp = "";
                }
                flag = false;
                continue;
            }
            if (isParen(chars[i], paren)) {
                if (stack == 0) {
                    temp += chars[i];
                    stack++;
                    flag = true;
                    continue;
                }
                if (stack != 0) {
                    temp += chars[i];
                    if (stack > 0) {
                        stack--;
                        if (stack == 0) {
                            flag = true;
                            buffer.add(temp);
                            temp = "";
                        }
                    }
                    continue;
                }
            } else {
                temp += chars[i];
            }
        }
        if (!temp.isEmpty()) {
            buffer.add(temp);
            temp = "";
        }
        return buffer;
    }
    public static void main(String[] args) {
    assert(separateParenGroups(("(()()) ((())) () ((())()())")).equals((new ArrayList<String>(Arrays.asList((String)"(()())", (String)"((()))", (String)"()", (String)"((())()())")))));
    assert(separateParenGroups(("() (()) ((())) (((())))")).equals((new ArrayList<String>(Arrays.asList((String)"()", (String)"(())", (String)"((()))", (String)"(((())))")))));
    assert(separateParenGroups(("(()(())((())))")).equals((new ArrayList<String>(Arrays.asList((String)"(()(())((())))")))));
    assert(separateParenGroups(("( ) (( )) (( )( ))")).equals((new ArrayList<String>(Arrays.asList((String)"()", (String)"(())", (String)"(()())")))));
    }

}
