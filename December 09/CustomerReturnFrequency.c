#include<stdio.h>
#include<stdlib.h>

int inputReturns()
{
    int n;
    printf("\nEnter the number of customers who have returned their product: ");
    scanf("%d", &n);
    return n;
}

int* arrayReturns(int numberOfReturns)
{
    int* array = (int*)malloc(numberOfReturns * sizeof(int));
    printf("\nEnter the number of products returned by each customer: ");
    for(int i = 0; i < numberOfReturns; i++)
    {
        printf("\nEnter the number of products returned by customer-%d: ", i + 1);
        scanf("%d", &array[i]);
    }

    return array;
}

int returnOnce(int* array, int numberOfReturns)
{
    int count = 0;

    for(int i = 0; i < numberOfReturns; i++)
    {
        if(array[i] == 1)

            count++;
    }

    return count;
}

void main()
{
    int n = inputReturns();
    int* returns = arrayReturns(n);
    int countOfOne = returnOnce(returns, n);
    printf("Therefore, %d customers had returned their products exactly once", countOfOne);
}