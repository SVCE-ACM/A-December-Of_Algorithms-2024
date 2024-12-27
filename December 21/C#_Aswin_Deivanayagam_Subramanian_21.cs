using System;

class Node
{
    public int Data;
    public Node Next;

    public Node(int data)
    {
        Data = data;
        Next = null;
    }
}

class Program
{
    static Node CreateLinkedList(int[] values)
    {
        Node head = null;
        foreach (var value in values)
        {
            Node newNode = new Node(value);
            if (head == null)
            {
                head = newNode;
            }
            else
            {
                Node current = head;
                while (current.Next != null)
                {
                    current = current.Next;
                }
                current.Next = newNode;
            }
        }
        return head;
    }

    static string FindIntersection(Node head1, Node head2, int intersectionPos)
    {
        if (intersectionPos == 0)
        {
            return "No intersection found.";
        }

        Node current1 = head1;
        for (int i = 1; i < intersectionPos; i++)
        {
            if (current1 == null)
            {
                return "Invalid intersection position";
            }
            current1 = current1.Next;
        }

        Node current2 = head2;
        while (current1 != null)
        {
            if (current1 == current2)
            {
                return current1.Data.ToString();
            }
            current1 = current1.Next;
            current2 = current2.Next;
        }

        return "No intersection found.";
    }

    static void Main()
    {
        Console.Write("Enter the number of nodes in the first linked list: ");
        int n1 = int.Parse(Console.ReadLine());
        Console.Write("Enter the node values: ");
        int[] values1 = Array.ConvertAll(Console.ReadLine().Split(), int.Parse);

        Console.Write("Enter the number of nodes in the second linked list: ");
        int n2 = int.Parse(Console.ReadLine());
        Console.Write("Enter the node values: ");
        int[] values2 = Array.ConvertAll(Console.ReadLine().Split(), int.Parse);

        Console.Write("Enter the position of intersection: ");
        int intersectionPos = int.Parse(Console.ReadLine());

        Node head1 = CreateLinkedList(values1);
        Node head2 = CreateLinkedList(values2);

        string intersectionValue = FindIntersection(head1, head2, intersectionPos);
        Console.WriteLine(intersectionValue);
    }
}
