import java.util.*

fun smartTicketingSystem(N: Int, requests: List<String>): List<String> {
    val queue: Deque<Pair<String, Int>> = ArrayDeque()
    val results = mutableListOf<String>()
    var availableTickets = N

    for (request in requests) {
        val parts = request.split(" ")
        val customer = parts[0]
        val numTickets = parts[1].toInt()
        val isVip = parts.size > 2 && parts[2] == "VIP"

        if (isVip) {
            queue.addFirst(Pair(customer, numTickets))
        } else {
            queue.add(Pair(customer, numTickets))
        }
    }

    while (queue.isNotEmpty() && availableTickets > 0) {
        val (customer, numTickets) = queue.poll()
        val ticketsAllocated = minOf(numTickets, availableTickets)
        availableTickets -= ticketsAllocated
        if (ticketsAllocated > 0) {
            results.add("$customer purchased $ticketsAllocated tickets")
        } else {
            results.add("$customer was not served")
        }
    }

    return results
}
