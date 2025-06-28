import java.util.*;
import java.lang.reflect.*;
import org.javatuples.*;
import java.security.*;
import java.math.*;
import java.io.*;
import java.util.stream.*;
class Problem {
    // Input is a space-delimited string of numberals from 'zero' to 'nine'.
    // Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    // Return the string with numbers sorted from smallest to largest
    // >>> sortNumbers(("three one five"))
    // ("one three five")
    public static String sortNumbers(String numbers) {

        String[] number_names = numbers.split(" ");
        List<Pair<Integer, String>> number_name_pairs = new ArrayList<>();
        for(String number_name: number_names){
            number_name_pairs.add(new Pair<>(getNumberFromName(number_name), number_name));
        }
        Collections.sort(number_name_pairs, Comparator.comparing(Pair::getValue0));
        StringBuilder output_string = new StringBuilder();
        for(Pair<Integer, String> number_name_pair: number_name_pairs){
            output_string.append(number_name_pair.getValue1());
            output_string.append(' ');
        }
        return output_string.toString().stripTrailing();
    }
    public static void main(String[] args) {
    assert(sortNumbers(("")).equals(("")));
    assert(sortNumbers(("three")).equals(("three")));
    assert(sortNumbers(("three five nine")).equals(("three five nine")));
    assert(sortNumbers(("five zero four seven nine eight")).equals(("zero four five seven eight nine")));
    assert(sortNumbers(("six five four three two one zero")).equals(("zero one two three four five six")));
    }

}
