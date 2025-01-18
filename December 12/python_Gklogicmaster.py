from collections import deque

def smart_ticket(requests, total_tickets):
    vip_queue = deque()
    regular_queue = deque()
    
    # Separate VIP and regular requests
    for req in requests:
        parts = req.split()
        name, tickets = parts[0], int(parts[1])
        if len(parts) > 2 and parts[2].upper() == 'VIP':
            vip_queue.append((name, tickets))
        else:
            regular_queue.append((name, tickets))
    
    results = []
    
    # Process ticket requests
    while total_tickets > 0 and (vip_queue or regular_queue):
        queue = vip_queue if vip_queue else regular_queue
        name, tickets = queue.popleft()

        if tickets <= total_tickets:
            total_tickets -= tickets
            results.append(f"{name} received {tickets} tickets.")
        else:
            results.append(f"{name} received {total_tickets} tickets (not fully satisfied).")
            total_tickets = 0

    if total_tickets == 0:
        results.append("Tickets sold out.")
    return results

# Input
N = int(input("Enter the total tickets available: "))
print("Enter a list of requests (e.g., 'raja 3 VIP') enter 'end' to stop:")
l = []
while True:
    req = input()
    if req.lower() == "end":  # Type 'end' to finish input
        break
    l.append(req)

b=smart_ticket(l, N)
print(b)
