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
    // Convert the integer to a string
    String str = Integer.toString(n);

    // Add a dot every three digits, starting from the right-hand side
    // and working our way to the left.
    StringBuilder sb = new StringBuilder();
    int count = 0;
    for (int i = str.length() - 1; i >= 0; i--) {
      char c = str.charAt(i);
      sb.insert(0, c);
      if (++count == 3) {
        sb.insert(0, '.');
        count = 0;
      }
    }

    // If there are no characters remaining, return "0".
    if (sb.length() == 0) {
      return "0";
    }

    // Return the string.
    return sb.toString();
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