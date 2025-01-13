from collections import deque

def TktCounter(N, requests):
    vip_queue = deque()
    regular_queue = deque()
    result = []

    for request in requests:
        parts = request.split()
        name = parts[0]
        tickets_requested = int(parts[1])
        is_vip = "VIP" in parts
        if is_vip:
            vip_queue.append((name, tickets_requested))
        else:
            regular_queue.append((name, tickets_requested))

    while N > 0 and (vip_queue or regular_queue):
        if vip_queue:
            customer, tickets_requested = vip_queue.popleft()
        else:
            customer, tickets_requested = regular_queue.popleft()

        if tickets_requested <= N:
            result.append(f"{customer} purchased {tickets_requested} tickets")
            N -= tickets_requested
        else:
            result.append(f"{customer} purchased {N} tickets")
            N = 0

    for queue in [vip_queue, regular_queue]:
        while queue:
            customer, _ = queue.popleft()
            result.append(f"{customer} was not served")

    return result

N = int(input("Enter No.Of Tickets: "))
Req_Booking = list(map(str,input("Enter Ticket Requests: ").split(",")))
print(f"Reservation Sheet!\n{TktCounter(N,Req_Booking)}")
