l = []
n = int(input("Enter number of tickets: "))
choice = 1

while choice != 0:
    a = str(input("Enter ticket details (e.g., name VIP/REG): "))
    l.append(a)
    choice = int(input("Do you want to enter more? (0 to stop)"))

l1 = []
l2 = []
l3 = []

for i in l:
    l1.append(i)
    if i.split()[1] == "VIP":
        l3.append(i)
    else:
        l2.append(i)

for i in l3:
    details = i.split()
    name = details[0]
    tickets_needed = int(details[1])
    
    if n > 0:
        c = 0
        while tickets_needed > 0 and n > 0:
            c += 1
            tickets_needed -= 1
            n -= 1
        if c > 0:
            print(name, "got", c, "tickets")
        if tickets_needed > 0:
            print("Tickets unavailable for", name, "!")

for i in l2:
    details = i.split()
    name = details[0]
    tickets_needed = int(details[1])
    
    if n > 0:
        c = 0
        while tickets_needed > 0 and n > 0:
            c += 1
            tickets_needed -= 1
            n -= 1
        if c > 0:
            print(name, "got", c, "tickets")
        if tickets_needed > 0:
            print("Tickets unavailable for", name, "!")
