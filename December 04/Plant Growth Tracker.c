#include<stdio.h>

int input()
{
    int numberOfMonths;
    printf("\nEnter the number of months: ");
    scanf("%d",&numberOfMonths);
    return numberOfMonths;
}

int predict(int numberOfMonths)
{
    int start = 0, next = 1, ctrl;
    int sum = start + next;
    for(ctrl = 2; ctrl < numberOfMonths; ctrl++)
    {
        start = next;
        next = sum;
        sum = start + next;
    }
    return sum;
}

int errorHandling(int numberOfMonths)
{
    if(numberOfMonths == 1)
    {
        return 1;
    }
    else if(numberOfMonths > 1)
    {
        return 0;
    }
    else
    {
        return -1;
    }
}

int main()
{
    int numberOfMonths = input();
    int error = errorHandling(numberOfMonths);
    if (error == 1)
    {
        printf("The plants take two months to grow before increasing in numbers.");
    }

    else if(numberOfMonths > 1)
    {
        int prediction = predict(numberOfMonths);
        printf("\nAfter %d months, there will be %d plants", numberOfMonths, prediction);
    }

    else
    {
        printf("Please enter the number of months as postive integers");
    }
    return 0;
}