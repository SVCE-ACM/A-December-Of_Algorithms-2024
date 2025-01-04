//(28) Bookshelf Organizer
#include <stdio.h>
#include <stdbool.h>

bool canOrganizeBooks(int* books, int booksSize, int shelfSize) {
    int count = 0;
    for (int i = 0; i < booksSize; i++) {
        if (i > 0 && books[i] != books[i - 1] + 1) {
            count = 1;
        } else {
            count++;
        }
        if (count == shelfSize) {
            count = 0;
        }
    }
    return count == 0;
}

int main() {
    int books1[] = {1, 2, 3, 6, 2, 3, 4, 7, 8};
    int books2[] = {1, 2, 3, 4, 5};
    int shelfSize1 = 3;
    int shelfSize2 = 4;
    
    printf("%s\n", canOrganizeBooks(books1, sizeof(books1) / sizeof(books1[0]), shelfSize1) ? "true" : "false");
    printf("%s\n", canOrganizeBooks(books2, sizeof(books2) / sizeof(books2[0]), shelfSize2) ? "true" : "false");
    
    return 0;
}

