Rc, Bc = map(int, input("Enter Red And Blue Blocks Count: ").split(" "))
if abs(Rc - Bc) != 1:
    print("Not Possible!")
else:
    Greatest = 'R' if Rc > Bc else 'B'
    Smallest = 'R' if Rc < Bc else 'B'
    Min = min(Rc, Bc)
    result = []
    for i in range(Min):
        result.append(Greatest)
        result.append(Smallest)
    result.append(Greatest)
    print("Anagram: ", ''.join(result))
