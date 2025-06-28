import java.util.*;
import java.lang.reflect.*;
import org.javatuples.*;
import java.security.*;
import java.math.*;
import java.io.*;
import java.util.stream.*;
class Problem {
    // Write a function that accepts two array lists of strings and returns the array list that has 
    // total number of chars in the all strings of the array list less than the other array list.
    // if the two array lists have the same number of chars, return the first array list.
    // Examples
    // >>> totalMatch((new ArrayList<String>(Arrays.asList())), (new ArrayList<String>(Arrays.asList())))
    // (new ArrayList<String>(Arrays.asList()))
    // >>> totalMatch((new ArrayList<String>(Arrays.asList((String)"hi", (String)"admin"))), (new ArrayList<String>(Arrays.asList((String)"hI", (String)"Hi"))))
    // (new ArrayList<String>(Arrays.asList((String)"hI", (String)"Hi")))
    // >>> totalMatch((new ArrayList<String>(Arrays.asList((String)"hi", (String)"admin"))), (new ArrayList<String>(Arrays.asList((String)"hi", (String)"hi", (String)"admin", (String)"project"))))
    // (new ArrayList<String>(Arrays.asList((String)"hi", (String)"admin")))
    // >>> totalMatch((new ArrayList<String>(Arrays.asList((String)"hi", (String)"admin"))), (new ArrayList<String>(Arrays.asList((String)"hI", (String)"hi", (String)"hi"))))
    // (new ArrayList<String>(Arrays.asList((String)"hI", (String)"hi", (String)"hi")))
    // >>> totalMatch((new ArrayList<String>(Arrays.asList((String)"4"))), (new ArrayList<String>(Arrays.asList((String)"1", (String)"2", (String)"3", (String)"4", (String)"5"))))
    // (new ArrayList<String>(Arrays.asList((String)"4")))
    public static ArrayList<String> totalMatch(ArrayList<String> lst1, ArrayList<String> lst2) {

        int count1 = 0;
        int count2 = 0;
        for (String str : lst1) {
            count1 += str.length();
        }
        for (String str : lst2) {
            count2 += str.length();
        }
        return count1 < count2 ? lst2 : lst1;
    }
    public static void main(String[] args) {
    assert(totalMatch((new ArrayList<String>(Arrays.asList())), (new ArrayList<String>(Arrays.asList()))).equals((new ArrayList<String>(Arrays.asList()))));
    assert(totalMatch((new ArrayList<String>(Arrays.asList((String)"hi", (String)"admin"))), (new ArrayList<String>(Arrays.asList((String)"hi", (String)"hi")))).equals((new ArrayList<String>(Arrays.asList((String)"hi", (String)"hi")))));
    assert(totalMatch((new ArrayList<String>(Arrays.asList((String)"hi", (String)"admin"))), (new ArrayList<String>(Arrays.asList((String)"hi", (String)"hi", (String)"admin", (String)"project")))).equals((new ArrayList<String>(Arrays.asList((String)"hi", (String)"admin")))));
    assert(totalMatch((new ArrayList<String>(Arrays.asList((String)"4"))), (new ArrayList<String>(Arrays.asList((String)"1", (String)"2", (String)"3", (String)"4", (String)"5")))).equals((new ArrayList<String>(Arrays.asList((String)"4")))));
    assert(totalMatch((new ArrayList<String>(Arrays.asList((String)"hi", (String)"admin"))), (new ArrayList<String>(Arrays.asList((String)"hI", (String)"Hi")))).equals((new ArrayList<String>(Arrays.asList((String)"hI", (String)"Hi")))));
    assert(totalMatch((new ArrayList<String>(Arrays.asList((String)"hi", (String)"admin"))), (new ArrayList<String>(Arrays.asList((String)"hI", (String)"hi", (String)"hi")))).equals((new ArrayList<String>(Arrays.asList((String)"hI", (String)"hi", (String)"hi")))));
    assert(totalMatch((new ArrayList<String>(Arrays.asList((String)"hi", (String)"admin"))), (new ArrayList<String>(Arrays.asList((String)"hI", (String)"hi", (String)"hii")))).equals((new ArrayList<String>(Arrays.asList((String)"hi", (String)"admin")))));
    assert(totalMatch((new ArrayList<String>(Arrays.asList())), (new ArrayList<String>(Arrays.asList((String)"this")))).equals((new ArrayList<String>(Arrays.asList()))));
    assert(totalMatch((new ArrayList<String>(Arrays.asList((String)"this"))), (new ArrayList<String>(Arrays.asList()))).equals((new ArrayList<String>(Arrays.asList()))));
    }

}
