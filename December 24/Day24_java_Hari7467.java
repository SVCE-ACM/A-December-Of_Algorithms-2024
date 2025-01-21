import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;


public class Day24_java_Hari7467 {
    
    public static List<String> generateUniquePermutations(String str) {
        List<String> result = new ArrayList<>();
        char[] chars = str.toCharArray();
        Arrays.sort(chars);
        
        boolean[] used = new boolean[chars.length]; 
        backtrack(chars, used, new StringBuilder(), result);
        return result;
    }
    
    private static void backtrack(char[] chars, boolean[] used, StringBuilder current, List<String> result) {
        if (current.length() == chars.length) {
            result.add(current.toString());
            return;
        }
        
        for (int i = 0; i < chars.length; i++) {
            if (used[i] || (i > 0 && chars[i] == chars[i - 1] && !used[i - 1])) {
                continue;
            }
            
            used[i] = true; 
            current.append(chars[i]); 
            backtrack(chars, used, current, result);  
            used[i] = false;  
            current.deleteCharAt(current.length() - 1); 
        }
    }

    public static void main(String[] args) {
        String str = "abc";
        HashMap<Character,ArrayList<String>> map=new HashMap<>();
        List<String> permutations = generateUniquePermutations(str);
        ArrayList<String> list=new ArrayList<>();
        Character c=permutations.get(0).charAt(0);
        for (String permutation : permutations) {
            if(c==permutation.charAt(0))
            {
                list.add(permutation);
            }
            else{
                map.putIfAbsent(c,new ArrayList<>(list));
                list.clear();;
                c=permutation.charAt(0);
                list.add(permutation);
            }
        }
        map.putIfAbsent(c,new ArrayList<>(list));
        for (Map.Entry<Character, ArrayList<String>> entry : map.entrySet()) {
            Character key = entry.getKey();
            ArrayList<String> value = entry.getValue();
            System.out.println(key + ": " + value);
        }
    }
}
