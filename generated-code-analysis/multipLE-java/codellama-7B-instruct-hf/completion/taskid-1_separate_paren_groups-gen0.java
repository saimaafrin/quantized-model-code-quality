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

        // Step 1:
        // Split the string into a string array based on " "
        String[] parts = paren_string.split(" ");
        // Step 2:
        // Convert all parens to array
        String[][] parts_arr = new String[parts.length][parts.length];
        for(int i=0;i<parts.length;i++){
            parts_arr[i] = parts[i].toCharArray();
        }
        // Step 3:
        // Get the index of the first occurence of "(" or ")"
        // Loop through the array and check if each "(" or ")" is balanced with another "(" or ")", and if it's not return false
        for(int i=0;i<parts.length;i++){
            int open_count = 0;
            int close_count = 0;
            for(int j=0;j<parts[i].length();j++){
                if(parts[i][j] == '('){
                    open_count++;
                }
                else if(parts[i][j] == ')'){
                    close_count++;
                }
                if(open_count != close_count){
                    return new ArrayList<String>();
                }
            }
        }
        // Step 4:
        // Go through the array again, but this time look for "(" and ")" and replace them with the next
        // available index of the new array
        // return the final array
        String[] final_arr = new String[parts_arr.length];
        for(int i=0;i<parts_arr.length;i++){
            String new_string = "";
            for(int j=0;j<parts_arr[i].length;j++){
                if(parts_arr[i][j] == '('){
                    new_string += final_arr[j];
                }
                else if(parts_arr[i][j] == ')'){
                    new_string += final_arr[j];
                }
                else{
                    new_string += parts_arr[i][j];
                }
            }
            final_arr[i] = new_string;
        }
        return new ArrayList<String>(Arrays.asList(final_arr));
    }
    public static void main(String[] args) {
    assert(separateParenGroups(("(()()) ((())) () ((())()())")).equals((new ArrayList<String>(Arrays.asList((String)"(()())", (String)"((()))", (String)"()", (String)"((())()())")))));
    assert(separateParenGroups(("() (()) ((())) (((())))")).equals((new ArrayList<String>(Arrays.asList((String)"()", (String)"(())", (String)"((()))", (String)"(((())))")))));
    assert(separateParenGroups(("(()(())((())))")).equals((new ArrayList<String>(Arrays.asList((String)"(()(())((())))")))));
    assert(separateParenGroups(("( ) (( )) (( )( ))")).equals((new ArrayList<String>(Arrays.asList((String)"()", (String)"(())", (String)"(()())")))));
    }

}
