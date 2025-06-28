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
    if (n == 0) {
      return "0";
    }

    // Get the absolute value of the integer as a string.
    String absNString = Integer.toString(Math.abs(n));

    // Get the length of the integer as a string.
    int length = absNString.length();

    // Get the number of groups of 3 digits.
    int groups = length / 3;

    // Get the remainder.
    int remainder = length % 3;

    // Get the number of digits in the last group.
    int lastGroup = remainder == 0 ? 3 : remainder;

    // Initialize the string builder.
    StringBuilder builder = new StringBuilder(length + groups);

    // Add the negative sign if needed.
    if (n < 0) {
      builder.append('-');
    }

    // Add the first group.
    int start = length - lastGroup;
    builder.append(absNString, start, length);

    // Add the remaining groups.
    for (int i = start - 3; i >= 0; i -= 3) {
      builder.append('.').append(absNString, i, i + 3);
    }

    // Return the string.
    return builder.toString();
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