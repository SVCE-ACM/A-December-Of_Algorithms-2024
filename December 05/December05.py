n = int(input("Enter the number of people: "))
k = int(input("Enter the count: "))
people = [i for i in range(1, n + 1)]
index = 0
while len(people) > 1:
    index = (index + k - 1) % len(people)
    people.pop(index)
print(people[0])