import java.util.*;
import java.lang.reflect.*;
import org.javatuples.*;
import java.security.*;
import java.math.*;
import java.io.*;
import java.util.stream.*;
class Problem {
    // I think we all remember that feeling when the result of some long-awaited
    // event is finally known. The feelings and thoughts you have at that moment are
    // definitely worth noting down and comparing.
    // Your task is to determine if a person correctly guessed the results of a number of matches.
    // You are given two array array lists of scores and guesses of equal length, where each index shows a match. 
    // Return an array array list of the same length denoting how far off each guess was. If they have guessed correctly,
    // the value is 0, and if not, the value is the absolute difference between the guess and the score.
    // example:
    // >>> compare((new ArrayList<Long>(Arrays.asList((long)1l, (long)2l, (long)3l, (long)4l, (long)5l, (long)1l))), (new ArrayList<Long>(Arrays.asList((long)1l, (long)2l, (long)3l, (long)4l, (long)2l, (long)-2l))))
    // (new ArrayList<Long>(Arrays.asList((long)0l, (long)0l, (long)0l, (long)0l, (long)3l, (long)3l)))
    // >>> compare((new ArrayList<Long>(Arrays.asList((long)0l, (long)5l, (long)0l, (long)0l, (long)0l, (long)4l))), (new ArrayList<Long>(Arrays.asList((long)4l, (long)1l, (long)1l, (long)0l, (long)0l, (long)-2l))))
    // (new ArrayList<Long>(Arrays.asList((long)4l, (long)4l, (long)1l, (long)0l, (long)0l, (long)6l)))
    public static ArrayList<Long> compare(ArrayList<Long> game, ArrayList<Long> guess) {

        ArrayList<Long> result = new ArrayList<Long>(Collections.nCopies(guess.size(), (long)0));
        for (int i = 0; i < guess.size(); i++) {
            if (guess.get(i).longValue() == game.get(i).longValue()) {
                result.set(i, (long)0);
            } else {
                result.set(i, (long)Math.abs(guess.get(i).longValue() - game.get(i).longValue()));
            }
        }
        return result;
    }
    public static void main(String[] args) {
    assert(compare((new ArrayList<Long>(Arrays.asList((long)1l, (long)2l, (long)3l, (long)4l, (long)5l, (long)1l))), (new ArrayList<Long>(Arrays.asList((long)1l, (long)2l, (long)3l, (long)4l, (long)2l, (long)-2l)))).equals((new ArrayList<Long>(Arrays.asList((long)0l, (long)0l, (long)0l, (long)0l, (long)3l, (long)3l)))));
    assert(compare((new ArrayList<Long>(Arrays.asList((long)0l, (long)0l, (long)0l, (long)0l, (long)0l, (long)0l))), (new ArrayList<Long>(Arrays.asList((long)0l, (long)0l, (long)0l, (long)0l, (long)0l, (long)0l)))).equals((new ArrayList<Long>(Arrays.asList((long)0l, (long)0l, (long)0l, (long)0l, (long)0l, (long)0l)))));
    assert(compare((new ArrayList<Long>(Arrays.asList((long)1l, (long)2l, (long)3l))), (new ArrayList<Long>(Arrays.asList((long)-1l, (long)-2l, (long)-3l)))).equals((new ArrayList<Long>(Arrays.asList((long)2l, (long)4l, (long)6l)))));
    assert(compare((new ArrayList<Long>(Arrays.asList((long)1l, (long)2l, (long)3l, (long)5l))), (new ArrayList<Long>(Arrays.asList((long)-1l, (long)2l, (long)3l, (long)4l)))).equals((new ArrayList<Long>(Arrays.asList((long)2l, (long)0l, (long)0l, (long)1l)))));
    }

}
