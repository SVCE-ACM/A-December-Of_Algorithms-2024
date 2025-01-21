#include<stdio.h>
#include<stdlib.h>

int numberOfFloors()
{
    int n;
    printf("\nEnter the number of floors in the Magical Tower: ");
    scanf("%d", &n);
    return n;
}

int powerOf(int base, int power)
{
    int powerValue = 1, i;
    for(i = 0; i < power; i++)
    {
        powerValue = powerValue * base;
    }
    return powerValue;
}

int numberOfDigits(int number)
{
    int count = 0, r;
    while(number != 0)
    {
        count++;
        r = number % 10;
        number = number / 10;
    }
    return count;
}

int** constructTower(int numberOfFloors)
{
    int** array = (int**)malloc(numberOfFloors * sizeof(int*)), i;

    for(i = 0; i < numberOfFloors; i++)
    {
        int powerValue = powerOf(11, i);
        int digitCount = numberOfDigits(powerValue);

        array[i] = (int*)malloc(digitCount * sizeof(int));
        int idx = digitCount - 1;

        while(powerValue != 0)
        {
            array[i][idx] = powerValue % 10;
            idx--;
            powerValue = powerValue / 10;
        }
    }

    return array;
}

void display(int** array, int numberOfFloors)
{
    int i, j;
    printf("[");
    for(i = 0; i < numberOfFloors; i++)
    {
        int powerValue = powerOf(11,i);
        int digitCount = numberOfDigits(powerValue);
        printf("[");
        for(j = 0; j < digitCount; j++)    
        {
            if(j == digitCount - 1)

                printf("%d", array[i][j]);
            
            else

                printf("%d, ", array[i][j]);
            
        }
        printf("]");
        printf("\t");
    }
    printf("]");
}

void main()
{
   int n = numberOfFloors();
   int** tower = constructTower(n);
   display(tower, n);
}