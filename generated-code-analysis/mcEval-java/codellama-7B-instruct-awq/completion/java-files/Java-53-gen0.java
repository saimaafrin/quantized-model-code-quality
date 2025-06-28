class Problem {

  /**
   * Reverse the characters of each word in the given string while maintaining the original word order.
   *
   * @param s The input string containing words separated by spaces.
   * @return The string with characters of each word reversed.
   *
   * Example:
   * reverseWords("Mr Ding")
   * Output: "rM gniD"
   */
  public static String reverseWords(String s)  {
    // Split the string into an array of words.
    String[] words = s.split(" ");

    // Reverse each word and store the result in a new array.
    String[] reversedWords = new String[words.length];
    for (int i = 0; i < words.length; i++) {
      String word = words[i];
      char[] charArray = word.toCharArray();
      charArray = reverse(charArray);
      reversedWords[i] = new String(charArray);
    }

    // Join the reversed words into a single string separated by spaces.
    StringBuilder reversedString = new StringBuilder();
    for (int i = 0; i < reversedWords.length; i++) {
      reversedString.append(reversedWords[i]);
      if (i < reversedWords.length - 1) {
        reversedString.append(" ");
      }
    }
    return reversedString.toString();
  }
  public static void main(String[] args) {
    assert reverseWords("The quick brown fox").equals("ehT kciuq nworb xof") : "Test failed for input: The quick brown fox";
    assert reverseWords("Hello World").equals("olleH dlroW") : "Test failed for input: Hello World";
    assert reverseWords("a b c d e f").equals("a b c d e f") : "Test failed for input: a b c d e f";
    System.out.println("All tests passed");
  }
}