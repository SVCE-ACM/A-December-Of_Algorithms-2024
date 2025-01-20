import java.util.*

fun canSplitSquad(N: Int, K: Int, D: Int, A: List<Int>): String {
    val subjectCounts = A.groupingBy { it }.eachCount()
    val uniqueSubjects = subjectCounts.size

    if (uniqueSubjects < K) {
        return "NO"
    }

    val maxTeamSize = (N + D) / 2
    val minTeamSize = (N - D) / 2

    if (subjectCounts.values.count { it <= minTeamSize } < K) {
        return "NO"
    }
    return "YES"
}
