import java.util.ArrayList;
import java.util.List;

class Problem {

  /**
   * Return all integers in the range [1, n] in lexicographical order.
   *
   * @param n The upper limit of the range.
   * @return List of integers in lexicographical order.
   *
   * Example:
   * lexicalOrder(13)
   * Output: [1,10,11,12,13,2,3,4,5,6,7,8,9]
   */
  public static List<Integer> lexicalOrder(int n)  {
      List<Integer> result = new ArrayList<>();
      for (int i = 1; i < 10; ++i)
          dfs(i, n, result);
      return result;
  }
  public static void main(String[] args) {
    // Test cases
    assert lexicalOrder(13)
      .equals(
        new ArrayList<Integer>() {
          {
            add(1);
            add(10);
            add(11);
            add(12);
            add(13);
            add(2);
            add(3);
            add(4);
            add(5);
            add(6);
            add(7);
            add(8);
            add(9);
          }
        }
      ) : "Test case 1 failed";

    assert lexicalOrder(20)
      .equals(
        new ArrayList<Integer>() {
          {
            add(1);
            add(10);
            add(11);
            add(12);
            add(13);
            add(14);
            add(15);
            add(16);
            add(17);
            add(18);
            add(19);
            add(2);
            add(20);
            add(3);
            add(4);
            add(5);
            add(6);
            add(7);
            add(8);
            add(9);
          }
        }
      ) : "Test case 2 failed";

    assert lexicalOrder(2)
      .equals(
        new ArrayList<Integer>() {
          {
            add(1);
            add(2);
          }
        }
      ) : "Test case 3 failed";

    System.out.println("All tests passed");
  }
}
