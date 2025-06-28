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

        // Your code here
        if(lst1.size() == 0 && lst2.size() == 0) {
            return new ArrayList<String>();
        }
        if(lst1.size() == 0) {
            return lst2;
        }
        if(lst2.size() == 0) {
            return lst1;
        }
        int[] count1 = new int[lst1.size()];
        int[] count2 = new int[lst2.size()];
        for(int i = 0; i < lst1.size(); i++) {
            count1[i] = lst1.get(i).length();
        }
        for(int i = 0; i < lst2.size(); i++) {
            count2[i] = lst2.get(i).length();
        }
        for(int i = 0; i < count1.length; i++) {
            for(int j = 0; j < count2.length; j++) {
                count1[i] += count2[j];
            }
        }
        int max = 0;
        ArrayList<String> ret = new ArrayList<String>();
        for(int i = 0; i < count1.length; i++) {
            if(count1[i] > max) {
                max = count1[i];
                ret.add(lst1.get(i));
            }
        }
        for(int i = 0; i < count2.length; i++) {
            if(count2[i] == max) {
                ret.add(lst2.get(i));
            }
        }
        return ret;
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
