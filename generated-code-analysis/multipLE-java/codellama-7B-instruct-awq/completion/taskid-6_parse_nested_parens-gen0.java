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

        // List of integers of corresponding nesting level for each group of parentheses.
        // e.g. if paren_string == "((()) ((())) () ((())()())", then
        // level_list == [2, 3, 1, 3, 2, 1, 3, 2, 1, 2]
        ArrayList<Integer> level_list = new ArrayList<>();
        int curr_level = 0;
        int max_level = 0;
        // List of index of opening parentheses.
        ArrayList<Integer> open_idx_list = new ArrayList<>();
        // Index of the last closing parentheses.
        int last_close_idx = -1;
        int curr_idx = 0;
        while (curr_idx < paren_string.length()) {
            char curr_char = paren_string.charAt(curr_idx);
            if (curr_char == '(') {
                // If we encounter an opening parentheses, update the level and add it to open_idx_list.
                level_list.add(curr_level);
                open_idx_list.add(curr_idx);
                curr_level++;
            } else if (curr_char == ')') {
                // If we encounter a closing parentheses, update the level and add it to open_idx_list.
                level_list.add(curr_level);
                open_idx_list.add(curr_idx);
                // If the current level is greater than the maximum, update maximum.
                if (curr_level > max_level) {
                    max_level = curr_level;
                }
                // If the current level is not 0, reduce the level and set the current index to the index of the opening parentheses.
                if (curr_level != 0) {
                    curr_level--;
                    curr_idx = open_idx_list.get(open_idx_list.size() - 1);
                    open_idx_list.remove(open_idx_list.size() - 1);
                } else {
                    // If the current level is 0, set the last closing index to the current index.
                    last_close_idx = curr_idx;
                }
            }
            curr_idx++;
        }
        // Add the last index of the closing parentheses to open_idx_list.
        if (last_close_idx >= 0) {
            open_idx_list.add(last_close_idx);
        }
        // Output list of levels.
        ArrayList<Long> level_list_out = new ArrayList<>();
        for (int i = 0; i < open_idx_list.size(); i++) {
            int start_idx = open_idx_list.get(i);
            int end_idx = open_idx_list.get(i + 1) - 1;
            // If the index of the closing parentheses is greater than the index of the opening parentheses,
            // set the level of the current group to be the maximum level.
            if (end_idx >= start_idx) {
                level_list_out.add(max_level);
            } else {
                // If the index of the closing parentheses is less than the index of the opening parentheses,
                // set the level of the current group to be the level of the current group.
                level_list_out.add(level_list.get(i));
            }
        }
        return level_list_out;
    }
    public static void main(String[] args) {
    assert(parseNestedParens(("(()()) ((())) () ((())()())")).equals((new ArrayList<Long>(Arrays.asList((long)2l, (long)3l, (long)1l, (long)3l)))));
    assert(parseNestedParens(("() (()) ((())) (((())))")).equals((new ArrayList<Long>(Arrays.asList((long)1l, (long)2l, (long)3l, (long)4l)))));
    assert(parseNestedParens(("(()(())((())))")).equals((new ArrayList<Long>(Arrays.asList((long)4l)))));
    }

}
