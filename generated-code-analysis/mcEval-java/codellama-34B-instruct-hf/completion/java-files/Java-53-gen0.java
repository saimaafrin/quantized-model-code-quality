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
    // return s;

    // 1. Split the string into words
    // 2. Reverse each word
    // 3. Combine the words back to a sentence

    // String[] words = s.split(" ");
    // StringBuilder sb = new StringBuilder();

    // for (String word : words) {
    //   char[] chars = word.toCharArray();
    //   int left = 0;
    //   int right = chars.length - 1;

    //   while (left < right) {
    //     char temp = chars[left];
    //     chars[left++] = chars[right];
    //     chars[right--] = temp;
    //   }
    //   sb.append(new String(chars) + " ");
    // }
    // return sb.toString().trim();

    // Stream API
    return Arrays.stream(s.split(" "))
      .map(word -> new StringBuilder(word).reverse().toString())
      .collect(Collectors.joining(" "));
  }
  public static void main(String[] args) {
    assert reverseWords("The quick brown fox").equals("ehT kciuq nworb xof") : "Test failed for input: The quick brown fox";
    assert reverseWords("Hello World").equals("olleH dlroW") : "Test failed for input: Hello World";
    assert reverseWords("a b c d e f").equals("a b c d e f") : "Test failed for input: a b c d e f";
    System.out.println("All tests passed");
  }
}