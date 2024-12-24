import java.util.Arrays;

public class WaveSort {
    public static int[] waveSort(int[] arr) {
        Arrays.sort(arr);
        for (int i = 0; i < arr.length - 1; i += 2) {
            int temp = arr[i];
            arr[i] = arr[i + 1];
            arr[i + 1] = temp;
        }
        return arr;
    }

    public static void main(String[] args) {
        int[] result1 = waveSort(new int[]{10, 5, 6, 3, 2, 20, 100, 80});
        System.out.println(Arrays.toString(result1));

        int[] result2 = waveSort(new int[]{1, 2, 3, 4, 5, 6});
        System.out.println(Arrays.toString(result2));
    }
}
