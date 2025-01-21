#include<stdio.h>

int inputRange()
{
    int n;
    printf("\nEnter the range: ");
    scanf("%d", &n);
    return n;
}

void digitManipulation(int n)
{
    int r, squareSum = 0;
    for(int i = 1; i <= n; i++)
    {
        int j = i;
        while(j != 0)
        {
            r = j % 10;
            squareSum = squareSum + r * r;
            j = j / 10;
        }
    }
    printf("\nSum of Square of all digits from 1 to %d is: %d", n, squareSum);
}

void main()
{
    int input = inputRange();
    digitManipulation(input);
}