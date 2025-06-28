import java.util.*;

class Problem {
    /**
     * Given an array of strings words where each word can be written as a concatenation of the Morse code of each letter,
     * return the number of different transformations among all words.
     *
     * Example:
     * uniqueMorseRepresentations(["gin","zen","gig","msg"]) -> 2
     * uniqueMorseRepresentations(["a"]) -> 1
     */
    public int uniqueMorseRepresentations(String[] words)  {
        // Initialize the mapping of each letter to its corresponding Morse code
        String[] morseCodes = new String[]{"....-", ".-..-", "-..-.", "-....", "..--", "....-", ".---", "-.-", ".-..", "-.--", "--.."};

        // Initialize a set to store the unique Morse code representations of each word
        Set<String> uniqueCodes = new HashSet<>();

        // Iterate through the array of words
        for (String word : words) {
            String morseCode = "";

            // Iterate through the letters of the current word
            for (int i = 0; i < word.length(); i++) {
                char letter = word.charAt(i);

                // Find the index of the letter in the array of letters
                int index = word.indexOf(letter);

                // Find the corresponding Morse code of the letter and add it to the Morse code representation of the current word
                morseCode += morseCodes[index];
            }

            // Add the Morse code representation of the current word to the set of unique Morse code representations
            uniqueCodes.add(morseCode);
        }

        // Return the number of unique Morse code representations
        return uniqueCodes.size();
    }
    public static void main(String[] args) {
        Problem solution = new Problem();

        // Test the function with different test cases
        assert solution.uniqueMorseRepresentations(new String[]{"hello", "world", "hello"}) == 2;
        assert solution.uniqueMorseRepresentations(new String[]{"abc", "def", "ghi"}) == 3;
        assert solution.uniqueMorseRepresentations(new String[]{"aaa", "aaa", "aaa"}) == 1;
        System.out.println("All tests passed");
    }
}