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
    List<Integer> res = new ArrayList<>();
    // For each number from 0 to 9, add it to the queue
    for (int i = 0; i <= 9; i++) {
      if (i >= low && i <= high) {
        res.add(i);
      }
    }
    if (low == 0) { // if low is 0, 0 is not considered in the range
      res.remove(0);
    }
    for (int i = 1; i <= 9; i++) {
      // Create a BFS tree, use the first digit of the number to decide the next digit
      // if the number is within the range, add it to the result list
      int num = i;
      while (num <= high) {
        int lastDigit = num % 10;
        int nextNum1 = num * 10 + (lastDigit - 1);
        int nextNum2 = num * 10 + (lastDigit + 1);
        if (lastDigit == 0 && nextNum2 <= high) {
          if (nextNum2 >= low) {
            res.add(nextNum2);
          }
          num = nextNum2;
        } else if (lastDigit == 9 && nextNum1 <= high) {
          if (nextNum1 >= low) {
            res.add(nextNum1);
          }
          num = nextNum1;
        } else {
          if (nextNum1 <= high && nextNum1 >= low) {
            res.add(nextNum1);
          }
          if (nextNum2 <= high && nextNum2 >= low) {
            res.add(nextNum2);
          }
          num = nextNum2;
        }
      }
    }
    // sort the result list
    res.sort(Integer::compareTo);
    return res;
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
