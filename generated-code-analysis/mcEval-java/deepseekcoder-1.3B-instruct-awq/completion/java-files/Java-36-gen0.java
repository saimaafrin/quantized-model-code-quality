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
    int[] nums = new int[12];
    for(int i=0; i<12; i++){
      nums[i] = i;
    }
    for(int i=0; i<nums.length; i++){
      int cur = nums[i];
      if(cur >= low && cur <= high){
        result.add(cur);
      }
      if(cur == 0 || cur > high){
        break;
      }
      int last = cur % 10;
      cur = cur * 10;
      if(last == 0){
        continue;
      }
      if((cur + last) <= high){
        result.add(cur + last);
      }
      if(last == 9){
        continue;
      }
      if((cur - last) >= low){
        result.add(cur - last);
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
