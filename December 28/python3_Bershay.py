from collections import Counter

def canArrangeBooks(books, shelfSize):
    if len(books) % shelfSize != 0:
        return False
    
    book_count = Counter(books)
    books.sort()
    
    for book in books:
        if book_count[book] == 0:
            continue
        
        for i in range(shelfSize):
            if book_count[book + i] > 0:
                book_count[book + i] -= 1
            else:
                return False
    
    return True

books = list(map(int, input("Enter the list of books: ").split()))
shelfSize = int(input("Enter the shelf size: "))
print(canArrangeBooks(books, shelfSize))
