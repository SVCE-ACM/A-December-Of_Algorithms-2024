#include <stdio.h>
#include<stdlib.h>

int arraySize()
{
    int n;
    printf("Enter the value of n: ");
    scanf("%d",&n);
    return n;
}

int* createArray(int n)
{
    int ctrl1; 
    int* array = (int*)malloc(n * sizeof(int));
    
    for( ctrl1 = 0; ctrl1 < n; ctrl1++)
    {
        printf("Enter element-%d: ",ctrl1+1);
        scanf("%d",&array[ctrl1]);
    }
    return array;
}

int vanishingNumber(int array[], int n)
{
    int ctrl2 = 0, ctrl3 = 1, flag = 0;
    
    while (ctrl2 < n && ctrl3 <= n)
    {
        if (array[ctrl2] != ctrl3)
        {
            return ctrl3;
            flag = 1;
            break;
        }
        else
        {
            flag = 0;
            ctrl2++;
            ctrl3++;
        }
    }
    if(flag == 0)
    {
        return 0;
    }
}

int main()
{
    int size = arraySize();
    int* result = createArray(size);
    int missingNumber = vanishingNumber(result, size);
    if (missingNumber != 0)
    {
        printf("The missing number is: %d", missingNumber);
    }
    else
    {
        printf("The numbers are in order.");
    }
}

