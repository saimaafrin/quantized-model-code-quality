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

    List<Integer> steppingNumbers = new ArrayList<>();

    // loop through every possible number within the range.
    for (int number = low; number <= high; number++) {

      // assume the number is stepping at first.
      boolean isSteppingNumber = true;

      // convert the number to string.
      String numberAsString = String.valueOf(number);

      // loop through every character in the string.
      for (int i = 0; i < numberAsString.length() - 1; i++) {

        // convert the character to int.
        int current = Integer.parseInt(String.valueOf(numberAsString.charAt(i)));

        // convert the next character to int.
        int next = Integer.parseInt(String.valueOf(numberAsString.charAt(i + 1)));

        // if the difference between the current and the next number is not 1 or -1 then the number is not stepping.
        if (Math.abs(current - next) != 1) {
          isSteppingNumber = false;
          break;
        }
      }

      // if the number is stepping then add it to the list.
      if (isSteppingNumber) {
        steppingNumbers.add(number);
      }
    }
    return steppingNumbers;
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
