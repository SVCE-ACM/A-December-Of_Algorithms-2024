from collections import Counter
from heapq import heappop, heappush

def can_organize_books(books, shelfSize):
    if len(books) % shelfSize != 0:
        return False

    book_count = Counter(books)
    unique_books = sorted(book_count.keys())

    for book in unique_books:
        while book_count[book] > 0:
            for i in range(shelfSize):
                if book_count[book + i] <= 0:
                    return False
                book_count[book + i] -= 1

    return True

books1 = [1, 2, 3, 6, 2, 3, 4, 7, 8]
shelfSize1 = 3
books2 = [1, 2, 3, 4, 5]
shelfSize2 = 4
print(can_organize_books(books1, shelfSize1)) 
print(can_organize_books(books2, shelfSize2)) 
