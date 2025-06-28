import java.util.*;
import java.lang.reflect.*;
import org.javatuples.*;
import java.security.*;
import java.math.*;
import java.io.*;
import java.util.stream.*;
class Problem {
    // You'll be given a string of words, and your task is to count the number
    // of boredoms. A boredom is a sentence that starts with the word "I".
    // Sentences are delimited by '.', '?' or '!'.
    // For example:
    // >>> isBored(("Hello world"))
    // (0l)
    // >>> isBored(("The sky is blue. The sun is shining. I love this weather"))
    // (1l)
    public static long isBored(String S) {

        return Arrays.stream(S.split("[.?!]")).filter(x -> x.startsWith("I")).count();
    }
    public static void main(String[] args) {
    assert(isBored(("Hello world")) == (0l));
    assert(isBored(("Is the sky blue?")) == (0l));
    assert(isBored(("I love It !")) == (1l));
    assert(isBored(("bIt")) == (0l));
    assert(isBored(("I feel good today. I will be productive. will kill It")) == (2l));
    assert(isBored(("You and I are going for a walk")) == (0l));
    }

}
