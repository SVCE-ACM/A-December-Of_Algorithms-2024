int minPlatforms(List<int> arrivals, List<int> departures) {
  arrivals.sort();
  departures.sort();
  int platformsNeeded = 0;
  int currentPlatforms = 0;

  int i = 0;
  int j = 0;

  while (i < arrivals.length) {
    if (arrivals[i] <= departures[j]) {
      currentPlatforms += 1;
      i += 1;
    } else {
      currentPlatforms -= 1;
      j += 1;
    }

    platformsNeeded = (platformsNeeded > currentPlatforms) ? platformsNeeded : currentPlatforms;
  }

  return platformsNeeded;
}

void main() {
  List<int> arrivals = [900, 940, 950, 1100, 1500, 1800];
  List<int> departures = [910, 1200, 1120, 1130, 1900, 2000];
  print(minPlatforms(arrivals, departures)); // Output: 3
}
