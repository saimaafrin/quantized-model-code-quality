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

        Stack<Long> operandStack = new Stack<Long>();
        for(int i = operand.size()-1; i >= 0; i--)
            operandStack.push(operand.get(i));
        for(int i = 0; i < op.size(); i++) {
            if(op.get(i).equals("+")) {
                long b = operandStack.pop();
                long a = operandStack.pop();
                operandStack.push(a + b);
            }
            else if(op.get(i).equals("-")) {
                long b = operandStack.pop();
                long a = operandStack.pop();
                operandStack.push(a - b);
            }
            else if(op.get(i).equals("*")) {
                long b = operandStack.pop();
                long a = operandStack.pop();
                operandStack.push(a * b);
            }
            else if(op.get(i).equals("//")) {
                long b = operandStack.pop();
                long a = operandStack.pop();
                operandStack.push(a / b);
            }
            else if(op.get(i).equals("**")) {
                long b = operandStack.pop();
                long a = operandStack.pop();
                operandStack.push((long)Math.pow(a, b));
            }
        }
        return operandStack.pop();
    }
    public static void main(String[] args) {
    assert(doAlgebra((new ArrayList<String>(Arrays.asList((String)"**", (String)"*", (String)"+"))), (new ArrayList<Long>(Arrays.asList((long)2l, (long)3l, (long)4l, (long)5l)))) == (37l));
    assert(doAlgebra((new ArrayList<String>(Arrays.asList((String)"+", (String)"*", (String)"-"))), (new ArrayList<Long>(Arrays.asList((long)2l, (long)3l, (long)4l, (long)5l)))) == (9l));
    assert(doAlgebra((new ArrayList<String>(Arrays.asList((String)"//", (String)"*"))), (new ArrayList<Long>(Arrays.asList((long)7l, (long)3l, (long)4l)))) == (8l));
    }

}
