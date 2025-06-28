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
    List<String> list = new ArrayList<>();
    if (n == 1) {
      list.add("0");
      list.add("1");
      list.add("8");
      return list;
    }
    int min = (int) Math.pow(10, n - 1);
    int max = (int) Math.pow(10, n) - 1;
    for (int i = min; i <= max; i++) {
      String str = String.valueOf(i);
      int left = 0;
      int right = str.length() - 1;
      while (left < right) {
        if (str.charAt(left) != str.charAt(right)) {
          break;
        }
        left++;
        right--;
      }
      if (left == right) {
        list.add(str);
      }
    }
    return list;
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
