from collections import deque

def process_ticket_requests(N, requests):
    queue = deque()
    for request in requests:
        parts = request.split()
        name = parts[0]
        tickets = int(parts[1])
        is_vip = len(parts) == 3 and parts[2] == "VIP"
        queue.append((name, tickets, is_vip))

    result = []
    vip_queue = deque()
    regular_queue = deque()

    while queue:
        name, tickets, is_vip = queue.popleft()
        if is_vip:
            vip_queue.append((name, tickets))
        else:
            regular_queue.append((name, tickets))

    while N > 0 and (vip_queue or regular_queue):
        if vip_queue:
            name, tickets = vip_queue.popleft()
        else:
            name, tickets = regular_queue.popleft()

        if tickets <= N:
            N -= tickets
            result.append(f"{name} purchased {tickets} tickets")
        else:
            result.append(f"{name} purchased {N} tickets")
            N = 0

    while vip_queue or regular_queue:
        if vip_queue:
            name, _ = vip_queue.popleft()
        else:
            name, _ = regular_queue.popleft()
        result.append(f"{name} was not served")

    return result


N = int(input("Enter the number of tickets available: "))
requests = []
print("Enter ticket requests (format: 'CustomerName NumberOfTickets [VIP]'):")
print("Type 'done' when finished.")

while True:
    request = input()
    if request.lower() == "done":
        break
    requests.append(request)


results = process_ticket_requests(N, requests)
for res in results:
    print(res)