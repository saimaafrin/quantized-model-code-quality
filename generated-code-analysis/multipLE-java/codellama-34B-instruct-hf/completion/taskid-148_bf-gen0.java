import java.util.*;
import java.lang.reflect.*;
import org.javatuples.*;
import java.security.*;
import java.math.*;
import java.io.*;
import java.util.stream.*;
class Problem {
    // There are eight planets in our solar system: the closerst to the Sun 
    // is Mercury, the next one is Venus, then Earth, Mars, Jupiter, Saturn, 
    // Uranus, Neptune.
    // Write a function that takes two planet names as strings planet1 and planet2. 
    // The function should return a pair containing all planets whose orbits are 
    // located between the orbit of planet1 and the orbit of planet2, sorted by 
    // the proximity to the sun. 
    // The function should return an empty pair if planet1 or planet2
    // are not correct planet names. 
    // Examples
    // >>> bf(("Jupiter"), ("Neptune"))
    // (new ArrayList<String>(Arrays.asList((String)"Saturn", (String)"Uranus")))
    // >>> bf(("Earth"), ("Mercury"))
    // (ArrayList<String>("Venus"))
    // >>> bf(("Mercury"), ("Uranus"))
    // (new ArrayList<String>(Arrays.asList((String)"Venus", (String)"Earth", (String)"Mars", (String)"Jupiter", (String)"Saturn")))
    public static ArrayList<String> bf(String planet1, String planet2) {

        String[] planets = {
            "Mercury",
            "Venus",
            "Earth",
            "Mars",
            "Jupiter",
            "Saturn",
            "Uranus",
            "Neptune"
        };
        int p1 = 0;
        for (int i = 0; i < 8; i++) {
            if (planets[i] == planet1) {
                p1 = i;
            }
        }
        int p2 = 0;
        for (int i = 0; i < 8; i++) {
            if (planets[i] == planet2) {
                p2 = i;
            }
        }
        if (p1 == 0 && p2 == 0) {
            return new ArrayList<String>(Arrays.asList(planets[0], planets[1], planets[2], planets[3], planets[4], planets[5], planets[6]));
        }
        if (p1 == 0 && p2 == 1) {
            return new ArrayList<String>(Arrays.asList(planets[0], planets[1]));
        }
        if (p1 == 0 && p2 == 2) {
            return new ArrayList<String>(Arrays.asList(planets[0], planets[1], planets[2]));
        }
        if (p1 == 0 && p2 == 3) {
            return new ArrayList<String>(Arrays.asList(planets[0], planets[1], planets[2], planets[3]));
        }
        if (p1 == 0 && p2 == 4) {
            return new ArrayList<String>(Arrays.asList(planets[0], planets[1], planets[2], planets[3], planets[4]));
        }
        if (p1 == 0 && p2 == 5) {
            return new ArrayList<String>(Arrays.asList(planets[0], planets[1], planets[2], planets[3], planets[4], planets[5]));
        }
        if (p1 == 0 && p2 == 6) {
            return new ArrayList<String>(Arrays.asList(planets[0], planets[1], planets[2], planets[3], planets[4], planets[5], planets[6]));
        }
        if (p1 == 1 && p2 == 2) {
            return new ArrayList<String>(Arrays.asList(planets[1], planets[2]));
        }
        if (p1 == 1 && p2 == 3) {
            return new ArrayList
    }
    public static void main(String[] args) {
    assert(bf(("Jupiter"), ("Neptune")).equals((new ArrayList<String>(Arrays.asList((String)"Saturn", (String)"Uranus")))));
    assert(bf(("Earth"), ("Mercury")).equals((new ArrayList<String>(Arrays.asList((String)"Venus")))));
    assert(bf(("Mercury"), ("Uranus")).equals((new ArrayList<String>(Arrays.asList((String)"Venus", (String)"Earth", (String)"Mars", (String)"Jupiter", (String)"Saturn")))));
    assert(bf(("Neptune"), ("Venus")).equals((new ArrayList<String>(Arrays.asList((String)"Earth", (String)"Mars", (String)"Jupiter", (String)"Saturn", (String)"Uranus")))));
    assert(bf(("Earth"), ("Earth")).equals((new ArrayList<String>(Arrays.asList()))));
    assert(bf(("Mars"), ("Earth")).equals((new ArrayList<String>(Arrays.asList()))));
    assert(bf(("Jupiter"), ("Makemake")).equals((new ArrayList<String>(Arrays.asList()))));
    }

}
