#include<stdio.h>
#include<stdlib.h>

int arraySize()
{
    int size;
    printf("\nEnter the number of elements in the array: ");
    scanf("%d", &size);
    return size;
}

int* createArray(int size)
{
    int* array = (int*)malloc(size * sizeof(int));
    int i;
    for(i = 0; i < size; i++)
    {
        printf("\nEnter element-%d: ", i+1);
        scanf("%d", &array[i]);
    }

    return array;
}

int inputTarget()
{
    int target;
    printf("\nEnter target element: ");
    scanf("%d", &target);
    return target;
}

int binarySearch(int searchElement, int* array, int size)
{
    int low = 0;
    int high = size - 1;
    int found = -1;

    while(low <= high)
    {
        // printf("\nLow Value: %d", low);
        // printf("\nHigh Value: %d", high);
        int middle = (low + high)/2;
        // printf("\nMiddle Index: %d", middle);
        int value = array[middle];
        // printf("\nMiddle value: %d", value);

        if(value < searchElement)

            low = middle + 1;

        else if(value > searchElement)

            high = middle - 1;

        else if(value == searchElement)
        {
            found = middle;
            break;
        }
    }
    return found;
}

void arraySort(int* array, int size)
{
    int ctrl1, ctrl2;
    int end = size - 1;
    for(ctrl1 = 0; ctrl1 < end; ctrl1++)
    {
        for(ctrl2 = ctrl1 + 1; ctrl2 < size; ctrl2++)
        {
            if(array[ctrl1] > array[ctrl2])
            {
                int temp = array[ctrl1];
                array[ctrl1] = array[ctrl2];
                array[ctrl2] = temp;
            }
        }
    }
}

void targetPairFinder(int target, int* array, int size)
{
    // printf("\n%d", size);
    arraySort(array, size);
    for(int i = 0; i < size; i++)
    {
        // printf("\nIteration-%d", i);
        // printf("\n");
        // for(int i = 0; i < size; i++)
        // {
        //     printf("%d\t", array[i]);
        // }
        // printf("\n");
        if(array[i] != 0 && array[i] < target)
        {
            int remaining = target - array[i];
            // printf("\nRemaining: %d", remaining);
            int idx = binarySearch(remaining, array, size);
            // printf("\nIndex: %d", idx);
            if(idx != -1 && array[i] != array[idx])
            {
                printf("(%d, %d)", array[i], array[idx]);
                array[i] = 0;
                array[idx] = 0;
                arraySort(array, size);
            }
            
        }
        // printf("\n\n");
        
    }
}

void main()
{
    int n = arraySize();
    int* input = createArray(n);
    int target = inputTarget();
    targetPairFinder(target, input, n);

    // int array[6] = {2, 4, 3, 7, 1, 5};
    // arraySort(array, 6);

    // for(int i = 0; i < 6; i++)
    // {
    //     printf("%d\t", array[i]);
    // }

    // int search = binarySearch(5, array, 6);

    // printf("\n%d", search);
}