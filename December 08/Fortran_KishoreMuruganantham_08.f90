program DigitSquareSum
    implicit none
    integer :: N, i, total_sum

    ! Function declaration
    integer :: digit_square_sum_of_number

    ! Input the value of N
    print *, "Enter the value of N:"
    read *, N

    ! Initialize total_sum
    total_sum = 0

    ! Calculate the total digit square sum
    do i = 1, N
        total_sum = total_sum + digit_square_sum_of_number(i)
    end do

    ! Print the result
    print *, "The total digit square sum is:", total_sum
end program DigitSquareSum

! Function to calculate the digit square sum of a single number
integer function digit_square_sum_of_number(num)
    implicit none
    integer :: num, digit, total

    ! Initialize total
    total = 0

    ! Calculate the square of each digit and sum them
    do while (num > 0)
        digit = mod(num, 10)
        total = total + digit * digit
        num = num / 10
    end do

    digit_square_sum_of_number = total
end function digit_square_sum_of_number
