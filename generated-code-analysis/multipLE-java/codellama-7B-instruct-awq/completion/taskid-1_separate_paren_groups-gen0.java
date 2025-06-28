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

        var groups = new ArrayList<String>();
        var stack = new ArrayList<Character>();
        var group = new StringBuilder();
        var j = 0;
        var k = 0;
        for (var i = 0; i < paren_string.length(); i++) {
            var c = paren_string.charAt(i);
            if (c == '(') {
                stack.add(c);
                group.append(c);
            }
            else if (c == ')') {
                stack.remove(stack.size() - 1);
                if (stack.size() == 0) {
                    groups.add(group.toString());
                    group = new StringBuilder();
                }
                else {
                    group.append(c);
                }
            }
            else if (stack.size() == 0) {
                groups.add(String.valueOf(c));
                j++;
            }
            else {
                group.append(c);
                k++;
            }
        }
        if (group.length() != 0) {
            groups.add(group.toString());
        }
        System.out.println(groups);
        System.out.println(j + " " + k);
        return groups;
    }
    public static void main(String[] args) {
    assert(separateParenGroups(("(()()) ((())) () ((())()())")).equals((new ArrayList<String>(Arrays.asList((String)"(()())", (String)"((()))", (String)"()", (String)"((())()())")))));
    assert(separateParenGroups(("() (()) ((())) (((())))")).equals((new ArrayList<String>(Arrays.asList((String)"()", (String)"(())", (String)"((()))", (String)"(((())))")))));
    assert(separateParenGroups(("(()(())((())))")).equals((new ArrayList<String>(Arrays.asList((String)"(()(())((())))")))));
    assert(separateParenGroups(("( ) (( )) (( )( ))")).equals((new ArrayList<String>(Arrays.asList((String)"()", (String)"(())", (String)"(()())")))));
    }

}
