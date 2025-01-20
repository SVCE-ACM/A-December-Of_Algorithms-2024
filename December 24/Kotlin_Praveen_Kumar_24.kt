import kotlin.collections.*

fun groupPermutations(s: String): Map<Char, List<String>> {
    val uniquePermutations = s.toList().permutations().distinct().sorted()
    val grouped = mutableMapOf<Char, MutableList<String>>()
    for (perm in uniquePermutations) {
        grouped.getOrPut(perm.first()) { mutableListOf() }.add(perm.joinToString(""))
    }
    return grouped
}

fun List<Char>.permutations(): Set<List<Char>> {
    if (this.size == 1) return setOf(this)
    val result = mutableSetOf<List<Char>>()
    for (i in this.indices) {
        val sublist = this.toMutableList()
        val current = sublist.removeAt(i)
        val perms = sublist.permutations()
        for (perm in perms) {
            result.add(listOf(current) + perm)
        }
    }
    return result
}

fun main() {
    val inputString = "abc"
    val result = groupPermutations(inputString)
    println(result)
}
