fun minTrips(houses: List<Int>, W: Int): Int {
    var trips = 0
    var currentLoad = 0

    for (gifts in houses) {
        if (currentLoad + gifts > W) {
            trips += 1
            currentLoad = 0
        }
        currentLoad += gifts
    }

    if (currentLoad > 0) {
        trips += 1
    }

    return trips
}
