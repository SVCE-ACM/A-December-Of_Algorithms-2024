def find_missing(N, bib_numbers):
    total_sum = 0
    for i in range(1, N + 1):
        total_sum += i

    array_sum = 0
    for num in bib_numbers:
        array_sum += num

    missing_number = total_sum - array_sum
    return missing_number

N = 5
bib_numbers = [1, 2, 4, 5]
missing_bib = find_missing(N, bib_numbers)
print("The missing bib number is:",missing_bib)
