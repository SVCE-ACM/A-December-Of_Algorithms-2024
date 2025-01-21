import java.util.*;
public class  Day29_java_Hari7467 {
    static Scanner sc = new Scanner(System.in);
    static class Node implements Comparable<Node> {
        int x, y, cost;

        Node(int x, int y, int cost) {
            this.x = x;
            this.y = y;
            this.cost = cost;
        }
        @Override
        public int compareTo(Node other) {
            return Integer.compare(this.cost, other.cost);
        }
    }
    public static int minCostWithPortals(int N, int M, int P, List<int[]> portals) {
        PriorityQueue<Node> pq = new PriorityQueue<>();
        pq.offer(new Node(1, 1, 0));
        int[][] dist = new int[N + 1][M + 1];
        for (int i = 1; i <= N; i++) {
            Arrays.fill(dist[i], Integer.MAX_VALUE);
        }
        dist[1][1] = 0;
        Map<String, List<int[]>> portalMap = new HashMap<>();
        for (int[] portal : portals) {
            int x1 = portal[0], y1 = portal[1], x2 = portal[2], y2 = portal[3], w = portal[4];
            portalMap.computeIfAbsent(x1 + "," + y1, k -> new ArrayList<>()).add(new int[]{x2, y2, w});
            portalMap.computeIfAbsent(x2 + "," + y2, k -> new ArrayList<>()).add(new int[]{x1, y1, w});
        }
        while (!pq.isEmpty()) {
            Node current = pq.poll();
            int x = current.x, y = current.y, cost = current.cost;
            if (x == N && y == M) {
                return cost;
            }
            String key = x + "," + y;
            if (portalMap.containsKey(key)) {
                for (int[] portal : portalMap.get(key)) {
                    int nx = portal[0], ny = portal[1], portalCost = portal[2];
                    int newCost = cost + portalCost;
                    if (newCost < dist[nx][ny]) {
                        dist[nx][ny] = newCost;
                        pq.offer(new Node(nx, ny, newCost));
                    }
                }
            }
        }
        return -1;
    }

    public static void main(String[] args) {
        System.out.println("Enter N (rows) and M (columns):");
        int N = sc.nextInt(), M = sc.nextInt();
        System.out.println("Enter P (number of portals):");
        int P = sc.nextInt();
        List<int[]> portals = new ArrayList<>();
        System.out.println("Enter portal details (x1 y1 x2 y2 W):");
        for (int i = 0; i < P; i++) {
            int x1 = sc.nextInt(), y1 = sc.nextInt();
            int x2 = sc.nextInt(), y2 = sc.nextInt();
            int w = sc.nextInt();
            portals.add(new int[]{x1, y1, x2, y2, w});
        }
        int result = minCostWithPortals(N, M, P, portals);
        if (result == -1) {
            System.out.println("No valid path exists.");
        } else {
            System.out.println("Minimum cost to reach (" + N + ", " + M + "): " + result);
        }
    }
}
