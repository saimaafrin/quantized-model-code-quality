import java.util.*;
import java.lang.reflect.*;
import org.javatuples.*;
import java.security.*;
import java.math.*;
import java.io.*;
import java.util.stream.*;
class Problem {
    // brackets is a string of "<" and ">".
    // return true if every opening bracket has a corresponding closing bracket.
    // >>> correctBracketing(("<"))
    // (false)
    // >>> correctBracketing(("<>"))
    // (true)
    // >>> correctBracketing(("<<><>>"))
    // (true)
    // >>> correctBracketing(("><<>"))
    // (false)
    public static boolean correctBracketing(String brackets) {

        if (brackets.equals("")) return true;
        return brackets.charAt(0) == '<' ?
            (brackets.charAt(1) == '<' ?
            correctBracketing(brackets.substring(2)) :
            (brackets.charAt(1) == '>' ?
            false :
            correctBracketing(brackets.substring(2)))) :
            (brackets.charAt(0) == '>' ?
            correctBracketing(brackets.substring(1)) :
            false);
    }
    public static void main(String[] args) {
    assert(correctBracketing(("<>")) == (true));
    assert(correctBracketing(("<<><>>")) == (true));
    assert(correctBracketing(("<><><<><>><>")) == (true));
    assert(correctBracketing(("<><><<<><><>><>><<><><<>>>")) == (true));
    assert(correctBracketing(("<<<><>>>>")) == (false));
    assert(correctBracketing(("><<>")) == (false));
    assert(correctBracketing(("<")) == (false));
    assert(correctBracketing(("<<<<")) == (false));
    assert(correctBracketing((">")) == (false));
    assert(correctBracketing(("<<>")) == (false));
    assert(correctBracketing(("<><><<><>><>><<>")) == (false));
    assert(correctBracketing(("<><><<><>><>>><>")) == (false));
    }

}
