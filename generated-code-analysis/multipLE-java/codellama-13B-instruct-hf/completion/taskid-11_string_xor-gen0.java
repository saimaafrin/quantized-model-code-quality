import java.util.*;
import java.lang.reflect.*;
import org.javatuples.*;
import java.security.*;
import java.math.*;
import java.io.*;
import java.util.stream.*;
class Problem {
    // Input are two strings a and b consisting only of 1s and 0s.
    // Perform binary XOR on these inputs and return result also as a string.
    // >>> stringXor(("010"), ("110"))
    // ("100")
    public static String stringXor(String a, String b) {

        char[] a1 = a.toCharArray();
        char[] b1 = b.toCharArray();
        StringBuilder result = new StringBuilder();
        for(int i=0;i<a1.length;i++){
            if(a1[i]=='0'&&b1[i]=='0'){
                result.append('0');
            }
            else if(a1[i]=='1'&&b1[i]=='1'){
                result.append('0');
            }
            else{
                result.append('1');
            }
        }
        return result.toString();
    }
    public static void main(String[] args) {
    assert(stringXor(("111000"), ("101010")).equals(("010010")));
    assert(stringXor(("1"), ("1")).equals(("0")));
    assert(stringXor(("0101"), ("0000")).equals(("0101")));
    }

}
