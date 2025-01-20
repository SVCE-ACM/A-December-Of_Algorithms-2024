function smartTicketingSystem(N, requests) {
    const queue = [];
    const results = [];
    let availableTickets = N;

    requests.forEach(request => {
        const [customer, numTicketsStr, ...vipTag] = request.split(' ');
        const numTickets = parseInt(numTicketsStr, 10);
        const isVip = vipTag.includes("VIP");

        if (isVip) queue.unshift([customer, numTickets]);
        else queue.push([customer, numTickets]);
    });

    while (queue.length && availableTickets > 0) {
        const [customer, numTickets] = queue.shift();
        const ticketsAllocated = Math.min(numTickets, availableTickets);
        availableTickets -= ticketsAllocated;

        if (ticketsAllocated > 0) {
            results.push(`${customer} purchased ${ticketsAllocated} tickets`);
        } else {
            results.push(`${customer} was not served`);
        }
    }

    return results;
}
console.log(smartTicketingSystem(5, ["Alice 3", "Bob 2 VIP", "Charlie 4"]));
