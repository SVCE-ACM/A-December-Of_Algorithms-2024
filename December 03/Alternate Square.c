#include<stdio.h>

int number(char colour[])
{
    int n;
    printf("Enter the number of %s squares: ", colour);
    scanf("%d",&n);
    return n;
}

void display(char array[], int size)
{
    int ctrl;
    for(ctrl = 0; ctrl < size; ctrl++)
    {
        printf("%c\t",array[ctrl]);
    }
}

void redSequence(int numberOfRed, int numberOfBlue)
{
    int ctrl, idx = 0;
    int size = numberOfRed + numberOfBlue;
    char array[size];
    for(ctrl = 1; ctrl <= numberOfRed; ctrl++)
    {
        array[idx] = 'R';
        idx+=2;
    }
    idx = 1;
    for(ctrl = 1; ctrl <= numberOfBlue; ctrl++)
    {
        array[idx] = 'B';
        idx+=2;
    }
    display(array, size);
}
void blueSequence(int numberOfRed, int numberOfBlue)
{
    int ctrl, idx = 0;
    int size = numberOfRed + numberOfBlue;
    char array[size];
    for(ctrl = 1; ctrl <= numberOfRed; ctrl++)
    {
        array[idx] = 'B';
        idx+=2;
    }
    idx = 1;
    for(ctrl = 1; ctrl <= numberOfBlue; ctrl++)
    {
        array[idx] = 'R';
        idx+=2;
    }
    display(array, size);
}

void possibleArrangement(int numberOfRed, int numberOfBlue, int boolean)
{
    int twoRemaining = numberOfBlue - numberOfRed;
    int oneRemaining = numberOfRed - numberOfBlue;

    if(boolean == 1 && oneRemaining == 1)
    {
        printf("It is possible to form a sequence in which no two adjacent squares are of the same color\n");
        redSequence(numberOfRed, numberOfBlue);
    }

    else if(boolean == 2 && twoRemaining == 1)
    {
        printf("It is possible to form a sequence in which no two adjacent squares are of the same color\n");
        blueSequence(numberOfRed, numberOfBlue);
    }
    else if(boolean == 0 && oneRemaining == 0) 
    {
        printf("It is possible to form a sequence in which no two adjacent squares are of the same color\n");
        printf("Sequence-1: \n");
        redSequence(numberOfRed, numberOfBlue);

        printf("\nSequence-2: \n");
        blueSequence(numberOfRed, numberOfBlue);
    }

    else
    {
        printf("Not possible");
    }
}

void sizeCheck(int numberOfRed, int numberOfBlue)
{
    if(numberOfRed > numberOfBlue)
    {
        possibleArrangement(numberOfRed, numberOfBlue, 1);
    }

    else if(numberOfRed < numberOfBlue)
    {
        possibleArrangement(numberOfRed, numberOfBlue, 2);
    }

    else
    {
        possibleArrangement(numberOfRed, numberOfBlue, 0);
    }
}

int main()
{
    int red = number("red");
    int blue = number("blue");
    sizeCheck(red, blue);
    return 0;
}