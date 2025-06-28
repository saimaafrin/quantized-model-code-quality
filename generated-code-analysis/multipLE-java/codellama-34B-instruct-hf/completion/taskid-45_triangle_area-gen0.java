import java.util.*;
import java.lang.reflect.*;
import org.javatuples.*;
import java.security.*;
import java.math.*;
import java.io.*;
import java.util.stream.*;
class Problem {
    // Given length of a side and high return area for a triangle.
    // >>> triangleArea((5l), (3l))
    // (7.5f)
    public static float triangleArea(long a, long h) {

        return (float) (a * h / 2);
    }
    public static void main(String[] args) {
    assert(triangleArea((5l), (3l)) == (7.5f));
    assert(triangleArea((2l), (2l)) == (2.0f));
    assert(triangleArea((10l), (8l)) == (40.0f));
    }

}
