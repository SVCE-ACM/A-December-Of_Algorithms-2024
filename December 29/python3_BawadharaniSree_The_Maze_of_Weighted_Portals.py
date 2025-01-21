import heapq

def find_min_weight_path(N, M, P, portals):
    # Graph initialization: rooms in grid are nodes, portals are edges
    adj = {}  # adjacency list for portals
    for portal in portals:
        x1, y1, x2, y2, W = portal
        if (x1, y1) not in adj:
            adj[(x1, y1)] = []
        if (x2, y2) not in adj:
            adj[(x2, y2)] = []
        adj[(x1, y1)].append(((x2, y2), W))
        adj[(x2, y2)].append(((x1, y1), W))

    # Dijkstra's algorithm setup
    start = (1, 1)
    end = (N, M)
    pq = [(0, start)]  # (accumulated weight, room)
    dist = {}  # dictionary to store minimum weight to reach each room
    dist[start] = 0
    
    while pq:
        current_weight, current_room = heapq.heappop(pq)
        
        # If we've reached the destination
        if current_room == end:
            return current_weight
        
        # Explore neighbors via portals
        if current_room in adj:
            for neighbor, weight in adj[current_room]:
                new_weight = current_weight + weight
                if neighbor not in dist or new_weight < dist[neighbor]:
                    dist[neighbor] = new_weight
                    heapq.heappush(pq, (new_weight, neighbor))
    
    return -1  # Return -1 if no valid path is found

# Function to get input from the user
def get_input():
    # Input the grid size
    N, M = map(int, input("Enter the number of rows (N) and columns (M): ").split())

    # Input the number of portals
    P = int(input("Enter the number of portals (P): "))
    
    # Input the portals
    portals = []
    for _ in range(P):
        x1, y1, x2, y2, W = map(int, input("Enter portal details (x1 y1 x2 y2 W): ").split())
        portals.append((x1, y1, x2, y2, W))
    
    return N, M, P, portals

# Main function
def main():
    N, M, P, portals = get_input()
    result = find_min_weight_path(N, M, P, portals)
    print("Minimum total weight:", result)

if __name__ == "__main__":
    main()
