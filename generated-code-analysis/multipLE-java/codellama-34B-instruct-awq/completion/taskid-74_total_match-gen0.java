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

        String[] lst1_array = new String[lst1.size()];
        String[] lst2_array = new String[lst2.size()];
        int lst1_total = 0;
        int lst2_total = 0;
        lst1_array = lst1.toArray(lst1_array);
        lst2_array = lst2.toArray(lst2_array);
        for(int i = 0; i < lst1.size(); i++) {
            lst1_total += lst1_array[i].length();
        }
        for(int i = 0; i < lst2.size(); i++) {
            lst2_total += lst2_array[i].length();
        }
        if(lst1_total < lst2_total) {
            return lst1;
        } else {
            return lst2;
        }
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
