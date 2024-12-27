using System;
using System.Collections.Generic;

public class BookshelfOrganizer
{
    public static bool CanOrganizeBooks(int[] books, int shelfSize)
    {
        if (books.Length % shelfSize != 0)
            return false;

        Dictionary<int, int> bookCount = new Dictionary<int, int>();

        foreach (var book in books)
        {
            if (bookCount.ContainsKey(book))
                bookCount[book]++;
            else
                bookCount[book] = 1;
        }

        foreach (var book in bookCount.Keys)
        {
            if (bookCount[book] % shelfSize != 0)
                return false;
        }

        return true;
    }

    public static void Main(string[] args)
    {
        int[] books1 = { 1, 2, 3, 6, 2, 3, 4, 7, 8 };
        int shelfSize1 = 3;
        int[] books2 = { 1, 2, 3, 4, 5 };
        int shelfSize2 = 4;

        Console.WriteLine(CanOrganizeBooks(books1, shelfSize1)); // Output: True
        Console.WriteLine(CanOrganizeBooks(books2, shelfSize2)); // Output: False
    }
}
