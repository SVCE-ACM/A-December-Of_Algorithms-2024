import java.util.*

fun canOrganizeBooks(books: List<Int>, shelfSize: Int): Boolean {
    if (books.size % shelfSize != 0) {
        return false
    }

    val bookCount = books.groupingBy { it }.eachCount().toMutableMap()
    val uniqueBooks = bookCount.keys.sorted()

    for (book in uniqueBooks) {
        while (bookCount[book]!! > 0) {
            for (i in 0 until shelfSize) {
                if (bookCount[book + i] == null || bookCount[book + i]!! <= 0) {
                    return false
                }
                bookCount[book + i] = bookCount[book + i]!! - 1
            }
        }
    }

    return true
}

fun main() {
    val books1 = listOf(1, 2, 3, 6, 2, 3, 4, 7, 8)
    val shelfSize1 = 3
    val books2 = listOf(1, 2, 3, 4, 5)
    val shelfSize2 = 4
    println(canOrganizeBooks(books1, shelfSize1))  // Output: true
    println(canOrganizeBooks(books2, shelfSize2))  // Output: false
}
