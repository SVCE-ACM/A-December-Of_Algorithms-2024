from collections import deque

def process_ticket_requests(N, requests):
    vip_queue = deque()
    regular_queue = deque()
    
    for request in requests:
        parts = request.split()
        name = parts[0]
        tickets = int(parts[1])
        is_vip = len(parts) > 2 and parts[2] == "VIP"
        
        if is_vip:
            vip_queue.append((name, tickets))
        else:
            regular_queue.append((name, tickets))
    
    result = []
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
    
    for queue in [vip_queue, regular_queue]:
        while queue:
            name, tickets = queue.popleft()
            result.append(f"{name} was not served")
    
    return result

N1 = 5
requests1 = ["John 2 VIP", "Alice 3", "Bob 2", "Charlie 1 VIP"]
print(process_ticket_requests(N1, requests1))

N2 = 10
requests2 = ["Eve 4", "Diana 3 VIP", "Adam 5", "Frank 6 VIP"]
print(process_ticket_requests(N2, requests2))
