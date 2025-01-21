from collections import Counter
import heapq

def can_organize_books(books, shelfSize):
    if len(books) % shelfSize != 0:
        return False

    book_counts = Counter(books)
    unique_books = list(book_counts.keys())
    heapq.heapify(unique_books)

    while unique_books:
        start = unique_books[0]
        for i in range(start, start + shelfSize):
            if book_counts[i] == 0:
                return False
            book_counts[i] -= 1
            if book_counts[i] == 0:
                heapq.heappop(unique_books)
    return True
books1 = [1, 2, 3, 6, 2, 3, 4, 7, 8]
shelfSize1 = 3
books2 = [1, 2, 3, 4, 5]
shelfSize2 = 4

print(can_organize_books(books1, shelfSize1))  
print(can_organize_books(books2, shelfSize2))  
