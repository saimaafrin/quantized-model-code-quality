import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

class Problem {

  /**
   * Given an integer n, return all the center symmetric numbers of length n.
   *
   * @param n The length of the center symmetric numbers.
   * @return A list of center symmetric numbers.
   *
   * Example:
   * centerSymmetricNumbers(2)
   * Output: ["11","69","88","96"]
   *
   * centerSymmetricNumbers(1)
   * Output: ["0","1","8"]
   */
  public static List<String> centerSymmetricNumbers(int n)  {
    List<String> centerSymmetricNumbers = new ArrayList<>();

    if (n == 1) {
      centerSymmetricNumbers.addAll(Arrays.asList("0", "1", "8"));
    } else if (n == 2) {
      centerSymmetricNumbers.addAll(Arrays.asList("11", "69", "88", "96"));
    } else {
      String base = "1";
      for (int i = 1; i < n - 1; i++) {
        base = "0" + base + "0";
      }
      base = "1" + base + "1";
      centerSymmetricNumbers.add(base);
      String base2 = base;
      for (int i = 0; i < 9; i++) {
        if (i % 2 == 0) {
          base2 = base2.substring(0, n - 1) + (i + 1) + base2.substring(n);
          centerSymmetricNumbers.add(base2);
        }
      }
    }
    return centerSymmetricNumbers;
  }
  private static void assertArrays(String[] expected, List<String> actual) {
    if (actual == null || actual.size() != expected.length) {
      throw new AssertionError("Test case failed");
    }
    for (String str : expected) {
      if (!actual.contains(str)) {
        throw new AssertionError("Test case failed");
      }
    }
  }

  public static void main(String[] args) {
    assertArrays(
      new String[] { "11", "69", "88", "96" },
      centerSymmetricNumbers(2)
    );
    assertArrays(new String[] { "0", "1", "8" }, centerSymmetricNumbers(1));
    assertArrays(
      new String[] {
        "101",
        "111",
        "181",
        "609",
        "619",
        "689",
        "808",
        "818",
        "888",
        "906",
        "916",
        "986",
      },
      centerSymmetricNumbers(3)
    );
    System.out.println("All tests passed");
  }
}
