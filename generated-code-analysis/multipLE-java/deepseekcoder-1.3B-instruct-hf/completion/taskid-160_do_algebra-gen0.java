import java.util.*;
import java.lang.reflect.*;
import org.javatuples.*;
import java.security.*;
import java.math.*;
import java.io.*;
import java.util.stream.*;
class Problem {
    // Given two array lists operator, and operand. The first array list has basic algebra operations, and 
    // the second array list is an array array list of integers. Use the two given array lists to build the algebric 
    // expression and return the evaluation of this expression.
    // The basic algebra operations:
    // Addition ( + ) 
    // Subtraction ( - ) 
    // Multiplication ( * ) 
    // Floor division ( // ) 
    // Exponentiation ( ** ) 
    // Example:
    // operator['+', '*', '-']
    // array array list = [2, 3, 4, 5]
    // result = 2 + 3 * 4 - 5
    // => result = 9
    // Note:
    // The length of operator array list is equal to the length of operand array list minus one.
    // Operand is an array array list of of non-negative integers.
    // Operator array list has at least one operator, and operand array list has at least two operands.
    public static long doAlgebra(ArrayList<String> op, ArrayList<Long> operand) {

        String operators = String.join("", op);
        String regex = "[^0-9]";
        operand.replaceAll(Pattern.compile(regex).matcher(String.join("", operand)).replaceAll(""));
        operand.replaceAll(Pattern.compile(regex).matcher(String.join("", operand)).replaceAll(""));
        for (int i = 0; i < operators.length(); i++) {
            switch (operators.charAt(i)) {
                case '+':
                    operand.set(i, operand.get(i) + operand.get(i + 1));
                    break;
                case '-':
                    operand.set(i, operand.get(i) - operand.get(i + 1));
                    break;
                case '*':
                    operand.set(i, operand.get(i) * operand.get(i + 1));
                    break;
                case '/':
                    operand.set(i, operand.get(i) / operand.get(i + 1));
                    break;
                case '^':
                    operand.set(i, (long) Math.pow(operand.get(i), operand.get(i + 1)));
                    break;
            }
        }
        return operand.get(0);
    }
    public static void main(String[] args) {
    assert(doAlgebra((new ArrayList<String>(Arrays.asList((String)"**", (String)"*", (String)"+"))), (new ArrayList<Long>(Arrays.asList((long)2l, (long)3l, (long)4l, (long)5l)))) == (37l));
    assert(doAlgebra((new ArrayList<String>(Arrays.asList((String)"+", (String)"*", (String)"-"))), (new ArrayList<Long>(Arrays.asList((long)2l, (long)3l, (long)4l, (long)5l)))) == (9l));
    assert(doAlgebra((new ArrayList<String>(Arrays.asList((String)"//", (String)"*"))), (new ArrayList<Long>(Arrays.asList((long)7l, (long)3l, (long)4l)))) == (8l));
    }

}
