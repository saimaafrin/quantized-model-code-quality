import java.util.*;
import java.lang.reflect.*;
import org.javatuples.*;
import java.security.*;
import java.math.*;
import java.io.*;
import java.util.stream.*;
class Problem {
    // Given the lengths of the three sides of a triangle. Return the area of
    // the triangle rounded to 2 decimal points if the three sides form a valid triangle. 
    // Otherwise return -1
    // Three sides make a valid triangle when the sum of any two sides is greater 
    // than the third side.
    // Example:
    // >>> triangleArea((3l), (4l), (5l))
    // (6.0f)
    // >>> triangleArea((1l), (2l), (10l))
    // (float)-1l
    public static float triangleArea(long a, long b, long c) {

        if (a >= b + c || b >= a + c || c >= a + b) {
            return -1.0f;
        }
        float s = (a + b + c) / 2;
        return (float) Math.sqrt(s * (s - a) * (s - b) * (s - c));
    }
    public static void main(String[] args) {
    assert(triangleArea((3l), (4l), (5l)) == (6.0f));
    assert(triangleArea((1l), (2l), (10l)) == (float)-1l);
    assert(triangleArea((4l), (8l), (5l)) == (8.18f));
    assert(triangleArea((2l), (2l), (2l)) == (1.73f));
    assert(triangleArea((1l), (2l), (3l)) == (float)-1l);
    assert(triangleArea((10l), (5l), (7l)) == (16.25f));
    assert(triangleArea((2l), (6l), (3l)) == (float)-1l);
    assert(triangleArea((1l), (1l), (1l)) == (0.43f));
    assert(triangleArea((2l), (2l), (10l)) == (float)-1l);
    }

}
