import math

def flatlandSpaceStations(n, c):
    """Compute the maximum distance between any city to any space stations.

    Keyword arguments:
    n : Number of city (int)
    c : Cities owning a space station (int array)
	Return:
	maximum : Maximum distance between any space station and any city
    """

    maximum = 0

    stations = c[:]
    stations.sort()

    # Dist. between stations
    for i in range(len(stations)-1):
        diff = math.floor((stations[i+1] - stations[i])/2)
        maximum = max(maximum, diff)

    # Dist. between first station and first city
    maximum = max(maximum, stations[0])
    # Dist. between last station and last city
    maximum = max(maximum, math.floor(((n-1) - stations[-1])))

    return maximum
