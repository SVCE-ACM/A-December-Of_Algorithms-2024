N = int(input())
requests = [input() for _ in range(N)]

result = []
served = []

for request in requests:
    if "VIP" in request:
        temp = request.split()
        ticket = int(temp[-2])
        if N >= ticket:
            N -= ticket
            result.append(f"{temp[0]} purchased {temp[1]} tickets")
            served.append(temp[0])

for request in requests:
    if "VIP" not in request:
        temp = request.split()
        ticket = int(temp[-1])
        if N >= ticket:
            N -= ticket
            result.append(f"{temp[0]} purchased {temp[1]} tickets")
            served.append(temp[0])

flag = False
for request in requests:
    temp = request.split()
    if temp[0] not in served and not flag and N > 0:
        result.append(f"{temp[0]} purchased {N} tickets")
        served.append(temp[0])
        N = 0
        flag = True
    elif temp[0] not in served:
        result.append(f"{temp[0]} was not served")

print(result)
