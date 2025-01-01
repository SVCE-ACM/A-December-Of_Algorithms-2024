import java.util.Arrays;

public class java_NaveenKumar0502_wavesort {
    public static void waveSort(int[] arr) {
        // Sort the array
        Arrays.sort(arr);

        // Swap adjacent elements
        for (int i = 0; i < arr.length - 1; i += 2) {
            int temp = arr[i];
            arr[i] = arr[i + 1];
            arr[i + 1] = temp;
        }
    }

    public static void main(String[] args) {
        int[] arr = {10, 5, 6, 3, 2, 20, 100, 80};

        waveSort(arr);

        System.out.println(Arrays.toString(arr)); // Output: [5, 3, 10, 6, 20, 2, 100, 80]
    }
}
