using System;
using System.Collections.Generic;

class Program
{
    static List<string> SmartTicketingSystem(int N, List<string> requests)
    {
        var queue = new LinkedList<Tuple<string, int>>();
        var results = new List<string>();
        int availableTickets = N;

        foreach (var request in requests)
        {
            var parts = request.Split();
            string customer = parts[0];
            int numTickets = int.Parse(parts[1]);
            bool isVip = parts.Length == 3 && parts[2] == "VIP";

            if (isVip)
            {
                queue.AddFirst(new Tuple<string, int>(customer, numTickets));
            }
            else
            {
                queue.AddLast(new Tuple<string, int>(customer, numTickets));
            }
        }

        while (queue.Count > 0 && availableTickets > 0)
        {
            var firstCustomer = queue.First.Value;
            queue.RemoveFirst();

            string customer = firstCustomer.Item1;
            int numTickets = firstCustomer.Item2;
            int ticketsAllocated = Math.Min(numTickets, availableTickets);
            availableTickets -= ticketsAllocated;

            if (ticketsAllocated > 0)
            {
                results.Add($"{customer} purchased {ticketsAllocated} tickets");
            }
            else
            {
                results.Add($"{customer} was not served");
            }
        }

        return results;
    }

    static void Main()
    {
        var requests = new List<string>
        {
            "Alice 3 VIP",
            "Bob 2",
            "Charlie 5 VIP",
            "David 1"
        };

        var result = SmartTicketingSystem(5, requests);
        foreach (var res in result)
        {
            Console.WriteLine(res);
        }
    }
}
