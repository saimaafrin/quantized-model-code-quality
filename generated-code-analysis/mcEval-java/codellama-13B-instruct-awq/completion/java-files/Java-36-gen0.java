import java.util.ArrayList;
import java.util.List;

class Problem {

  /**
   * Find all stepping numbers in the range [low, high] where a stepping number is defined as a number where each digit is either one more or one less than the adjacent digit.
   *
   * @param low The lower bound of the range.
   * @param high The upper bound of the range.
   * @return A list of stepping numbers within the range [low, high] sorted in ascending order.
   *
   * Example:
   * findSteppingNumbers(0, 21)
   * Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 21]
   */
  public static List<Integer> findSteppingNumbers(int low, int high)  {
    List<Integer> result = new ArrayList<>();
    if (low > high || high < 0 || low < 0) {
      return result;
    }
    int n = high - low;
    for (int i = 0; i <= n; i++) {
      int candidate = low + i;
      if (candidate % 10 == candidate / 10) {
        result.add(candidate);
      }
    }
    return result;
  }
  public static void main(String[] args) {
    assert findSteppingNumbers(0, 21)
      .equals(
        new ArrayList<>(List.of(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 21))
      );
    assert findSteppingNumbers(10, 15).equals(new ArrayList<>(List.of(10, 12)));
    assert findSteppingNumbers(50, 55).equals(List.of(54));

    System.out.println("All tests passed");
  }
}
