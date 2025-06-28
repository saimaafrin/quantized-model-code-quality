import java.util.*;

class Problem {
   /**
     * Given a list of numbers, determine how many items in the list are twice some other item in the same list.
     * 
     * Example:
     * >>> countDoubles(new int[] {1, 4, 3, 2, 9, 7, 18, 22})
     * 3
     * >>> countDoubles(new int[] {2, 4, 8, 10})
     * 2
     * >>> countDoubles(new int[] {7, 5, 11, 13, 1, 3})
     * 0
     */
    public static int countDoubles(int[] numbers)  {
        Map<Integer, Integer> countMap = new HashMap<>();
        for (int num : numbers) {
            countMap.put(num, countMap.getOrDefault(num, 0) + 1);
        }
        
        int count = 0;
        for (Map.Entry<Integer, Integer> entry : countMap.entrySet()) {
            if (entry.getValue() > 1 && numbers.contains(entry.getKey() * 2)) {
                count++;
            }
        }
        return count;
    }
    public static void main(String[] args) {
        // Test the function with different test cases
        assert countDoubles(new int[]{1, 2, 4, 8, 16}) == 4;
        assert countDoubles(new int[]{5, 10, 20, 40, 80}) == 4;
        assert countDoubles(new int[]{3, 6, 12, 24, 48}) == 4;
        System.out.println("All tests passed");
    }
}