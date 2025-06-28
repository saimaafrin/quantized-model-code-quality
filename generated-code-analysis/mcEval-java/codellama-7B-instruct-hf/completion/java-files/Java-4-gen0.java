import java.lang.*;
import java.util.*;

class Problem {

  /**
   * Given an array of distinct integers, return all possible permutations of the array.
   * >>> permute(new int[]{1,2,3})
   * [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
   * >>> permute(new int[]{0,1})
   * [[0,1],[1,0]]
   * >>> permute(new int[]{1})
   * [[1]]
   */
  public List<List<Integer>> permute(int[] nums)  {
    List<List<Integer>> result = new ArrayList<>();
    if (nums == null || nums.length == 0) {
      return result;
    }

    // base case: single element
    if (nums.length == 1) {
      List<Integer> permutation = new ArrayList<>();
      permutation.add(nums[0]);
      result.add(permutation);
      return result;
    }

    for (int i = 0; i < nums.length; i++) {
      // permutations of all elements except the i-th element
      List<List<Integer>> permutations = permute(removeAt(nums, i));
      // add each permutation with i-th element
      for (List<Integer> permutation : permutations) {
        permutation.add(0, nums[i]);
        result.add(permutation);
      }
    }

    return result;
  }
public static void main(String[] args) {
    Problem solution = new Problem();

    // Test the function with different test cases
    assert solution
      .permute(new int[] { 4, 5, 6 })
      .equals(
        Arrays.asList(
          Arrays.asList(4, 5, 6),
          Arrays.asList(4, 6, 5),
          Arrays.asList(5, 4, 6),
          Arrays.asList(5, 6, 4),
          Arrays.asList(6, 4, 5),
          Arrays.asList(6, 5, 4)
        )
      );
    assert solution
      .permute(new int[] { 7, 8 })
      .equals(Arrays.asList(Arrays.asList(7, 8), Arrays.asList(8, 7)));
    assert solution
      .permute(new int[] { 9 })
      .equals(Collections.singletonList(Collections.singletonList(9)));
    System.out.println("All tests passed");
  }
}