program split_squad
  implicit none

  integer :: N, K, D
  integer, dimension(:), allocatable :: A
  integer :: i, max_team_size, min_team_size, unique_subjects
  integer :: count
  character(len=3) :: result
  integer, dimension(100) :: subject_counts

  ! Read inputs
  print *, 'Enter N, K, D: '
  read *, N, K, D
  print *, 'Enter the list of subjects (A): '
  allocate(A(N))
  read *, A

  ! Initialize subject_counts to zero
  subject_counts = 0

  ! Count frequency of each subject
  do i = 1, N
     subject_counts(A(i)) = subject_counts(A(i)) + 1
  end do

  ! Count unique subjects
  unique_subjects = 0
  do i = 1, 100
     if (subject_counts(i) > 0) then
        unique_subjects = unique_subjects + 1
     end if
  end do

  ! Check if the number of unique subjects is less than K
  if (unique_subjects < K) then
     result = 'NO'
  else
     max_team_size = (N + D) / 2
     min_team_size = (N - D) / 2
     count = 0

     ! Check if there are enough subjects with counts <= min_team_size
     do i = 1, 100
        if (subject_counts(i) > 0 .and. subject_counts(i) <= min_team_size) then
           count = count + 1
        end if
     end do

     if (count < K) then
        result = 'NO'
     else
        result = 'YES'
     end if
  end if

  ! Output the result
  print *, result

end program split_squad
