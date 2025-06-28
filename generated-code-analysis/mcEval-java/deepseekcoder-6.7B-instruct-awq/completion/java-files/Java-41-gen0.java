class Problem {

  /**
   * Given an integer n, add a dot ('.') as a thousand separator every three digits and return the result as a string.
   *
   * @param n The integer to add thousand separators to.
   * @return The string with thousand separators added.
   *
   * Example:
   * addThousandSeparator(987)
   * Output: "987"
   *
   * Example:
   * addThousandSeparator(1234)
   * Output: "1.234"
   *
   * Example:
   * addThousandSeparator(123456789)
   * Output: "123.456.789"
   *
   * Example:
   * addThousandSeparator(0)
   * Output: "0"
   */
  public static String addThousandSeparator(int n)  {
    // If the number is zero, return "0"
    if (n == 0) {
      return "0";
    }

    // Convert the number to a string
    String number = Integer.toString(n);

    // Initialize a string builder
    StringBuilder result = new StringBuilder();

    // Loop through the string in reverse
    for (int i = 0; i < number.length(); i++) {
      // If the current character is the last one and its index mod 3 is 0, add it to the result
      if (i == number.length() - 1 && i % 3 == 0) {
        result.insert(0, number.charAt(i));
      }
      // If the current index mod 3 is 0, add a dot and the current character to the result
      else if (i % 3 == 0) {
        result.insert(0, number.charAt(i));
        result.insert(0, '.');
      }
      // Otherwise, just add the current character to the result
      else {
        result.insert(0, number.charAt(i));
      }
    }

    // Return the result as a string
    return result.toString();
  }
  public static void main(String[] args) {
    assert "2.147.483.647".equals(
        addThousandSeparator(2147483647)
      ) : "Test case 1 failed";
    assert "10.000".equals(addThousandSeparator(10000)) : "Test case 2 failed";
    assert "999".equals(addThousandSeparator(999)) : "Test case 3 failed";
    System.out.println("All tests passed");
  }
}