import java.util.ArrayList;
import java.util.List;

public class Day20_java_Hari7467 {
    public static void main(String[] args) {
        int[] steps = {1, 2, 3}; 
        int distance = 4;      
        List<List<Integer>> combinations = findCombinations(steps, distance);
        System.out.println(combinations.size());
    }

    public static List<List<Integer>> findCombinations(int[] steps, int distance) {
        List<List<Integer>> result = new ArrayList<>();
        backtrack(steps, distance, new ArrayList<>(), result);
        return result;
    }

    private static void backtrack(int[] steps, int remaining, List<Integer> path, List<List<Integer>> result) {
        if (remaining == 0) {
            result.add(new ArrayList<>(path));
            return;
        }
        
        for (int step : steps) {
            if (step <= remaining) {
                path.add(step); 
                backtrack(steps, remaining - step, path, result);
                path.remove(path.size() - 1); 
            }
        }
    }
}
