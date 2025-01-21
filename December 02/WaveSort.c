#include<stdio.h>
#include<stdlib.h>

int arraySize()
{
    int n;
    printf("Enter the number of elements for array: ");
    scanf("%d", &n);
    return n;
}

int* createArray(int size)
{
    int ctrl;
    int* array = (int*)malloc(size * sizeof(int));
    for(ctrl = 0; ctrl < size; ctrl++)
    {
        printf("Enter element-%d: ",ctrl+1);
        scanf("%d", &array[ctrl]);
    }
    return array;
}

int* arraySort(int array[], int size)
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
    return array;
}

void display(int array[], int size)
{
    int ctrl;
    for(ctrl = 0; ctrl < size; ctrl++)
    {
        printf("%d\t",array[ctrl]);
    }
}

int* waveSort(int array[], int result[], int size)
{
    int end = size - 1;
    int ctrl = 0, ctrl1 = 0;
    int ctrl2 = end;
    while(ctrl1 < ctrl2)
    {
        result[ctrl] = array[ctrl2];
        ctrl++;
        result[ctrl] = array[ctrl1];
        ctrl++;
        ctrl1++;
        ctrl2--;
    }
    return result;
}

int main()
{
    int size = arraySize();
    int result[size];
    int* input = createArray(size);
    int* sortedInput = arraySort(input, size);
    int* output = waveSort(sortedInput, result, size);    
    display(output, size);
    return 0;
}