import java.util.*;
import java.lang.reflect.*;
import org.javatuples.*;
import java.security.*;
import java.math.*;
import java.io.*;
import java.util.stream.*;
class Problem {
    // Imagine a road that's a perfectly straight infinitely long line.
    // n cars are driving left to right;  simultaneously, a different set of n cars
    // are driving right to left.   The two sets of cars start out being very far from
    // each other.  All cars move in the same speed.  Two cars are said to collide
    // when a car that's moving left to right hits a car that's moving right to left.
    // However, the cars are infinitely sturdy and strong; as a result, they continue moving
    // in their trajectory as if they did not collide.
    // This function outputs the number of such collisions.
    public static long carRaceCollision(long n) {

        // The cars start n distance apart from each other
        long nDistance = n;
        long nLeft = n;
        long nRight = n;
        long nCollisions = 0;
        long nPosition;
        // The cars move to the right
        nPosition = nLeft - 1;
        while(nPosition > 0) {
            nPosition--;
            // nPosition + nDistance is the distance between the cars
            if((nPosition + nDistance) <= nRight) {
                nCollisions++;
            }
            nRight--;
            nDistance--;
        }
        // The cars move to the left
        nPosition = nRight - 1;
        nDistance = n;
        while(nPosition > 0) {
            nPosition--;
            // nDistance is the distance between the cars
            if((nDistance + nPosition) <= nLeft) {
                nCollisions++;
            }
            nLeft--;
            nDistance--;
        }
        return nCollisions;
    }
    public static void main(String[] args) {
    assert(carRaceCollision((2l)) == (4l));
    assert(carRaceCollision((3l)) == (9l));
    assert(carRaceCollision((4l)) == (16l));
    assert(carRaceCollision((8l)) == (64l));
    assert(carRaceCollision((10l)) == (100l));
    }

}
