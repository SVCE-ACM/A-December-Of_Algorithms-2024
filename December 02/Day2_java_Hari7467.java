class Day2_java_Hari7467 {
   
    private int[] wavePattern(int arr[]) {
        for (int i = 0; i < arr.length - 1; i++) {
            if (i % 2 == 0) {
               
                if (arr[i] > arr[i + 1]) {
                    swap(arr, i, i + 1);
                }
            } else {
               
                if (arr[i] < arr[i + 1]) {
                    swap(arr, i, i + 1);
                }
            }
        }
        return arr;
    }

    
    private void swap(int[] arr, int i, int j) {
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }

   
    private void show(int arr[]) {
        for (int i : arr) {
            System.out.print(i + " ");
        }
        System.out.println();
    }

   
    public static void main(String[] args) {
        int arr[] = {10, 5, 6, 3, 2, 20, 100, 80};
        Day2_java_Hari7467 obj = new Day2_java_Hari7467();

        if (arr.length > 1) {
            obj.show(obj.wavePattern(arr));
        } else {
            System.out.println("Array should have at least two elements");
        }
    }
}
