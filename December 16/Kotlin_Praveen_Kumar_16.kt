fun minPlatforms(arrivals: IntArray, departures: IntArray): Int {
    arrivals.sort()
    departures.sort()
    var platformsNeeded = 0
    var currentPlatforms = 0

    var i = 0
    var j = 0

    while (i < arrivals.size) {
        if (arrivals[i] <= departures[j]) {
            currentPlatforms++
            i++
        } else {
            currentPlatforms--
            j++
        }

        platformsNeeded = maxOf(platformsNeeded, currentPlatforms)
    }

    return platformsNeeded
}
