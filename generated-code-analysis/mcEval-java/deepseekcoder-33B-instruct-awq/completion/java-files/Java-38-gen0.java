class Problem {

  /**
   * Given an integer n, determine if it is a power of two.
   * If it is, return true; otherwise, return false.
   * A number n is a power of two if there exists an integer x such that n == 2^x.
   *
   * @param n The integer to be checked.
   * @return True if n is a power of two, false otherwise.
   *
   * Example:
   * isPowerOfTwo(1)
   * Output: true
   *
   * Example:
   * isPowerOfTwo(16)
   * Output: true
   *
   * Example:
   * isPowerOfTwo(3)
   * Output: false
   *
   * Example:
   * isPowerOfTwo(4)
   * Output: true
   *
   * Example:
   * isPowerOfTwo(5)
   * Output: false
   */
  public static boolean isPowerOfTwo(int n)  {
    if(n <= 0) {
      return false;
    }

    if(n == 1) {
      return true;
    }

    while(n % 2 == 0) {
      n = n / 2;
    }

    return n == 1;
  }
  public static void main(String[] args) {
    // Test cases
    assert isPowerOfTwo(1024) == true; // 1024 is 2^10
    assert isPowerOfTwo(65536) == true; // 65536 is 2^16
    assert isPowerOfTwo(14) == false; // 14 is not a power of two

    System.out.println("All tests passed");
  }
}