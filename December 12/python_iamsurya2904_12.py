from collections import deque

def smart_ticketing_system(N, requests):
    queue = deque()
    results = []
    available_tickets = N

    for request in requests:
        customer, num_tickets_str, *vip_tag = request.split()
        num_tickets = int(num_tickets_str)
        is_vip = "VIP" in vip_tag

        if is_vip:
            queue.appendleft((customer, num_tickets))
        else:
            queue.append((customer, num_tickets))

    while queue and available_tickets > 0:
        customer, num_tickets = queue.popleft()
        tickets_allocated = min(num_tickets, available_tickets)
        available_tickets -= tickets_allocated
        results.append(f"{customer} purchased {tickets_allocated} tickets" if tickets_allocated > 0 else f"{customer} was not served")

    return results

