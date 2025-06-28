import java.util.*;
import java.lang.reflect.*;
import org.javatuples.*;
import java.security.*;
import java.math.*;
import java.io.*;
import java.util.stream.*;
class Problem {
    // You are given a string s.
    // if s[i] is a letter, reverse its case from lower to upper or vise versa, 
    // otherwise keep it as it is.
    // If the string contains no letters, reverse the string.
    // The function should return the resulted string.
    // Examples
    // >>> solve(("1234"))
    // ("4321")
    // >>> solve(("ab"))
    // ("AB")
    // >>> solve(("#a@C"))
    // ("#A@c")
    public static String solve(String s) {

        String res = "";
        if(s.matches(".*[a-zA-Z].*")){
            for(int i=0; i<s.length(); i++){
                char c = s.charAt(i);
                if(c>= 'a' && c <= 'z'){
                    c = (char) (c-'a'+'A');
                }else if(c >= 'A' && c <= 'Z'){
                    c = (char) (c-'A'+'a');
                }
                res += c;
            }
        }else{
            res = s.substring(s.length()-1);
            for(int i = s.length()-2; i>=0; i--){
                res += s.charAt(i);
            }
        }
        return res;
    }
    public static void main(String[] args) {
    assert(solve(("AsDf")).equals(("aSdF")));
    assert(solve(("1234")).equals(("4321")));
    assert(solve(("ab")).equals(("AB")));
    assert(solve(("#a@C")).equals(("#A@c")));
    assert(solve(("#AsdfW^45")).equals(("#aSDFw^45")));
    assert(solve(("#6@2")).equals(("2@6#")));
    assert(solve(("#$a^D")).equals(("#$A^d")));
    assert(solve(("#ccc")).equals(("#CCC")));
    }

}
