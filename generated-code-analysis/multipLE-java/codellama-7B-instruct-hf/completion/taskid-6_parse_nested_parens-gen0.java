import java.util.*;
import java.lang.reflect.*;
import org.javatuples.*;
import java.security.*;
import java.math.*;
import java.io.*;
import java.util.stream.*;
class Problem {
    // Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    // For each of the group, output the deepest level of nesting of parentheses.
    // E.g. (()()) has maximum two levels of nesting while ((())) has three.
    // >>> parseNestedParens(("(()()) ((())) () ((())()())"))
    // (new ArrayList<Long>(Arrays.asList((long)2l, (long)3l, (long)1l, (long)3l)))
    public static ArrayList<Long> parseNestedParens(String paren_string) {

        // Your code goes here
        ArrayList<Long> levels = new ArrayList<Long>();
        for (String group : paren_string.split(" ")) {
            Stack<Character> s = new Stack<Character>();
            boolean good = true;
            for (char c : group.toCharArray()) {
                if (c == '(') {
                    s.push(c);
                } else if (c == ')') {
                    if (s.size() == 0) {
                        good = false;
                        break;
                    } else {
                        s.pop();
                    }
                }
            }
            if (s.size() != 0) {
                good = false;
            }
            if (good) {
                levels.add((long)s.size());
            } else {
                levels.add((long)0);
            }
        }
        return levels;
    }
    public static void main(String[] args) {
    assert(parseNestedParens(("(()()) ((())) () ((())()())")).equals((new ArrayList<Long>(Arrays.asList((long)2l, (long)3l, (long)1l, (long)3l)))));
    assert(parseNestedParens(("() (()) ((())) (((())))")).equals((new ArrayList<Long>(Arrays.asList((long)1l, (long)2l, (long)3l, (long)4l)))));
    assert(parseNestedParens(("(()(())((())))")).equals((new ArrayList<Long>(Arrays.asList((long)4l)))));
    }

}
